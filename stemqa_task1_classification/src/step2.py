import os
import random
import sys

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    balanced_accuracy_score,
    confusion_matrix,
    f1_score,
    matthews_corrcoef,
    precision_score,
    recall_score,
)
from sklearn.preprocessing import StandardScaler


np.random.seed(42)
random.seed(42)


def _load_dataset(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    required_cols = {
        "event_time_idx",
        "session_intensity",
        "payment_stress",
        "support_backlog",
        "feature_usage_volatility",
        "is_escalation_risk",
    }
    if not required_cols.issubset(df.columns):
        missing = sorted(required_cols.difference(df.columns))
        raise ValueError(f"Missing required columns: {missing}")
    return df


def _engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.sort_values("event_time_idx", kind="mergesort").reset_index(drop=True).copy()
    # Lag and rolling statistics from time-ordered data
    out["session_intensity_lag1"] = out["session_intensity"].shift(1)
    out["payment_stress_lag2"] = out["payment_stress"].shift(2)
    out["support_backlog_roll5"] = out["support_backlog"].rolling(window=5, min_periods=1).mean()
    out["usage_volatility_roll7_std"] = (
        out["feature_usage_volatility"].rolling(window=7, min_periods=2).std()
    )
    out["intensity_x_stress"] = out["session_intensity"] * out["payment_stress"]
    out["payment_stress_sq"] = out["payment_stress"] ** 2
    out["support_backlog_abs"] = np.abs(out["support_backlog"])
    out["session_intensity_ewm12"] = out["session_intensity"].ewm(span=12, adjust=False).mean()

    # Deterministic imputation for lag/rolling edge rows
    out["session_intensity_lag1"] = out["session_intensity_lag1"].fillna(
        out["session_intensity"].iloc[0]
    )
    out["payment_stress_lag2"] = out["payment_stress_lag2"].fillna(out["payment_stress"].iloc[0])
    out["usage_volatility_roll7_std"] = out["usage_volatility_roll7_std"].fillna(0.0)
    return out


def _false_positive_rate(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred, labels=[0, 1]).ravel()
    denom = tn + fp
    return 0.0 if denom == 0 else float(fp / denom)


def run_pipeline() -> float:
    # Default: CSV in the same directory as this script (independent of process CWD).
    default_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), "customer_risk_events.csv")
    csv_path = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else default_csv
    df = _load_dataset(csv_path)
    df = _engineer_features(df)

    feature_cols = [
        "session_intensity",
        "payment_stress",
        "support_backlog",
        "feature_usage_volatility",
        "session_intensity_lag1",
        "payment_stress_lag2",
        "support_backlog_roll5",
        "usage_volatility_roll7_std",
        "intensity_x_stress",
        "payment_stress_sq",
        "support_backlog_abs",
        "session_intensity_ewm12",
    ]

    # Strict temporal split: train / validation / test
    train_end = 7600
    valid_end = 9800

    train = df.iloc[:train_end]
    valid = df.iloc[train_end:valid_end]
    test = df.iloc[valid_end:]

    X_train = train[feature_cols].to_numpy(dtype=np.float64)
    y_train = train["is_escalation_risk"].to_numpy(dtype=np.int64)
    X_valid = valid[feature_cols].to_numpy(dtype=np.float64)
    y_valid = valid["is_escalation_risk"].to_numpy(dtype=np.int64)
    X_test = test[feature_cols].to_numpy(dtype=np.float64)
    y_test = test["is_escalation_risk"].to_numpy(dtype=np.int64)
    valid_time = valid["event_time_idx"].to_numpy(dtype=np.float64)
    test_time = test["event_time_idx"].to_numpy(dtype=np.float64)

    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_valid_s = scaler.transform(X_valid)
    X_test_s = scaler.transform(X_test)

    model = LogisticRegression(
        solver="lbfgs",
        max_iter=1200,
        C=0.7,
        class_weight="balanced",
        random_state=42,
    )
    model.fit(X_train_s, y_train)

    # Hardening rule 1: fixed precision carry-through before thresholding
    valid_probs = np.round(model.predict_proba(X_valid_s)[:, 1], 6)
    thresholds = np.arange(0.18, 0.831, 0.005)
    eps = 1e-12
    late_valid_mask = valid_time >= np.quantile(valid_time, 0.75)

    # Hardening rule 2: constrained objective + global tie-break (not sequential best).
    # 1) Compute (threshold, feasible, objective) for every candidate.
    # 2) If any feasible exists, restrict to feasible rows; else use all rows.
    # 3) J_max = max objective in that set.
    # 4) Among rows with |J - J_max| <= eps, choose the largest threshold.
    rows = []
    for th in thresholds:
        pred_v = (valid_probs >= th).astype(np.int64)
        rec = recall_score(y_valid, pred_v, zero_division=0)
        prec = precision_score(y_valid, pred_v, zero_division=0)
        f1m = f1_score(y_valid, pred_v, average="macro", zero_division=0)
        bacc = balanced_accuracy_score(y_valid, pred_v)
        mcc = matthews_corrcoef(y_valid, pred_v)
        fpr = _false_positive_rate(y_valid, pred_v)
        late_rec = recall_score(y_valid[late_valid_mask], pred_v[late_valid_mask], zero_division=0)

        feasible = (rec >= 0.92) and (prec >= 0.88) and (late_rec >= 0.90)
        objective = 1.6 * f1m + 0.9 * bacc + 0.7 * mcc - 0.55 * fpr + 0.25 * late_rec
        rows.append((float(th), feasible, float(objective)))

    feasible_rows = [r for r in rows if r[1]]
    candidates = feasible_rows if feasible_rows else rows

    ths = np.array([r[0] for r in candidates], dtype=np.float64)
    objs = np.array([r[2] for r in candidates], dtype=np.float64)
    j_max = float(np.max(objs))
    near_max = np.abs(objs - j_max) <= eps
    best_threshold = float(np.max(ths[near_max]))

    test_probs = np.round(model.predict_proba(X_test_s)[:, 1], 6)
    test_pred = (test_probs >= best_threshold).astype(np.int64)
    test_f1_macro = f1_score(y_test, test_pred, average="macro", zero_division=0)
    test_fpr = _false_positive_rate(y_test, test_pred)
    test_mcc = matthews_corrcoef(y_test, test_pred)
    late_test_mask = test_time >= np.quantile(test_time, 0.75)
    test_late_recall = recall_score(y_test[late_test_mask], test_pred[late_test_mask], zero_division=0)

    # Single final numeric answer: composite risk triage quality index
    final_value = (
        0.50 * test_f1_macro
        + 0.25 * test_mcc
        + 0.15 * (1.0 - test_fpr)
        + 0.10 * test_late_recall
    )
    return float(final_value)


def main() -> None:
    result = run_pipeline()
    sys.stdout.write(f"{result:.3f}\n")


if __name__ == "__main__":
    main()

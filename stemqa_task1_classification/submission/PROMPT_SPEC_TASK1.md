# Prompt spec checklist — task1 (customer risk / matches current `src/step2.py`)

Sync this with `stemqa_task1_classification/src/step2.py` after any code edit.

- [ ] Input file: `customer_risk_events.csv` in the same directory as the solution script.
- [ ] Columns exactly: `event_time_idx`, `session_intensity`, `payment_stress`, `support_backlog`, `feature_usage_volatility`, `is_escalation_risk`.
- [ ] Sort by `event_time_idx`, stable sort (`mergesort`), then reset row index.
- [ ] Features:
  - [ ] `session_intensity_lag1` — lag 1; fill with first row `session_intensity`
  - [ ] `payment_stress_lag2` — lag 2; fill with first row `payment_stress`
  - [ ] `support_backlog_roll5` — mean, window 5, min_periods 1
  - [ ] `usage_volatility_roll7_std` — std, window 7, min_periods 2; NaN → 0.0
  - [ ] `intensity_x_stress`, `payment_stress_sq`, `support_backlog_abs`
  - [ ] `session_intensity_ewm12` — ewm span 12, adjust=False
- [ ] Feature column order for model: as in `feature_cols` in code.
- [ ] Splits: train rows `0:7600`, valid `7600:9800`, test `9800:` (iloc slices).
- [ ] `StandardScaler` fit on train only; transform valid/test.
- [ ] `LogisticRegression(solver='lbfgs', max_iter=1200, C=0.7, class_weight='balanced', random_state=42)`.
- [ ] Validation: `late_valid_mask` = `event_time_idx >= np.quantile(valid event_time_idx, 0.75)`.
- [ ] Round positive-class probabilities to **6** decimals before thresholding (valid and test).
- [ ] Thresholds: `np.arange(0.18, 0.831, 0.005)` (same as code).
- [ ] Per threshold on validation: recall, precision, macro F1, balanced accuracy, MCC, FPR (confusion_matrix labels `[0,1]`), late-subgroup recall.
- [ ] Feasible if: recall ≥ 0.92, precision ≥ 0.88, late recall ≥ 0.90.
- [ ] Objective: `1.6*f1_macro + 0.9*balanced_acc + 0.7*mcc - 0.55*fpr + 0.25*late_recall`.
- [ ] Prefer feasible thresholds; if none feasible, maximize objective over all thresholds.
- [ ] Tie-break: largest threshold if objective equal within `1e-12`.
- [ ] Test: `late_test_mask` = test `event_time_idx >= np.quantile(test event_time_idx, 0.75)`.
- [ ] Final scalar: `0.50*test_f1_macro + 0.25*test_mcc + 0.15*(1 - test_fpr) + 0.10*test_late_recall`.
- [ ] Print one value, **3** decimal places, no extra text.

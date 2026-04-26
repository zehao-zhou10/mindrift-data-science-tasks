"""Synthetic data generator for modular data science task pipelines."""

from __future__ import annotations

from pathlib import Path
import json

import numpy as np
import pandas as pd


def generate_synthetic_data(domain_prefix: str = "generic", n_rows: int = 2000) -> pd.DataFrame:
    """Generate synthetic event data and persist it as CSV.

    The output schema is:
    - user_id (string-like)
    - event_timestamp (datetime)
    - intensity_score (float)
    - category_tier (string)

    Notes:
    - Includes occasional >48 hour gaps per user to support Stage 1A session logic.
    - Writes to `{domain_prefix}_data.csv` in the current working directory.
    """
    if n_rows <= 0:
        raise ValueError("n_rows must be a positive integer")

    rng = np.random.default_rng(42)

    user_count = max(10, min(150, n_rows // 12))
    user_ids = [f"user_{i:04d}" for i in range(user_count)]
    tiers = np.array(["bronze", "silver", "gold", "platinum", "VIP"], dtype=object)

    sampled_users = rng.choice(user_ids, size=n_rows, replace=True)
    sampled_tiers = rng.choice(tiers, size=n_rows, p=[0.30, 0.30, 0.20, 0.10, 0.10], replace=True)

    # Build timestamps per user with occasional large jumps (>48h).
    base_time = pd.Timestamp("2024-01-01T00:00:00")
    user_offsets: dict[str, pd.Timestamp] = {uid: base_time for uid in user_ids}
    timestamps: list[pd.Timestamp] = []

    for uid in sampled_users:
        if rng.random() < 0.09:
            step_hours = float(rng.uniform(49, 96))  # force occasional >48h gap
        else:
            step_hours = float(rng.uniform(1, 16))
        user_offsets[uid] = user_offsets[uid] + pd.to_timedelta(step_hours, unit="h")
        timestamps.append(user_offsets[uid])

    # Intensity with tier + user + noise effects.
    tier_effect = {"bronze": 0.2, "silver": 0.6, "gold": 1.0, "platinum": 1.4, "VIP": 1.7}
    user_effects = {uid: float(rng.normal(0.0, 0.35)) for uid in user_ids}
    noise = rng.normal(0.0, 0.8, size=n_rows)
    trend = np.linspace(0.0, 0.3, n_rows)

    intensity = np.array(
        [
            5.0 + tier_effect[tier] + user_effects[uid] + noise[idx] + trend[idx]
            for idx, (uid, tier) in enumerate(zip(sampled_users, sampled_tiers))
        ],
        dtype=float,
    )
    intensity = np.clip(intensity, a_min=0.0, a_max=None)

    metadata = [
        json.dumps(
            {
                "base_score": float(round(score, 6)),
                "is_void": bool(rng.random() < 0.22),
            },
            separators=(",", ":"),
        )
        for score in intensity
    ]

    df = pd.DataFrame(
        {
            "user_id": pd.Series(sampled_users, dtype="string"),
            "event_timestamp": pd.to_datetime(timestamps, utc=False),
            "intensity_score": intensity.astype(float),
            "category_tier": pd.Series(sampled_tiers, dtype="string"),
            "metadata": pd.Series(metadata, dtype="string"),
        }
    )

    csv_path = Path(f"{domain_prefix}_data.csv")
    df.to_csv(csv_path, index=False)
    return df


if __name__ == "__main__":
    generate_synthetic_data()

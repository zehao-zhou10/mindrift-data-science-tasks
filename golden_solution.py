"""Auto-generated runnable golden solution for 1_SEMANTIC/2_SEMANTIC/3_SEMANTIC."""

import numpy as np
import pandas as pd
import json

np.random.seed(42)

df = pd.read_csv("fintech_data.csv")
df["event_timestamp"] = pd.to_datetime(df["event_timestamp"])
df = df.sort_values("event_timestamp").reset_index(drop=True)

# ------------------------------
# Stage 1
# ------------------------------
def parse_metadata(row):
    try:
        data = json.loads(row['metadata'])
        score = float(data.get('base_score', 0.0))
        is_void = data.get('is_void', False)
        if is_void:
            if row['category_tier'] == 'VIP':
                return 0.0
            else:
                return score * -1.0
        return score
    except:
        return np.nan

df['intensity_score'] = df.apply(parse_metadata, axis=1)
df = df.dropna(subset=['intensity_score'])

# If Stage 1 did not emit session_id, create deterministic fallback grouping.
if "session_id" not in df.columns:
    df = df.sort_values(["user_id", "event_timestamp"]).reset_index(drop=True)
    df["session_id"] = df["user_id"].astype(str)

# ------------------------------
# Stage 2
# ------------------------------
df = df.sort_values(['user_id', 'event_timestamp'])
df['is_weekend'] = df['event_timestamp'].dt.dayofweek.isin([5, 6])
cleared_totals = []
for user, user_df in df.groupby('user_id'):
    running_total = 0.0
    escrow_queue = [] # Stores [amount, subsequent_weekdays_seen]
    for _, row in user_df.iterrows():
        if row['is_weekend']:
            escrow_queue.append([row['intensity_score'], 0])
        else:
            running_total += row['intensity_score']
            for item in escrow_queue:
                item[1] += 1
        # Reverse iteration to safely pop from list
        for i in range(len(escrow_queue) - 1, -1, -1):
            if escrow_queue[i][1] == 3:
                running_total += escrow_queue[i][0]
                escrow_queue.pop(i)
        cleared_totals.append(running_total)
df['stage2_val'] = cleared_totals
df = df.drop(columns=['is_weekend'])

# Ensure stage3 has a canonical input column.
if 'stage2_val' not in df.columns:
    for _col in ['decayed_impact', 'rolling_ex_max', 'alt_cumsum']:
        if _col in df.columns:
            df['stage2_val'] = df[_col]
            break
if 'stage2_val' not in df.columns:
    raise ValueError('Stage 2 must create stage2_val directly or one of the known aliases.')

# ------------------------------
# Stage 3
# ------------------------------
group_max = df.groupby('user_id')['stage2_val'].max()
max_val = group_max.max()
tied_users = group_max[np.isclose(group_max, max_val, atol=1e-7)].index

if len(tied_users) > 1:
    def count_vowels(s):
        return sum(1 for char in str(s).lower() if char in 'aeiou')
    vowel_scores = pd.Series({u: count_vowels(u) for u in tied_users})
    max_vowels = vowel_scores.max()
    vowel_tied = vowel_scores[vowel_scores == max_vowels].index
    if len(vowel_tied) > 1:
        best_user = sorted(vowel_tied)[0]
    else:
        best_user = vowel_tied[0]
else:
    best_user = tied_users[0]

final_answer = round(df[df['user_id'] == best_user]['stage2_val'].max(), 4)

if "final_answer" not in locals():
    raise ValueError("Stage 3 must assign `final_answer`.")

print(final_answer)

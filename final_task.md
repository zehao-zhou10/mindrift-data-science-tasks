# Synthetic Data Science Task

## Backstory
A fintech analytics team is building a deterministic triage score for event streams.
The team must run a fixed 3-stage transformation-and-selection pipeline to ensure reproducible outputs
for audit and model-risk review. This task version uses Stage 1 `1_SEMANTIC`, Stage 2 `2_SEMANTIC`,
and Stage 3 `3_SEMANTIC` from your deviation library.

Use the generated dataset file: `fintech_data.csv`.

Stage keys selected: `1_SEMANTIC`, `2_SEMANTIC`, `3_SEMANTIC`.

## Combined Prompt
### Stage 1 Instruction

JSON Metadata Override: The dataset contains a `metadata` column formatted as stringified JSON. Extract the `base_score` from this JSON. If the JSON contains the key `"is_void": true`, the extracted score must be multiplied by -1. HOWEVER, there is an exception: If the user's `category_tier` (a separate column in the dataframe) is exactly 'VIP', a voided score does not become negative; it becomes exactly 0.0. Calculate this final `intensity_score` for all rows.

### Stage 2 Instruction

The Escrow Queue: Sort the data chronologically per `user_id`. Calculate a `stage2_val` (cleared cumulative spend) for each user. Rule 1: Any `intensity_score` from a transaction occurring Monday-Friday is cleared immediately and added to the user's running total. Rule 2: Any transaction occurring on a weekend (Saturday/Sunday) is put into an 'escrow' queue. Rule 3: A weekend transaction leaves escrow and is added to the running total ONLY AFTER the user makes exactly 3 subsequent weekday transactions. If 3 subsequent weekday transactions never occur, that specific weekend amount is never added.

### Stage 3 Instruction

Vowel-Weighted Tie-Breaker: Find the user(s) with the highest maximum `stage2_val`. If multiple users tie for this maximum value (difference < 1e-7), break the tie by calculating the 'Vowel Score' of their `user_id` string. The Vowel Score is the total number of vowels (A, E, I, O, U, case-insensitive) in the `user_id`. The user with the HIGHEST Vowel Score wins. If still tied, pick the user whose `user_id` comes first alphabetically. Return the maximum `stage2_val` of the winning user, rounded to 4 decimals.

## Combined Golden Code
```python
# ------------------------------
# Combined Golden Solution Script
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

```

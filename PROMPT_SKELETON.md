# Human Prompt Skeleton

> Replace all bracketed placeholders with your own text.

## Backstory
[Write a realistic data science scenario for fintech.]

## Data
Use `fintech_data.csv` with columns:
- `user_id`
- `event_timestamp`
- `intensity_score`
- `category_tier`

## Task Instructions
1) JSON Metadata Override: The dataset contains a `metadata` column formatted as stringified JSON. Extract the `base_score` from this JSON. If the JSON contains the key `"is_void": true`, the extracted score must be multiplied by -1. HOWEVER, there is an exception: If the user's `category_tier` (a separate column in the dataframe) is exactly 'VIP', a voided score does not become negative; it becomes exactly 0.0. Calculate this final `intensity_score` for all rows.
2) The Escrow Queue: Sort the data chronologically per `user_id`. Calculate a `stage2_val` (cleared cumulative spend) for each user. Rule 1: Any `intensity_score` from a transaction occurring Monday-Friday is cleared immediately and added to the user's running total. Rule 2: Any transaction occurring on a weekend (Saturday/Sunday) is put into an 'escrow' queue. Rule 3: A weekend transaction leaves escrow and is added to the running total ONLY AFTER the user makes exactly 3 subsequent weekday transactions. If 3 subsequent weekday transactions never occur, that specific weekend amount is never added.
3) Vowel-Weighted Tie-Breaker: Find the user(s) with the highest maximum `stage2_val`. If multiple users tie for this maximum value (difference < 1e-7), break the tie by calculating the 'Vowel Score' of their `user_id` string. The Vowel Score is the total number of vowels (A, E, I, O, U, case-insensitive) in the `user_id`. The user with the HIGHEST Vowel Score wins. If still tied, pick the user whose `user_id` comes first alphabetically. Return the maximum `stage2_val` of the winning user, rounded to 4 decimals.

## Output Requirement
[State exactly one final numeric output format, rounding policy, and units if any.]

## Determinism Notes
- [Specify precision carry-through expectations.]
- [Specify any tie-breakers.]
- [Specify defaults for any library behavior that must be fixed.]

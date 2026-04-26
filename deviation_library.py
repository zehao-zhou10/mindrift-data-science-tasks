"""Deviation library for synthetic task assembly.

Stage 1 contains concrete starter deviations.
Stage 2/3 are intentionally scaffold-only for user-provided logic.
"""

STAGE_1_DEVIATIONS = {
    "1_SEMANTIC": {
        "prompt_instruction": (
            "JSON Metadata Override: The dataset contains a `metadata` column formatted as stringified JSON. "
            "Extract the `base_score` from this JSON. If the JSON contains the key `\"is_void\": true`, the extracted score must be multiplied by -1. "
            "HOWEVER, there is an exception: If the user's `category_tier` (a separate column in the dataframe) is exactly 'VIP', "
            "a voided score does not become negative; it becomes exactly 0.0. Calculate this final `intensity_score` for all rows."
        ),
        "golden_code": (
            "def parse_metadata(row):\n"
            "    try:\n"
            "        data = json.loads(row['metadata'])\n"
            "        score = float(data.get('base_score', 0.0))\n"
            "        is_void = data.get('is_void', False)\n"
            "        if is_void:\n"
            "            if row['category_tier'] == 'VIP':\n"
            "                return 0.0\n"
            "            else:\n"
            "                return score * -1.0\n"
            "        return score\n"
            "    except:\n"
            "        return np.nan\n\n"
            "df['intensity_score'] = df.apply(parse_metadata, axis=1)\n"
            "df = df.dropna(subset=['intensity_score'])\n"
        ),
    }
}


STAGE_2_DEVIATIONS = {
    "2_SEMANTIC": {
        "prompt_instruction": (
            "The Escrow Queue: Sort the data chronologically per `user_id`. Calculate a `stage2_val` (cleared cumulative spend) for each user. "
            "Rule 1: Any `intensity_score` from a transaction occurring Monday-Friday is cleared immediately and added to the user's running total. "
            "Rule 2: Any transaction occurring on a weekend (Saturday/Sunday) is put into an 'escrow' queue. "
            "Rule 3: A weekend transaction leaves escrow and is added to the running total ONLY AFTER the user makes exactly 3 subsequent weekday transactions. "
            "If 3 subsequent weekday transactions never occur, that specific weekend amount is never added."
        ),
        "golden_code": (
            "df = df.sort_values(['user_id', 'event_timestamp'])\n"
            "df['is_weekend'] = df['event_timestamp'].dt.dayofweek.isin([5, 6])\n"
            "cleared_totals = []\n"
            "for user, user_df in df.groupby('user_id'):\n"
            "    running_total = 0.0\n"
            "    escrow_queue = [] # Stores [amount, subsequent_weekdays_seen]\n"
            "    for _, row in user_df.iterrows():\n"
            "        if row['is_weekend']:\n"
            "            escrow_queue.append([row['intensity_score'], 0])\n"
            "        else:\n"
            "            running_total += row['intensity_score']\n"
            "            for item in escrow_queue:\n"
            "                item[1] += 1\n"
            "        # Reverse iteration to safely pop from list\n"
            "        for i in range(len(escrow_queue) - 1, -1, -1):\n"
            "            if escrow_queue[i][1] == 3:\n"
            "                running_total += escrow_queue[i][0]\n"
            "                escrow_queue.pop(i)\n"
            "        cleared_totals.append(running_total)\n"
            "df['stage2_val'] = cleared_totals\n"
            "df = df.drop(columns=['is_weekend'])\n"
        ),
    }
}


STAGE_3_DEVIATIONS = {
    "3_SEMANTIC": {
        "prompt_instruction": (
            "Vowel-Weighted Tie-Breaker: Find the user(s) with the highest maximum `stage2_val`. "
            "If multiple users tie for this maximum value (difference < 1e-7), break the tie by calculating the 'Vowel Score' of their `user_id` string. "
            "The Vowel Score is the total number of vowels (A, E, I, O, U, case-insensitive) in the `user_id`. The user with the HIGHEST Vowel Score wins. "
            "If still tied, pick the user whose `user_id` comes first alphabetically. Return the maximum `stage2_val` of the winning user, rounded to 4 decimals."
        ),
        "golden_code": (
            "group_max = df.groupby('user_id')['stage2_val'].max()\n"
            "max_val = group_max.max()\n"
            "tied_users = group_max[np.isclose(group_max, max_val, atol=1e-7)].index\n\n"
            "if len(tied_users) > 1:\n"
            "    def count_vowels(s):\n"
            "        return sum(1 for char in str(s).lower() if char in 'aeiou')\n"
            "    vowel_scores = pd.Series({u: count_vowels(u) for u in tied_users})\n"
            "    max_vowels = vowel_scores.max()\n"
            "    vowel_tied = vowel_scores[vowel_scores == max_vowels].index\n"
            "    if len(vowel_tied) > 1:\n"
            "        best_user = sorted(vowel_tied)[0]\n"
            "    else:\n"
            "        best_user = vowel_tied[0]\n"
            "else:\n"
            "    best_user = tied_users[0]\n\n"
            "final_answer = round(df[df['user_id'] == best_user]['stage2_val'].max(), 4)\n"
        ),
    }
}
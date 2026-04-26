"""Task assembler: combines staged deviations into final prompt/code artifacts.

Also emits editable skeleton files for:
- Human-written prompt
- Human-readable explanation
- A reusable request template you can send to an assistant
"""

from __future__ import annotations

import argparse
import json
from itertools import product
from pathlib import Path

import numpy as np
import pandas as pd

from data_generator import generate_synthetic_data
from deviation_library import (
    STAGE_1_DEVIATIONS,
    STAGE_2_DEVIATIONS,
    STAGE_3_DEVIATIONS,
)

USED_COMBINATIONS_PATH = Path("used_stage_combinations.json")


def _get_stage_keys(stage_map: dict, stage_name: str) -> list[str]:
    keys = sorted(stage_map.keys())
    if not keys:
        raise ValueError(f"{stage_name} has no deviations configured. Add at least one key.")
    return keys


def _load_used_combinations(path: Path = USED_COMBINATIONS_PATH) -> list[list[str]]:
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}") from exc
    if not isinstance(data, list):
        raise ValueError(f"{path} must contain a JSON list")
    combos: list[list[str]] = []
    for row in data:
        if isinstance(row, list) and len(row) == 3 and all(isinstance(x, str) for x in row):
            combos.append(row)
    return combos


def _save_used_combinations(combos: list[list[str]], path: Path = USED_COMBINATIONS_PATH) -> None:
    path.write_text(json.dumps(combos, indent=2), encoding="utf-8")


def reset_used_combinations(path: Path = USED_COMBINATIONS_PATH) -> str:
    """Reset used stage combination history to empty."""
    _save_used_combinations([], path)
    return str(path.resolve())


def select_unused_combination(path: Path = USED_COMBINATIONS_PATH) -> tuple[str, str, str]:
    """Select the next unused (stage1, stage2, stage3) key tuple and persist it."""
    s1_keys = _get_stage_keys(STAGE_1_DEVIATIONS, "STAGE_1_DEVIATIONS")
    s2_keys = _get_stage_keys(STAGE_2_DEVIATIONS, "STAGE_2_DEVIATIONS")
    s3_keys = _get_stage_keys(STAGE_3_DEVIATIONS, "STAGE_3_DEVIATIONS")

    used = _load_used_combinations(path)
    used_set = {tuple(x) for x in used}

    for combo in product(s1_keys, s2_keys, s3_keys):
        if combo not in used_set:
            used.append(list(combo))
            _save_used_combinations(used, path)
            return combo
    raise RuntimeError("No unused stage combinations remain. Clear used_stage_combinations.json to recycle.")


def _resolve_deviation(stage_map: dict, key: str, stage_name: str) -> dict:
    if key in stage_map:
        return stage_map[key]
    return {
        "prompt_instruction": f"[{stage_name}] Placeholder selected: {key}. Add your deviation in deviation_library.py.",
        "golden_code": f"# [{stage_name}] Placeholder golden code for key '{key}'.\n",
    }


def _build_human_prompt_skeleton(
    domain_context: str,
    dataset_name: str,
    stage1_text: str,
    stage2_text: str,
    stage3_text: str,
) -> str:
    return f"""# Human Prompt Skeleton

> Replace all bracketed placeholders with your own text.

## Backstory
[Write a realistic data science scenario for {domain_context}.]

## Data
Use `{dataset_name}` with columns:
- `user_id`
- `event_timestamp`
- `intensity_score`
- `category_tier`

## Task Instructions
1) {stage1_text}
2) {stage2_text}
3) {stage3_text}

## Output Requirement
[State exactly one final numeric output format, rounding policy, and units if any.]

## Determinism Notes
- [Specify precision carry-through expectations.]
- [Specify any tie-breakers.]
- [Specify defaults for any library behavior that must be fixed.]
"""


def _build_human_explanation_skeleton(
    dataset_name: str,
    stage1_key: str,
    stage2_key: str,
    stage3_key: str,
) -> str:
    return f"""# Human-Readable Explanation Skeleton

## Dataset and Setup
- Load `{dataset_name}`.
- Confirm deterministic ordering and parsing assumptions.

## Stage-by-Stage Logic
- Stage 1 (`{stage1_key}`): [Explain what this stage does in plain English.]
- Stage 2 (`{stage2_key}`): [Explain the transformation/aggregation.]
- Stage 3 (`{stage3_key}`): [Explain final selection/scoring logic.]

## Why This Is Deterministic
- [Mention tie-breakers, thresholds, and precision handling.]

## Final Numeric Answer
- [Paste final value exactly as produced by golden code, with required rounding.]
"""


def _build_assistant_request_template(
    domain_context: str,
    dataset_name: str,
    stage1_key: str,
    stage2_key: str,
    stage3_key: str,
) -> str:
    return f"""You are helping me finalize a synthetic data science task package.

Context:
- Domain context: {domain_context}
- Dataset file: {dataset_name}
- Stage keys selected: {stage1_key}, {stage2_key}, {stage3_key}

I already have:
1) Combined prompt instructions
2) Combined golden code

Please generate:
1) A polished human-written prompt (markdown)
2) A human-readable explanation (markdown)

Constraints:
- Keep deterministic requirements explicit.
- Keep rounding/precision rules explicit.
- Do not include Python code in the human-written prompt.
- Keep wording professional and concise.

Input artifacts:
- final_task.md
- PROMPT_SKELETON.md
- HUMAN_EXPLANATION_SKELETON.md

Return both markdown sections in a copy-paste friendly format.
"""


def _build_backstory(domain_context: str, stage1_key: str, stage2_key: str, stage3_key: str) -> str:
    return f"""A {domain_context} analytics team is building a deterministic triage score for event streams.
The team must run a fixed 3-stage transformation-and-selection pipeline to ensure reproducible outputs
for audit and model-risk review. This task version uses Stage 1 `{stage1_key}`, Stage 2 `{stage2_key}`,
and Stage 3 `{stage3_key}` from your deviation library."""


def _build_stage2_adapter(stage2_key: str) -> str:
    """Normalize stage2 output to a canonical column `stage2_val` for stage3 consumption."""
    candidate_map = {
        "2A": "decayed_impact",
        "2B": "rolling_ex_max",
        "2C": "alt_cumsum",
    }
    preferred = candidate_map.get(stage2_key)
    preferred_line = (
        f"if '{preferred}' in df.columns:\n    df['stage2_val'] = df['{preferred}']\n"
        if preferred
        else ""
    )
    return (
        "# Ensure stage3 has a canonical input column.\n"
        + preferred_line
        + "if 'stage2_val' not in df.columns:\n"
        "    for _col in ['decayed_impact', 'rolling_ex_max', 'alt_cumsum']:\n"
        "        if _col in df.columns:\n"
        "            df['stage2_val'] = df[_col]\n"
        "            break\n"
        "if 'stage2_val' not in df.columns:\n"
        "    raise ValueError('Stage 2 must create stage2_val directly or one of the known aliases.')\n"
    )


def _tune_dataset_for_combination(
    df: pd.DataFrame,
    stage1_key: str,
    stage2_key: str,
    stage3_key: str,
) -> pd.DataFrame:
    """Inject deterministic edge-case rows for select combinations.

    Current tuning target:
    - 1A + 2A + 3A
      * Requires correct >48h session split
      * Requires Stage 2 lookahead + mean-fill behavior
      * Requires Stage 3 tie-break by variance (ddof=0)
    """
    if (stage1_key, stage2_key, stage3_key) == ("1_BOSS", "2_BOSS", "3_BOSS"):
        return _build_adversarial_boss_dataset(n_rows=len(df))
    if (stage1_key, stage2_key, stage3_key) != ("1A", "2A", "3A"):
        return df

    tuned = df.copy()
    tuned["event_timestamp"] = pd.to_datetime(tuned["event_timestamp"])
    # Keep background data well below crafted maxima so stage-3 decision is dominated by crafted sessions.
    tuned["intensity_score"] = tuned["intensity_score"].clip(upper=20.0)

    crafted_rows = [
        # Session A (variance == 0), all values same -> max stage2_val = 140
        {"user_id": "user_tie", "event_timestamp": "2024-06-01 00:00:00", "intensity_score": 80.0, "category_tier": "platinum"},
        {"user_id": "user_tie", "event_timestamp": "2024-06-01 01:00:00", "intensity_score": 80.0, "category_tier": "platinum"},
        {"user_id": "user_tie", "event_timestamp": "2024-06-01 02:00:00", "intensity_score": 80.0, "category_tier": "platinum"},
        # Gap > 48h forces new session under correct Stage-1 logic.
        # Session B (variance > 0), engineered to tie on max stage2_val = 140
        {"user_id": "user_tie", "event_timestamp": "2024-06-04 10:00:00", "intensity_score": 100.0, "category_tier": "platinum"},
        {"user_id": "user_tie", "event_timestamp": "2024-06-04 11:00:00", "intensity_score": 60.0, "category_tier": "platinum"},
        {"user_id": "user_tie", "event_timestamp": "2024-06-04 12:00:00", "intensity_score": 40.0, "category_tier": "platinum"},
    ]
    crafted_df = pd.DataFrame(crafted_rows)
    crafted_df["event_timestamp"] = pd.to_datetime(crafted_df["event_timestamp"])
    crafted_df["user_id"] = crafted_df["user_id"].astype("string")
    crafted_df["category_tier"] = crafted_df["category_tier"].astype("string")
    crafted_df["intensity_score"] = crafted_df["intensity_score"].astype(float)

    tuned = pd.concat([tuned, crafted_df], ignore_index=True)
    tuned = tuned.sort_values(["event_timestamp", "user_id"], kind="mergesort").reset_index(drop=True)
    return tuned


def _evaluate_boss_pipeline(df_in: pd.DataFrame, variant: str = "correct") -> float:
    """Evaluate 1_BOSS/2_BOSS/3_BOSS pipeline for a chosen bug variant."""
    df = df_in.copy()
    df["event_timestamp"] = pd.to_datetime(df["event_timestamp"])

    # Stage 1
    df = df.sort_values(["user_id", "event_timestamp"])
    session_ids: list[str] = []
    for user, user_df in df.groupby("user_id"):
        sess_idx = 0
        count = 0
        prev_time = None
        for _, row in user_df.iterrows():
            if prev_time is not None:
                cond_gap = (row["event_timestamp"] - prev_time) > pd.Timedelta(hours=48)
                cond_cap = count == 3
                if variant == "bug_stage1_and":
                    trigger_new = cond_gap and cond_cap
                elif variant == "bug_stage1_ge48":
                    trigger_new = ((row["event_timestamp"] - prev_time) >= pd.Timedelta(hours=48)) or cond_cap
                else:
                    trigger_new = cond_gap or cond_cap
                if trigger_new:
                    sess_idx += 1
                    count = 0
            session_ids.append(f"{user}_{sess_idx}")
            count += 1
            prev_time = row["event_timestamp"]
    df["session_id"] = session_ids

    # Stage 2
    df = df.sort_values("event_timestamp")
    result_frames = []
    for _, tier_df in df.groupby("category_tier"):
        tier_df = tier_df.copy()
        tier_df["peer_baseline"] = 0.0
        for idx, row in tier_df.iterrows():
            if variant == "bug_stage2_allow_same_user":
                mask = tier_df["event_timestamp"] < row["event_timestamp"]
            elif variant == "bug_stage2_leq_time":
                mask = (tier_df["event_timestamp"] <= row["event_timestamp"]) & (tier_df["user_id"] != row["user_id"])
            else:
                mask = (tier_df["event_timestamp"] < row["event_timestamp"]) & (tier_df["user_id"] != row["user_id"])
            valid_peers = tier_df[mask]
            if not valid_peers.empty:
                if variant == "bug_stage2_first_peer":
                    tier_df.at[idx, "peer_baseline"] = float(valid_peers.iloc[0]["intensity_score"])
                else:
                    tier_df.at[idx, "peer_baseline"] = float(valid_peers.iloc[-1]["intensity_score"])
        tier_df["stage2_val"] = tier_df["intensity_score"] - tier_df["peer_baseline"]
        result_frames.append(tier_df)
    df = pd.concat(result_frames).sort_values("event_timestamp")
    df = df.drop(columns=["peer_baseline"])

    # Stage 3
    group_sums = df.groupby("session_id")["stage2_val"].sum()
    interpolation = "linear" if variant == "bug_stage3_linear_q" else "nearest"
    cutoff = group_sums.quantile(0.80, interpolation=interpolation)
    top_sessions = group_sums[group_sums >= cutoff].index
    subset = df[df["session_id"].isin(top_sessions)]

    group_maxes = subset.groupby("session_id")["stage2_val"].max()
    unique_maxes = group_maxes.drop_duplicates().sort_values(ascending=False)
    second_highest_val = unique_maxes.iloc[1] if len(unique_maxes) > 1 else unique_maxes.iloc[0]

    tied_sessions = group_maxes[np.isclose(group_maxes, second_highest_val, atol=1e-7)].index
    if len(tied_sessions) > 1:
        group_stds = df[df["session_id"].isin(tied_sessions)].groupby("session_id")["stage2_val"].std(ddof=0)
        best_session = group_stds.idxmax() if variant == "bug_stage3_pick_max_std" else group_stds.idxmin()
    else:
        best_session = tied_sessions[0]

    final_answer = round(float(df[df["session_id"] == best_session]["intensity_score"].sum()), 4)
    return final_answer


def _score_boss_dataset(df: pd.DataFrame) -> tuple[int, float, dict[str, float]]:
    """Return (# bug variants that differ from correct, correct answer, all answers)."""
    variants = [
        "bug_stage1_and",
        "bug_stage1_ge48",
        "bug_stage2_allow_same_user",
        "bug_stage2_leq_time",
        "bug_stage2_first_peer",
        "bug_stage3_linear_q",
        "bug_stage3_pick_max_std",
    ]
    answers = {"correct": _evaluate_boss_pipeline(df, "correct")}
    for v in variants:
        answers[v] = _evaluate_boss_pipeline(df, v)
    mismatch_count = sum(1 for v in variants if answers[v] != answers["correct"])
    return mismatch_count, answers["correct"], answers


def _build_adversarial_boss_dataset(n_rows: int = 2000) -> pd.DataFrame:
    """Generate a deterministic edge-heavy dataset tuned for the BOSS pipeline."""
    rng = np.random.default_rng(314159)
    rows: list[dict[str, object]] = []

    # Core adversarial block: crafted timestamps/intensities to hit boundaries and tie logic.
    # User A: capacity split on 4th event within <48h (tests OR with count==3).
    rows.extend(
        [
            {"user_id": "A", "event_timestamp": "2024-01-01 00:00:00", "intensity_score": 60.0, "category_tier": "gold"},
            {"user_id": "A", "event_timestamp": "2024-01-01 01:00:00", "intensity_score": 20.0, "category_tier": "gold"},
            {"user_id": "A", "event_timestamp": "2024-01-01 02:00:00", "intensity_score": 60.0, "category_tier": "gold"},
            {"user_id": "A", "event_timestamp": "2024-01-01 03:00:00", "intensity_score": 20.0, "category_tier": "gold"},
        ]
    )

    # User B/C: same-timestamp and strict-before peer baseline edge cases.
    rows.extend(
        [
            {"user_id": "B", "event_timestamp": "2024-01-01 01:00:00", "intensity_score": 55.0, "category_tier": "gold"},
            {"user_id": "C", "event_timestamp": "2024-01-01 01:00:00", "intensity_score": 35.0, "category_tier": "gold"},
            {"user_id": "B", "event_timestamp": "2024-01-01 04:00:00", "intensity_score": 90.0, "category_tier": "gold"},
            {"user_id": "C", "event_timestamp": "2024-01-01 05:00:00", "intensity_score": 10.0, "category_tier": "gold"},
        ]
    )

    # User D: exact 48h boundary followed by >48h (tests > vs >=).
    rows.extend(
        [
            {"user_id": "D", "event_timestamp": "2024-01-02 00:00:00", "intensity_score": 40.0, "category_tier": "silver"},
            {"user_id": "D", "event_timestamp": "2024-01-04 00:00:00", "intensity_score": 41.0, "category_tier": "silver"},  # exactly 48h
            {"user_id": "D", "event_timestamp": "2024-01-06 01:00:00", "intensity_score": 42.0, "category_tier": "silver"},  # >48h
        ]
    )

    # Additional deterministic filler sessions to stabilize percentile cutoff behavior.
    base = pd.Timestamp("2024-02-01 00:00:00")
    users = [f"F{i:02d}" for i in range(28)]
    tiers = np.array(["bronze", "silver", "gold", "platinum"], dtype=object)
    for uid in users:
        t = base + pd.to_timedelta(float(rng.uniform(0, 36)), unit="h")
        for _ in range(4):
            step = float(rng.choice([2.0, 6.0, 12.0, 48.0, 60.0], p=[0.35, 0.30, 0.20, 0.10, 0.05]))
            t = t + pd.to_timedelta(step, unit="h")
            rows.append(
                {
                    "user_id": uid,
                    "event_timestamp": t,
                    "intensity_score": float(np.clip(rng.normal(18.0, 5.0), 2.0, 40.0)),
                    "category_tier": str(rng.choice(tiers, p=[0.25, 0.35, 0.25, 0.15])),
                }
            )

    df = pd.DataFrame(rows)
    df["event_timestamp"] = pd.to_datetime(df["event_timestamp"])
    df["user_id"] = df["user_id"].astype("string")
    df["category_tier"] = df["category_tier"].astype("string")
    df["intensity_score"] = df["intensity_score"].astype(float)
    df = df.sort_values(["event_timestamp", "user_id"], kind="mergesort").reset_index(drop=True)

    # Deterministic local search to increase sensitivity to common implementation bugs.
    best_df = df.copy()
    best_score, _, _ = _score_boss_dataset(best_df)
    for _ in range(45):
        cand = best_df.copy()
        idx = int(rng.integers(0, len(cand)))
        # Mostly perturb intensity; sometimes perturb timestamp by small discrete hours.
        if rng.random() < 0.8:
            delta = float(rng.choice([-8, -5, -3, -2, 2, 3, 5, 8]))
            cand.at[idx, "intensity_score"] = float(np.clip(cand.at[idx, "intensity_score"] + delta, 1.0, 120.0))
        else:
            h = int(rng.choice([-2, -1, 1, 2, 24, 48, 49]))
            cand.at[idx, "event_timestamp"] = pd.to_datetime(cand.at[idx, "event_timestamp"]) + pd.Timedelta(hours=h)
        cand = cand.sort_values(["event_timestamp", "user_id"], kind="mergesort").reset_index(drop=True)
        score, _, _ = _score_boss_dataset(cand)
        if score > best_score:
            best_df = cand
            best_score = score
            if best_score == 7:
                break

    return best_df


def _build_runnable_golden_script(
    dataset_name: str,
    stage1_key: str,
    stage2_key: str,
    stage3_key: str,
    s1_code: str,
    s2_code: str,
    s3_code: str,
) -> str:
    stage2_adapter = _build_stage2_adapter(stage2_key)
    return f'''"""Auto-generated runnable golden solution for {stage1_key}/{stage2_key}/{stage3_key}."""

import numpy as np
import pandas as pd
import json

np.random.seed(42)

df = pd.read_csv("{dataset_name}")
df["event_timestamp"] = pd.to_datetime(df["event_timestamp"])
df = df.sort_values("event_timestamp").reset_index(drop=True)

# ------------------------------
# Stage 1
# ------------------------------
{s1_code.rstrip()}

# If Stage 1 did not emit session_id, create deterministic fallback grouping.
if "session_id" not in df.columns:
    df = df.sort_values(["user_id", "event_timestamp"]).reset_index(drop=True)
    df["session_id"] = df["user_id"].astype(str)

# ------------------------------
# Stage 2
# ------------------------------
{s2_code.rstrip()}

{stage2_adapter.rstrip()}

# ------------------------------
# Stage 3
# ------------------------------
{s3_code.rstrip()}

if "final_answer" not in locals():
    raise ValueError("Stage 3 must assign `final_answer`.")

print(final_answer)
'''


def assemble_task(
    stage1_key: str,
    stage2_key: str,
    stage3_key: str,
    domain_context: str,
    n_rows: int = 2000,
) -> dict[str, str]:
    """Assemble final task artifacts and helper skeletons.

    Returns absolute paths for generated files.
    """
    df = generate_synthetic_data(domain_prefix=domain_context, n_rows=n_rows)

    s1 = _resolve_deviation(STAGE_1_DEVIATIONS, stage1_key, "STAGE 1")
    s2 = _resolve_deviation(STAGE_2_DEVIATIONS, stage2_key, "STAGE 2")
    s3 = _resolve_deviation(STAGE_3_DEVIATIONS, stage3_key, "STAGE 3")
    dataset_name = f"{domain_context}_data.csv"
    tuned_df = _tune_dataset_for_combination(df, stage1_key, stage2_key, stage3_key)
    tuned_df.to_csv(dataset_name, index=False)
    backstory = _build_backstory(domain_context, stage1_key, stage2_key, stage3_key)

    combined_prompt = "\n\n".join(
        [
            "### Stage 1 Instruction",
            s1["prompt_instruction"],
            "### Stage 2 Instruction",
            s2["prompt_instruction"],
            "### Stage 3 Instruction",
            s3["prompt_instruction"],
        ]
    )

    combined_code = "\n".join(
        [
            "# ------------------------------",
            "# Combined Golden Solution Script",
            "# ------------------------------",
            s1["golden_code"],
            s2["golden_code"],
            s3["golden_code"],
        ]
    )

    final_md = f"""# Synthetic Data Science Task

## Backstory
{backstory}

Use the generated dataset file: `{dataset_name}`.

Stage keys selected: `{stage1_key}`, `{stage2_key}`, `{stage3_key}`.

## Combined Prompt
{combined_prompt}

## Combined Golden Code
```python
{combined_code}
```
"""

    output_path = Path("final_task.md")
    output_path.write_text(final_md, encoding="utf-8")

    runnable_golden = _build_runnable_golden_script(
        dataset_name=dataset_name,
        stage1_key=stage1_key,
        stage2_key=stage2_key,
        stage3_key=stage3_key,
        s1_code=s1["golden_code"],
        s2_code=s2["golden_code"],
        s3_code=s3["golden_code"],
    )
    golden_script_path = Path("golden_solution.py")
    golden_script_path.write_text(runnable_golden, encoding="utf-8")

    prompt_skeleton = _build_human_prompt_skeleton(
        domain_context=domain_context,
        dataset_name=dataset_name,
        stage1_text=s1["prompt_instruction"],
        stage2_text=s2["prompt_instruction"],
        stage3_text=s3["prompt_instruction"],
    )
    explanation_skeleton = _build_human_explanation_skeleton(
        dataset_name=dataset_name,
        stage1_key=stage1_key,
        stage2_key=stage2_key,
        stage3_key=stage3_key,
    )
    assistant_request = _build_assistant_request_template(
        domain_context=domain_context,
        dataset_name=dataset_name,
        stage1_key=stage1_key,
        stage2_key=stage2_key,
        stage3_key=stage3_key,
    )

    prompt_skeleton_path = Path("PROMPT_SKELETON.md")
    explanation_skeleton_path = Path("HUMAN_EXPLANATION_SKELETON.md")
    assistant_prompt_path = Path("ASSISTANT_REQUEST_TEMPLATE.txt")

    prompt_skeleton_path.write_text(prompt_skeleton, encoding="utf-8")
    explanation_skeleton_path.write_text(explanation_skeleton, encoding="utf-8")
    assistant_prompt_path.write_text(assistant_request, encoding="utf-8")

    return {
        "selected_stage_keys": f"{stage1_key},{stage2_key},{stage3_key}",
        "dataset_csv": str(Path(dataset_name).resolve()),
        "golden_solution_py": str(golden_script_path.resolve()),
        "final_task_md": str(output_path.resolve()),
        "prompt_skeleton_md": str(prompt_skeleton_path.resolve()),
        "human_explanation_skeleton_md": str(explanation_skeleton_path.resolve()),
        "assistant_request_template_txt": str(assistant_prompt_path.resolve()),
    }


def assemble_task_with_new_combination(
    domain_context: str,
    n_rows: int = 2000,
    used_combinations_path: Path = USED_COMBINATIONS_PATH,
) -> dict[str, str]:
    """Pick an unused stage tuple, mark it used, then build full task artifacts."""
    s1, s2, s3 = select_unused_combination(path=used_combinations_path)
    return assemble_task(
        stage1_key=s1,
        stage2_key=s2,
        stage3_key=s3,
        domain_context=domain_context,
        n_rows=n_rows,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Assemble synthetic DS task artifacts.")
    parser.add_argument("--domain", default="generic", help="Domain prefix/context used for dataset naming.")
    parser.add_argument("--rows", type=int, default=2000, help="Number of synthetic rows to generate.")
    parser.add_argument(
        "--reset-used",
        action="store_true",
        help="Reset used_stage_combinations.json to an empty list and exit.",
    )
    args = parser.parse_args()

    if args.reset_used:
        reset_path = reset_used_combinations()
        print(f"reset_used_combinations: {reset_path}")
        raise SystemExit(0)

    # Default mode: automatically choose an unused stage combination.
    output_paths = assemble_task_with_new_combination(domain_context=args.domain, n_rows=args.rows)
    for name, path in output_paths.items():
        print(f"{name}: {path}")

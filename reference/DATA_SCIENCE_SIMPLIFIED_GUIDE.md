# Data Science Simplified Guide (Project Use)

## Scope Boundaries
- AI can assist with Step 2 Python code only.
- Human must write Prompt (Step 1) and Human-Readable Explanation (Step 2 narrative).

## Absolute Code Rules
- Start every script with:
  - np.random.seed(42)
  - random.seed(42)
- Allowed libraries only: stdlib, numpy, pandas, scipy, sklearn, sympy.
- No network I/O.
- Read only task input files; do not depend on hidden local files.
- Deterministic output every run.

## Data Science Task Shape (Preferred)
- Plausible professional scenario (risk scoring, forecasting, SLA analytics, anomaly triage).
- Explicit dataset schema and deterministic processing order.
- Time-safe split (if temporal): train/valid/test boundaries specified.
- Fully specified feature engineering rules and edge-row fills.
- Fully specified model hyperparameters.
- Fully specified threshold/selection/tie-break policy.
- Final answer = one numeric value only, exact rounding format stated.

## Prompt Quality Must-Haves
- Self-contained: all required constraints present.
- Deterministic: single unambiguous numeric answer.
- Computationally intensive: requires code, multi-step reasoning.
- Precision rules explicit (rounding mode/decimals/when applied).
- Units explicit if relevant.
- No Python code in the prompt text.
- Real-world plausible scenario.

## Step 2 Must-Haves
- Code output matches final numeric answer exactly.
- Runtime practical (<20 min target).
- Explanation written by human and mirrors code logic.

## Model Evaluation Target
- 10 responses total.
- Desired failures: 3-9 incorrect numeric answers.
- Invalid failures do not count (ambiguity, prompt flaws, formatting-only issues).

## Hardening Levers (Add 1-2 at a time)
- Explicit precedence rules (operation order).
- Piecewise thresholds with strict inequality details.
- Constrained optimization + deterministic fallback.
- Tie-break rule for equal objective values.
- Precision carry-through at intermediate stages.
- Verification hook metric combined into final scalar.

## Pre-Submission Checklist
- Prompt and code are perfectly aligned.
- Dataset file name + columns exactly match prompt text.
- Final number rounding/units exactly match requested format.
- Human explanation aligns with final code after last edits.

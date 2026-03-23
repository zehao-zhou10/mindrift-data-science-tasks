# Prompt spec checklist (generic — copy per task)

Use while writing **your own** prompt text. Replace placeholders with this task’s exact names.

- [ ] Real-world DS scenario is explicit and plausible.
- [ ] Input data source is explicit (file name + path as used in submission).
- [ ] Required columns / schema listed exactly (names and types if relevant).
- [ ] Row order / time column: sort key and stable sort rule stated.
- [ ] Feature engineering: each derived column, window sizes, `min_periods`, formulas.
- [ ] Edge / missing handling: exact fill rules for lags, rolling std, etc.
- [ ] Train / validation / test split: exact row ranges or time cutoffs (no leakage).
- [ ] Preprocessing: scaler fit scope (train only), model class and every hyperparameter.
- [ ] Any probability rounding **before** thresholding: decimals and rule.
- [ ] Threshold grid: start, end, step (inclusive/exclusive clear).
- [ ] Feasibility constraints on validation (recall, precision, subgroups, etc.).
- [ ] Objective to maximize/minimize when choosing threshold; tie-break rule.
- [ ] Fallback if no feasible threshold (if applicable).
- [ ] Final scalar: exact formula on **test** (metrics, weights, subgroup defs).
- [ ] Metric definitions: F1 averaging, FPR denominator, MCC, etc., as in code.
- [ ] Final output: one number only; rounding decimals; units if any.
- [ ] Float precision: e.g. float64 / IEEE-754 if the prompt requires it.

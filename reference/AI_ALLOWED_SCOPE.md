# AI Allowed Scope (Working Notes)

Allowed with AI assistance:
- Step 2 Python code implementation and refactoring.
- Code-level ideation and hardening iterations.
- Deterministic reproducibility checks and runtime checks.

Human-authored only:
- Final prompt text (Step 1).
- Human-readable explanation text (Step 2 narrative).

Operational constraints to enforce:
- Allowed libraries only: Python stdlib, numpy, pandas, scipy, sklearn, sympy.
- Deterministic seeds at script start:
  - np.random.seed(42)
  - random.seed(42)
- No network I/O.
- Use only task input files for file reads.
- Final output must be one numeric value in required format.

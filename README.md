# Mindrift Data Science Tasks

This repository contains my workflow for building and validating deterministic data science tasks used in evaluation pipelines.

## Repository Structure

- `reference/`  
  Project guidelines, quality standards, and hardening notes.
- `stemqa_task1_classification/`  
  A concrete task implementation and submission artifacts.
- `deviation_library.py`  
  Modular stage deviations used to compose synthetic tasks.
- `data_generator.py`  
  Synthetic dataset generator.
- `task_assembler.py`  
  End-to-end task assembly script (selects stage combo, generates dataset, golden solution, and skeleton docs).

## Quick Start

From repository root:

```powershell
python task_assembler.py --reset-used
python task_assembler.py --domain fintech --rows 2500
python golden_solution.py
```

This generates:

- `fintech_data.csv` (dataset)
- `final_task.md` (combined task prompt + code)
- `golden_solution.py` (runnable reference solution)
- `PROMPT_SKELETON.md` (fill-in template for human-written prompt)
- `HUMAN_EXPLANATION_SKELETON.md` (fill-in template for human explanation)

## What This Demonstrates

- Deterministic synthetic data generation
- Multi-stage transformation pipelines
- Reproducible golden-answer computation
- Prompt/explanation scaffolding for human-in-the-loop task authoring
- Scripted workflow for generating new stage combinations

## Notes

- Python cache and local virtual environments are ignored via `.gitignore`.
- Stage-combination history is tracked in `used_stage_combinations.json`.

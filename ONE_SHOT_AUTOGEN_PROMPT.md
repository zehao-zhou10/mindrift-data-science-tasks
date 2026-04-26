# One-Shot Task Generation Prompt

Use this exact instruction with the assistant to run the full pipeline in one request.

---

You are operating in this repository and must complete all steps end-to-end.

Goal:
Generate one brand-new synthetic data science task package using a stage combination I have not used before.

Repository files to use:
- `deviation_library.py`
- `data_generator.py`
- `task_assembler.py`
- `used_stage_combinations.json`

Required steps:
1. Select a **new** stage combination `(stage1_key, stage2_key, stage3_key)` that is not yet listed in `used_stage_combinations.json`.
2. Generate the task artifacts using that new combination (dataset + combined task markdown + skeleton files).
3. Ensure these output files are created/updated:
   - `final_task.md`
   - `PROMPT_SKELETON.md`
   - `HUMAN_EXPLANATION_SKELETON.md`
   - `ASSISTANT_REQUEST_TEMPLATE.txt`
   - `<domain_context>_data.csv`
4. In the skeleton files, keep clear fill-in placeholders where I should replace your text with my own writing.
5. Return:
   - Selected stage keys
   - Absolute paths of generated files
   - A short “what to fill in” checklist for the two skeleton files

Execution notes:
- Prefer using `task_assembler.assemble_task_with_new_combination(...)`.
- Keep Stage 2 and Stage 3 logic exactly as configured in `deviation_library.py` (no extra invention).
- Do not delete existing deviations.

Inputs for this run:
- `domain_context`: [REPLACE_ME_DOMAIN]
- `n_rows`: [REPLACE_ME_ROW_COUNT]

---

Suggested values:
- `domain_context = fintech`
- `n_rows = 2000`

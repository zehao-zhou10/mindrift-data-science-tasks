# Project Guidelines (Full Copy)

Project overview
Note: This is the most important article in the CI STEM Q&A project repository. Ensure you have read the entire document and keep it on hand for reference while you work through tasks. Reading time: 45–60 minutes.

Mission: Produce a diverse collection of challenging STEM problems that will be solved using Python programming with standard libraries and multi-step reasoning. Problems that are computationally intensive, professionally relevant, and diverse, and are explicitly designed to push the limits of model reasoning and trigger model failures, while remaining solvable by a human with code.

The Core Philosophy:  Unlike textbook-style exercises, these problems reflect the kinds of computational tasks encountered in scientific and professional workflows – tasks that cannot reasonably be solved by hand, but instead require careful coding and reasoning.

Task structure: Consists of 3 steps:

Step 1 is the generation of a well-formed prompt that sets up a computationally intensive STEM problem

Step 2 is the creation of a golden solution, which consists of a correct final answer, Python code, and a clear human-readable explanation

Step 3 is evaluation of the model’s responses to confirm that it fails for valid reasoning-based reasons

                                                         START

                                                            │

                                                            ▼

              ╔═══════════════════════════════════╗

              ║                         STEP 1: PROMPT WRITING                       ║

              ║                    • Craft multi-step STEM problem                  ║

              ║                    • Deterministic & professional                      ║

              ╚═══════════════════════════════════╝

                                                           │

                                                           ▼

              ╔═══════════════════════════════════╗

              ║                        STEP 2: GOLDEN SOLUTION                      ║

              ║                   • Python code + Explanation                          ║

              ║                   • Final Answer                                                 ║

              ╚═══════════════════════════════════╝

                                                         │

                                                         ▼

              ╔═══════════════════════════════════╗

              ║                          STEP 3: MODEL EVALUATION                  ║

              ║                        • Run 10 model responses                        ║

              ║                        • Target: 3–9 valid failures                         ║

              ╚═══════════════════════════════════╝

                                                     │

                                                     ▼

                                                SUBMIT


                     

Task Creation Steps in a Nutshell
Step 1: Generate the Prompt
Create an original, professional STEM problem

Run the Prompt Quality Criteria autochecks below the prompt text field

Autochecks are guides only – they are not a QA signal. Failed autochecks must either be rerun or overridden with reasoning

Prompts must be:

Fully self-contained (no missing required inputs)

Deterministic (one correct numeric answer)

Computationally intensive (requires code, 3–5+ reasoning steps)

Clearly state precision, rounding, and units

❌ Do not include code in the prompt

 

Step 2: Write the Golden Solution
Provide:

✅ Correct Python code (allowed libraries only)

✅ Clear human-readable explanation

✅ Final numeric answer (correct rounding & units)

Code and explanation must match exactly and solve the prompt accurately

Run and review the Solution autochecks

 

Step 3: Evaluate Model Responses
Generate 10 model responses

Count incorrect answers:

✅ 3–9 wrong → good difficulty

❌ 0–2 wrong → too easy → harden prompt

❌ 10 wrong → too hard → check prompt or add hints

Failures must be due to model reasoning, not prompt flaws or rounding/tolerance

 

Final Checks Before Submission
Prompt is complete, original, precise, and plausible

Single unambiguous numeric answer

3–9 valid model failures

Solution is correct, reproducible, and well-explained

Autochecks reviewed (but not relied on)

AI usage will be tracked. You may only use AI to write your Python code – nothing else!

 

Video Library
Follow the link below to our video library to take in bite-sized chunks of the content contained within the guidelines and supplementary materials. These videos cover most of the CI STEM Q&A project content and expectations (from how to think about task creation to quality criteria, common errors, and more).

CI STEM Q&A Google Drive Video Library

 

STEP 1 – Prompt Creation 
Section 1: Prompt Requirements (Zero Error Tolerance)
If any of these checks fail, the prompt is immediately rejected.

At the generation stage, you must create a prompt that meets the basic criteria of this project. This section guides you how to create a good prompt and prevents wasted effort on tasks that will be automatically rejected. The prompt must adhere to the following requirements: 

 1.1 Completeness
Requirement: The prompt must specify all information that is necessary to uniquely determine the correct numeric output without external lookups or follow-up questions. This includes: all required input values or data sources, the target quantity, any nonstandard assumptions, and any conventions that could change the result (the constraints might be a logical consequence of the previous ones, not all of them should be explicitly spelt out). Domain knowledge is allowed (and expected) for standard, widely accepted conventions in the chosen subdomain, provided they do not introduce ambiguity or multiple plausible solution paths. If a convention is not contextually universal, has common variants, or materially affects the numeric result, it must be explicitly stated in the prompt.

Check: Could two competent solvers in the same subdomain, applying standard practice, still produce different correct answers due to interpretation? If yes → incomplete. If no → complete.

Examples:

✅ Acceptable implicit domain knowledge

“Compute the Euclidean norm of the residual vector” (no alternative meaning in-context)

“Use OLS regression” when you also specify intercept handling and data preprocessing rules if relevant

❌ Not acceptable to leave implicit (must specify)

“Compute the AUC” (ROC vs PR, macro vs micro, tie handling)

“Use standard numerical integration” (trapezoid vs Simpson; step size; endpoints)

“Compute the 99th percentile” (linear interpolation vs nearest-rank can change result)

For more: SEE THE PROMPT COMPLETENESS GUIDE HERE.

 

 1.2 Uniqueness
Requirement: Must be original. Do not recycle open-source problem sets or use a template when creating prompts. 

Check: Is this an original problem, not directly copy pasted from online resources, textbooks?

 

1.3 Precision & Numerical Rules
Requirement: The prompt must explicitly specify the numerical precision conventions that affect the final numeric result, including:

Arithmetic precision (e.g., IEEE-754 binary64 / float64 for all real-valued computations)

Rounding rule for the final output (e.g., round-half-to-even vs round-half-away-from-zero)

Rounding target (maximum 3 decimals) and the exact count

Any mandatory intermediate rounding / truncation / clamping, including when it is applied (after each step, each iteration, per update, etc.)

Do not include any tolerance by default.

Check: Could two competent solvers implement the same method but still get different final numbers due to different floating-point / rounding / tolerance choices? If yes → precision rules are incomplete.

 

1.4 Language Specificity
Language Specificity: Written in clear US English with no grammar or usage errors. It is structured in a natural, coherent flow that clearly communicates the user intent.

Check: Is the prompt grammatically correct and clearly written in US English?

 

1.5 Formatting
Formatting: Prompt is clear and readable (Markdown/KaTeX/LaTeX/Unicode allowed). It is no longer than 7,000 characters, contains no explicit code (pseudocode is allowed), and maintains a consistent, easy-to-read visual structure.

Check: Is the prompt well-formatted, Py code-free, and within token limits?

 

1.6 Plausibility  
Requirement: The task's situation must resemble a relatively plausible, real-world, practical, professional, or scientific scenario, focusing on the constraints and decision-making processes encountered in applied STEM work rather than being a contrived puzzle, a basic coding challenge, or a purely academic example.

Check: Does the core logic of this scenario mirror a challenge a professional might actually need to solve?

 

1.7 STEM Domain Relevance
Requirement: The prompt must be within STEM domain (mathematics, physics, computer science, engineering, data science). Subdomains selectable via dropdown in task UI.

Check: Does the prompt correctly exercise the intended STEM domain and subdomain?

 

1.8 ‼️ AI Usage Forbidden ‼️
Requirement: You may use AI assistance for ideation purposes and to assist with writing code, but you may not use any AI assistance in writing task prompts or providing human reasoning steps. If you are suspected of using AI to write prompts or the human reasoning steps, you will be removed from production and potentially the Mindrift platform.

Check: Was any AI assistance used to generate the task prompt or the human reasoning steps?

 

1.9 Autochecks
Requirement: You must run all autochecks provided in the UI. They can help you sense-check the validity of multiple elements of your task. If any of these fail, use your understanding of the project requirements, as well as your domain expertise, to determine whether the autocheck failure is valid or not. All failed autochecks must either be addressed through task improvements or overridden with an explanation on why the verdict is incorrect.

Note: Autochecks are NOT QA signals. If your task passes all autochecks, this does NOT mean it will automatically make it through QA. QA comments on redo/rejected tasks always take precedence.

 

1.10 Decision Path
                            START

                                |

                                v

              +------------------------------------+

              |        1.1 COMPLETE                |

              |  Is the problem self-contained     |

              |  and solvable without external     |

              |  lookups or clarifying questions?  |

              +------------------------------------+

                                |

                 +--------------+--------------+

                 |                             |

                NO                            YES

                 |                             |

                 v                             v

        +------------------+       +------------------------+

        |   REJECT         |       |      1.2 UNIQUE        |

        |   (Incomplete)   |       |  Is this original,     |

        +------------------+       |  not copy-pasted from  |

                                   |  online or textbooks?  |

                                   +------------------------+

                                              |

                                +--------------+--------------+

                                |                             |

                               NO                            YES

                                |                             |

                                v                             v

                      +------------------+       +------------------------+

                      |   REJECT         |       |  1.3 LANGUAGE          |

                      |   (Not Original) |       |  Is it grammatically   |

                      +------------------+       |  correct US English?   |

                                                 +------------------------+

                                                            |

                                              +--------------+--------------+

                                              |                             |

                                             NO                            YES

                                              |                             |

                                              v                             v

                                    +------------------+       +------------------------+

                                    |   REJECT         |       |  1.4 FORMATTING        |

                                    |   (Language)     |       |  Well-formatted,       |

                                    +------------------+       |  code-free, in limits? |

                                                               +------------------------+

                                                                          |

                                                            +--------------+--------------+

                                                            |                             |

                                                           NO                            YES

                                                            |                             |

                                                            v                             v

                                                  +------------------+       +------------------------+

                                                  |   REJECT         |       |  1.5 PLAUSIBILITY      |

                                                  |   (Format)       |       |  Would a professional  |

                                                  +------------------+       |  encounter this?       |

                                                                             +------------------------+

                                                                                        |

                                                                          +--------------+--------------+

                                                                          |                             |

                                                                         NO                            YES

                                                                          |                             |

                                                                          v                             v

                                                                +------------------+       +------------------------+

                                                                |   REJECT         |       |  1.6 STEM DOMAIN       |

                                                                |   (Contrived)    |       |  Does it exercise a    |

                                                                +------------------+       |  STEM domain?          |

                                                                                           +------------------------+

                                                                                                      |

                                                                                        +--------------+--------------+

                                                                                        |                             |

                                                                                       NO                            YES

                                                                                        |                             |

                                                                                        v                             v

                                                                              +------------------+       +------------------+

                                                                              |   REJECT         |       |   PASS SECTION 1 |

                                                                              |   (Not STEM)     |       |   Continue to    |

                                                                              +------------------+       |   Section 2      |

                                                                                                         +------------------+

 

Section 2: Core Directives 
2.1 Objective  
Requirement: The prompt must be deterministic and lead to one unambiguous correct numeric outcome. State rounding rules, numerical precision, and units clearly. Maximum rounding: three significant decimals (e.g., 1.568, 0.006).

Check: Is there a single, indisputable correct numeric answer with precision and units specified?

 

2.2 Reproducible 
Requirement: The prompt must be reproducible, meaning all information necessary to uniquely determine the numeric output must be fully specified so that it produces the same correct result on every run when solved correctly without reliance on randomness, undefined behavior, or external state. Explicitly specify anything nonstandard or variant-heavy.

Check: Does the prompt avoid randomness, external data, or undefined behavior?

 

 2.3 Verifiable 
Requirement: The prompt must allow the solution to be checked objectively via explicit mathematical steps or executable code.

Check: Is there a clear, precise solution path that can be used to independently verify the correctness of the result?

 

2.4 Challenging 
Requirement: The prompt must require correct reasoning rather than guesswork, with complexity that can lead to valid reasoning errors.

Check: Does the problem require multi-step reasoning where errors can propagate?

 

 2.5 Computationally Intensive 
Requirement: Requires code to solve; involves at least 3–5 reasoning steps (e.g. setting up formulas, applying constraints, iterating over cases, checking thresholds). Should be too complex to solve by hand within a day.

Check: Does the task involve multi-step calculations, algorithmic reasoning, or iterative processes that cannot be reliably solved by intuition alone?

 

2.6 Decision Path
            START

                         (Passed Section 1)

                                |

                                v

              +------------------------------------+

              |        2.1 DETERMINISTIC           |

              |  Single correct numeric answer     |

              |  with precision & units specified? |

              +------------------------------------+

                                |

                 +--------------+--------------+

                 |                             |

                NO                            YES

                 |                             |

                 v                             v

        +------------------+       +------------------------------------+

        |      REWORK      |       |         2.2 REPRODUCIBLE         |

        | (add precision,  |       |  Avoids randomness, external data, |

        |  units, clarity) |       |  or undefined behavior?            |

        +------------------+       +------------------------------------+

                 |                             |

                 |              +--------------+--------------+

                 |              |                             |

                 |             NO                            YES

                 |              |                             |

                 |              v                             v

                 |     +------------------+       +------------------------------------+

                 |     |      REWORK      |       |          2.3 VERIFIABLE            |

                 |     | (remove external |       |  Clear solution path to verify?    |

                 |     |  dependencies)   |       +------------------------------------+

                 |     +------------------+                    |

                 |              |              +--------------+--------------+

                 |              |              |                             |

                 |              |             NO                            YES

                 |              |              |                             |

                 |              |              v                             v

                 |              |     +------------------+       +------------------------------------+

                 |              |     |      REWORK      |       |         2.4 CHALLENGING            |

                 |              |     | (ensure clear    |       |  Multi-step reasoning required?    |

                 |              |     |  solution path)  |       +------------------------------------+

                 |              |     +------------------+                    |

                 |              |              |              +--------------+--------------+

                 |              |              |              |                             |

                 |              |              |             NO                            YES

                 |              |              |              |                             |

                 |              |              |              v                             v

                 |              |              |     +------------------+       +------------------------------------+

                 |              |              |     |      REWORK      |       |    2.5 COMPUTATIONALLY INTENSIVE   |

                 |              |              |     | (add complexity) |       |  Code required (3-5+ steps)?       |

                 |              |              |     +------------------+       +------------------------------------+

                 |              |              |              |                             |

                 |              |              |              |              +--------------+--------------+

                 |              |              |              |              |                             |

                 |              |              |              |             NO                            YES

                 |              |              |              |              |                             |

                 |              |              |              |              v                             v

                 |              |              |              |     +------------------+       +------------------+

                 |              |              |              |     |      REWORK      |       |  PASS Section 2  |

                 |              |              |              |     | (increase        |       |  Ready to Create |

                 |              |              |              |     |  complexity)     |       |  Solution        |

                 |              |              |              |     +------------------+       +------------------+

                 |              |              |              |              |

                 v              v              v              v              v

        +--------------------------------------------------------------------------+

        |                    LOOP BACK TO START OF SECTION 2                       |

        +--------------------------------------------------------------------------+

 

2.7 Checklist 
Check	Action	Failure Impact
Prompt fits a STEM domain/subdomain	Select correct domain in UI dropdown	Rejection - wrong domain
Requires code to solve (not solvable by hand or lookup)	Ensure 3+ reasoning steps; apply hardening if needed	Too trivial - model solves easily
Deterministic: single correct numeric answer	Specify all constraints, precision, units	Ambiguous - multiple valid answers
At least 3 reasoning steps needed	Add complexity, dependencies, or constraints	Too simple - fails computational intensity
Rounding/precision (≤3 sig figs) and units stated	Include explicit format requirements in prompt	Non-reproducible results
Context is complete (no assumptions required)	Provide all necessary inputs, formulas, constraints	Incomplete - requires clarifying questions
Professional, original, and plausible	Create novel scenario; avoid textbooks/templates	Rejection - copied or contrived
Passes all UI autochecks	Review and fix any flagged issues	Blocked from submission
Hints provided if all responses fail	Add 3 escalating hints (Section 3)	Cannot proceed if 0/10 correct
 

Section 3: Task Files
Task files are supplementary data files that experts may upload to accompany their prompts. These files contain data (e.g., CSV datasets, matrices, configuration values) that the prompt references and the model must analyze or process to solve the problem.

Input files must contain realistic, relevant data necessary for completing the task. All data referenced in the prompt must be present and accessible. You may attach multiple files in a task, but all should be required and relevant to the task's completion.

Files may not contain existing or proprietary data, and should be uniquely generated for the purposes of your task.

For more on how to use input files and some handy tips, see the USING INPUT FILES article.

 

3.1 File Completeness and Relevance
Requirement: The uploaded files must contain all data referenced in the prompt. No external lookups or assumptions should be required to interpret the file contents.

Check: Can the file be used directly with the prompt to solve the problem without additional data sources?

 

3.2 File Content & Format
Requirement: Files must be in standard, machine-readable formats (e.g. CSV, TSV, JSON, PDF, TXT). Data must be well-structured with clear headers/labels where applicable. No proprietary or binary formats. Like prompts, files should NOT contain seed code or scripts.

Check: Is the file format standard and can it be parsed using allowed Python libraries (in-built + NumPy, pandas, SciPy, scikit-learn (sklearn), sympy)?

 

3.3 Determinism Preserved
Requirement: File contents must be static and deterministic. No references to external URLs, timestamps, or dynamic data. The same file must produce the same result every time.

Check: Does the file contain only fixed, reproducible data?

 

3.4 Size & Complexity Appropriateness
Requirement: File size should be reasonable (and preferably not exceed 50 MB combined). Data complexity should match the computational intensity requirement—large enough to require code, but not so large as to cause timeout issues.

Check: Is the file appropriately sized for the problem’s computational requirements?

 

3.5 Prompt-File Alignment
Requirement: The prompt must explicitly reference the file and describe what data it contains. Column names, data types, and structure mentioned in the prompt must exactly match the file.

Check: Does the prompt accurately describe the file’s structure and contents?

 

Common Pitfalls
Pitfall	Description	Fix
❌ Missing data	File referenced in prompt but data incomplete	Ensure all values mentioned in prompt exist in file
❌ Format mismatch	Prompt describes CSV but file is malformed	Validate file parses correctly with pandas/NumPy
❌ Ambiguous structure	Headers unclear or missing	Add clear column headers and use consistent delimiters
❌ Oversized files	File too large, causes timeout	Reduce dataset size while maintaining computational challenge
 

STEP 2 – Golden Solution Creation
Provide the correct solution consisting of Python code, final numeric answer, and human-readable explanation. This final answer will be compared to the model responses in the third step to determine whether your prompt is challenging enough to the model.

Section 1: Solution Requirements 
1.1 Correctness
Requirement: Code must solve the prompt exactly and produce the single correct answer.

Check: Does the code output match the expected answer?

 

1.2 Reproducibility
Requirement: Code must return the same answer every run. No randomness allowed.

Check: Does running the code multiple times produce identical results?

 

1.3 Efficiency
Requirement: Code must run in reasonable time (<20 minutes). No brute force approaches.

Check: Does the code complete execution in under 20 minutes?

 

1.4 Allowed Libraries
Requirement: Use only standard Python libraries: anything that ships with Python (e.g. math, statistics) + NumPy, pandas, SciPy, scikit-learn (sklearn), sympy. No network I/O. File I/O is allowed only to read the task’s uploaded input files. Do not read any other local files and do not write any files.

Check: Does the code use only allowed libraries with no external dependencies?

Full list of allowed libraries:

Python Standard Library

math

cmath

statistics

decimal

fractions

collections

itertools

functools

heapq

bisect

operator

re

string

dataclasses

typing

enum

random (only if explicitly seeded + deterministic consumption order)

Third-Party

NumPy

pandas

SciPy

Scikit-learn (sklearn)

SymPy

Important note: Floating-point results can drift due to precision and operation order, and some functions may vary slightly across implementations if the exact evaluation order isn’t fixed. When sensitivity matters, specify float64, the step/order of operations, and any rounding/tolerances. SymPy is permitted for symbolic derivations, but tasks must remain closed-form and verifiable: specify the symbolic objective and require a final numeric output (or an explicitly defined canonical symbolic form).

 

1.5 Format Compliance
Requirement: Output must match exactly what the prompt specifies (correct units, decimals, rounding). No more than 3 decimals in the final answer if a non-integer.

Check: Does the output format match the prompt requirements?

 

1.6 Code Clarity
Requirement: Code must be tidy, commented, and easy to follow.

Check: Is the code readable and well-documented?

 

1.7 Human-Readable Explanation
Requirement: A concise, step-by-step overview is required. Do not provide extensive details outlining every single step; an overview will suffice. The explanation must be ordered, mirror the code logic, end with the final numeric answer, and make sense to a non-coder. 

Check: Does the explanation match the code logic and output?

 

1.8 Final Answer Format
Requirement: Numerical output rounded to no more than 3 significant decimals. Must match Python code output. Numerical Value field is mandatory; Unit field required if mentioned in prompt.

Check: Does the final answer match the code output with correct units and rounding?

 

1.9 Checklist
Check	Action	Failure Impact
Written in Python with allowed libraries	Use only in-built + standard libs, e.g. NumPy, pandas, scikit-learn (sklearn), SciPy, sympy	Rejection - non-standard libraries
Code runs without errors	Test execution	Cannot validate solution
Runtime <20 minutes	Optimize if slow	Rejection - inefficient
Code is deterministic	No randomness, fixed seeds	Non-reproducible results
Output is single correct numeric answer	Verify against expected	Invalid solution
Format matches prompt (rounding/units)	Check ≤3 sig figs, correct units	Format mismatch rejection
Human-readable explanation covers key steps	State formulas, show critical intermediates, mirror code logic	Unclear solution
Code matches human-readable explanation	Ensure logic flow and results align between code and explanation	Inconsistent solution
Solution directly answers the prompt	Verify no made-up data, incorrect assumptions, or off-topic content	Invalid/irrelevant solution
 

Common Pitfalls
Pitfall	Description	Fix
❌ Non-deterministic code	Random seeds, floating-point instability	Set fixed seeds; use stable algorithms
❌ Non-standard libraries	Using libraries outside in-built + NumPy, pandas, scikit-learn (sklearn), SciPy, sympy	Replace with allowed libraries only
❌ External I/O	Network calls or writing files (reading uploaded input files is OK)	Remove all external dependencies
❌ Format mismatch	Answer formatted differently from prompt request	Match exact units, rounding, significant decimals
❌ Overly complex code	Excessively long or opaque; sacrificing clarity	Refactor; add comments; simplify logic
❌ Explanation mismatch	Human-readable doesn’t match code logic or output	Align explanation with code step-by-step
 

STEP 3 – Model response evaluation
The evaluation step determines if your prompt is appropriately challenging by ensuring it yields the desired rate of model failures (at least 3 failures out of 10) while remaining solvable.

Section 1: Evaluation Criteria
1.1 Final Numeric Answer
Requirement: The model’s final numeric output must exactly match the expected answer. An incorrect numeric answer is the non-negotiable definition of a valid model failure.

Check: Does the model’s final numeric answer match the expected answer?

 

1.2 Reasoning Validity
Requirement: Failures must be due to valid reasoning errors (e.g., wrong formula, ignored constraint, arithmetic slip), not due to prompt flaws (e.g., ambiguity, missing data) or transcript errors/model timeouts. If the answer is correct but reasoning is entirely wrong (a “lucky guess”), this is invalid and the prompt must be reworked.

Check: Is the failure due to model reasoning error (not prompt flaw or lucky guess)?

 

1.3 Failure Rate
Requirement: Generate 10 model responses. Between 3 and 9 responses must be incorrect to confirm the prompt is appropriately challenging yet solvable.

Check: Are 3-9 out of 10 responses incorrect?

 

1.4 Decision Path

 

                  START (Model Evaluation Complete)

                              |

                              v

+------------------------------------------------------------------+

|  How many model responses are INCORRECT?                         |

+------------------------------------------------------------------+

                              |

         +--------------------+--------------------+

         |                    |                    |

      0-2/10               3-9/10                10/10

    (Too Easy)         (✅ Valid Range)        (Too Hard)

         |                    |                    |

         v                    v                    v

+----------------+    +----------------+    +----------------+

| Apply 1-2      |    | ✅ PASS        |    | Check: Prompt  |

| hardening      |    | Appropriately  |    | issue or valid |

| techniques     |    | challenging    |    | difficulty?    |

+----------------+    +----------------+    +----------------+

         |                                         |

         v                                   +-----+-----+

+----------------+                          |           |

| Re-run 10      |                       Prompt      Valid

| model          |                       Issue    Difficulty

| responses      |                          |           |

+----------------+                          v           v

         |                           +----------+ +----------+

         v                           | Fix      | | Add      |

+----------------+                   | prompt   | | HINTS    |

| Still 0-2/10?  |                   | (STEP 1) | | Re-run   |

+----------------+                   +----------+ +----------+

         |

   +-----+-----+

   |           |

  YES          NO

   |           |

   v           v

+----------+ +----------+

| Add 1-2  | | ✅ PASS  |

| MORE     | +----------+

| techniques|

| Re-run   |

+----------+

   |

   v

(LOOP - but consider hints if still failing)


 

1.5 Valid vs Invalid Failure Reasons

 

✅ VALID	❌ INVALID
Incorrect numeric answer	Correct answer + wrong reasoning
Wrong formula or method	Prompt vague or missing data
Ignored constraint	Multiple interpretations possible
Arithmetic/unit error	Rounding beyond 3rd decimal
Conditional logic error	Formatting/parsing error
Error propagation 	Failure due to overstuffed/unclear prompt

 

Section 2: Difficulty Tuning (Hardening + Hints)
2.1 Hardening Prompts
When the model solves your prompt too easily (0-2 failures out of 10), apply hardening techniques to increase difficulty while maintaining determinism.

⚠️ Critical Rule: Longer prompts are not better. Add 1-2 techniques at a time and rerun your prompt. Hardening is not guaranteed to cause model failure. Fundamental difficulty lies in introducing domain-specific reasoning and nuances, rather than adding arbitrary hardening levers.

See the following articles on prompt hardening to take your prompt to the next level:

Making Prompts Harder, Faster

Domain-Specific Task Guidance & Model Breaking Approaches in STEM Tasks

CI STEM Task Creation Guide

CI STEM Q&A Prompt Hardening Techniques Playbook

 

2.2 Introducing Hints to Make Prompts “Easier”
What is a hint: A hint is a brief piece of escalating guidance intended to reinforce model learning by teaching the correct approach or reasoning path to a problem, without introducing new, crucial information or revealing the final answer.

When: When you generate a prompt (and solution) that the model cannot solve at all, you will need to create a hint.

How: Create 2–3 short, escalating hints (Hint 1 → Hint 2 → Hint 3).

Hint 1: conceptual orientation (“what to try”).

Hint 2: method choice / algorithm pattern.

Hint 3: checks, edge cases, or stability guidance.

Each hint consists of one or two sentences in an imperative or neutral tone.

 

2.2.1 Hint Trigger
Requirement: Hints should only be added when the prompt yields valid failures in all model response evaluations (e.g., 0/10 correct). The goal is to reinforce model learning by teaching the approach, 

Check: Did all model responses fail to produce the correct answer?

 

2.2.2 Solution vs Hint
Requirement: Hints must not contain new crucial information or data points necessary to solve the problem. They should only provide guidance on reasoning approach.

Check: Does the hint avoid introducing new inputs, data, or answer-revealing values?

 

2.2.3 Guidance vs Revealing 
Requirement: Hints should point to the right method, decomposition, or reasoning path; flag common pitfalls; remind about units, rounding, and constraints; or suggest stability/accuracy tactics.

Check: Does the hint teach the approach without revealing the solution?

 

2.2.4 Determinism Preserved
Requirement: Hints must not change requirements (precision, libraries, output format) or imply approximate target values.

Check: Do hints preserve all original problem constraints?

 

 Hint Do’s and Don’ts
✅ Do	❌ Don’t
Point to the right method or reasoning path	Introduce new required inputs
Flag common pitfalls	Give key missing data
Remind about units, rounding, constraints	Provide the final formula with numbers
Suggest stability/accuracy tactics	Reveal intermediate or final numeric values
Keep to 1-2 sentences per hint	Relax the problem’s rules
 

2.3 Decision Path
+------------------------------------------------------------------+

|  Count CORRECT model responses                                   |

+------------------------------------------------------------------+

                              |

         +--------------------+--------------------+

         |                                         |

       3-9                                        0-2

    (≥3 correct)                            (0-2 correct)

         |                                         |

         v                                         v

+------------------+                  +------------------------+

|  NO HINTS        |                  |  Were failures VALID?  |

|  NEEDED          |                  |  (model error, not     |

+------------------+                  |   prompt flaw)         |

                                      +------------------------+

                                                   |

                                      +------------+------------+

                                      |                         |

                                     YES                        NO

                                      |                         |

                                      v                         v

                            +------------------+      +------------------+

                            |  WRITE HINTS     |      |  FIX PROMPT      |

                            +------------------+      |  (STEP 1)        |

                                      |               +------------------+

                                      v

                            +------------------+

                            |  HINT 1:         |

                            |  Conceptual      |

                            |  (what to try)   |

                            +------------------+

                                      |

                                      v

                            +------------------+

                            |  HINT 2:         |

                            |  Method/Algorithm|

                            +------------------+

                                      |

                                      v

                            +------------------+

                            |  HINT 3:         |

                            |  Validation/     |

                            |  Edge cases      |

                            +------------------+

                                      |

                                      v

+------------------------------------------------------------------+

|  VALIDATE: Introduces new data or values?                        |

+------------------------------------------------------------------+

                              |

                 +------------+------------+

                 |                         |

                YES                        NO

                 |                         |

                 v                         v

        +------------------+    +---------------------------+

        |  REWORK HINT     |    |  Changes original         |

        +------------------+    |  constraints?             |

                 |              +---------------------------+

                 |                         |

                 |              +----------+----------+

                 |              |                     |

                 |             YES                    NO

                 |              |                     |

                 v              v                     v

        +---------------------------------------+  +------------------+

        |          LOOP BACK TO WRITE HINTS     |  |  ✅ SUBMIT HINTS |

        +---------------------------------------+  +------------------+

 

2.4 Checklist
Check	Action	Failure Impact
10 model responses generated	Generate via Model Answers tab	Cannot evaluate prompt difficulty
3-9 responses are incorrect	Count incorrect answers	0-2: Too easy → Harden prompt; 10: Too hard → Add hints or fix
All failures are valid (model error)	Verify each failure reason	Invalid failures don’t count; rework prompt
No lucky guesses exist	Check reasoning on correct answers	Correct answer + wrong reasoning → Rework prompt for larger output
Understood why each failed	Document failure reasons	Cannot improve prompt or verify validity
Re-ran if outside 3-9 range	Harden (if easy) or add hints (if hard)	Prompt won’t meet project requirements
 

Common Pitfalls
Pitfall	Description	Fix
❌ Invalid failure counting	Counting formatting mismatches or rounding errors as failures	Only count incorrect numeric answers as failures
❌ Prompt-caused failures	Accepting failures due to missing info or vague conditions	Fix prompt (STEP 1), then re-run evaluation
❌ Skipping rework	Forgetting to harden prompt if model solves too easily	Return to STEP 1; apply hardening techniques
 

Quick Reference
Task Flow Summary
Step	Goal	Pass Condition
Prompt Writing	Create STEM problem	Passes all requirements + Hints if needed
Golden Solution	Provide correct solution	Correct code + matching explanation + formatted answer
Model Evaluation	Test model responses	3-9/10 incorrect with valid failures
 

Prompt Requirements
Criterion	Check
Completeness	Self-contained without external lookups?
Uniqueness	Original, not copy-pasted?
Precision	Precision and numeric rules defined?
Language	Grammatically correct US English?
Formatting	Well-formatted, code-free, ≤7K characters?
Plausibility	Would a professional encounter this?
STEM Domain	Correct domain/subdomain?
 

Prompt Core Directives
Criterion	Check
Deterministic	Single answer with precision/units?
Reproducible	Avoids randomness/external data?
Verifiable	Clear solution path exists?
Challenging	Multi-step reasoning required?
Computationally Intensive	Code required (3-5+ steps)?
 

Model Evaluation
Check	Pass	Fail
Incorrect responses	3-9 out of 10	0-2 (too easy) or 10 (too hard)
Failure validity	Model reasoning error	Prompt flaw, rounding, or lucky guess
 

Model Failure Validity
Valid Failures	Invalid Failures
Wrong numeric answer	Correct answer + wrong reasoning
Wrong formula/method	Prompt vague or missing data
Ignored constraint	Multiple interpretations
Arithmetic/unit error	Rounding beyond 3rd sig fig if decimal
Conditional logic error	Formatting/parsing error
 

Golden Solution
Check	Requirement
Libraries	In-built + NumPy, pandas, SciPy, scikit-learn (sklearn), sympy only
Runtime	<20 minutes
Determinism	Same result every run
Output	Single correct numeric answer
Format	≤3 sig figs, correct units
Explanation	Matches code logic and output
 

Hardening Techniques
ID	Technique	Description
H-01	Template disruption	Add twist that invalidates standard approach
H-02	Hidden state	Track evolving variable across steps
H-03	Continuity/normalization	Piecewise problems requiring smooth joins
H-04	Numerical obligation	Root-finding, integration, no shortcuts
H-05	Scalability barrier	Scale so brute-force is infeasible
H-06	Verification by residual	Tie correctness to computed error metric
H-07	Contradictory constraints	Trade-off reasoning required
H-08	Near-limit regimes	Parameters near divergence thresholds
H-09	Nonlinearities	Nonlinear functions, not linear simplifications
H-10	Precision carry-through	Multi-stage with exact intermediate results
⚠️ Add 1-2 at a time. Longer prompts ≠ better.

 

Hints
Hint	Focus
Hint 1	Conceptual orientation (what to try)
Hint 2	Method/algorithm pattern
Hint 3	Validation/checks/edge cases
 

Self-Review Checklist for Experts
Check	Action	Failure Impact
Prompt is deterministic with unique numeric answer	Verify single correct answer exists	Ambiguous → Rejection
Prompt is self-contained	Confirm no missing inputs/assumptions	Incomplete → Rework required
Requires ≥3 reasoning steps and coding	Verify not trivial or solvable by hand	Too easy → Model solves; task invalid
Answer formatted correctly	Check whole number / rounding rules clear	Format mismatch → Rejection
Model responses fail for reasoning-based reasons	Confirm 3-9/10 wrong due to model error	Invalid failures → Rework prompt
Python code is reproducible	No randomness; same result every run	Non-reproducible → Rejection
Python uses only allowed libraries	In-built + NumPy, pandas, SciPy, scikit-learn (sklearn), sympy only	Non-standard libraries → Rejection
Python output matches human solution	Cross-verify code and explanation	Mismatch → Rejection
                                   

Decision Path 
                                   START

                                     |

                                     v

+========================================================================+

|                     STAGE 1: GENERATION                                |

|                  (Task Creation - Original Expert)                      |

+========================================================================+

                                     |

                                     v

                +====================================+

                |     STEP 1: PROMPT WRITING         |

                |  Create multi-step STEM problem    |

                |  Deterministic, professional       |

                +====================================+

                                     |

                                     v

                +====================================+

                |     STEP 2: GOLDEN SOLUTION        |

                |  Python code + Reasoning steps     |

                |  + Final numerical answer          |

                +====================================+

                                     |

                                     v

                +------------------------------------+

                |  Autochecks pass?                  |

                +------------------------------------+

                                     |

                      +--------------+--------------+

                      |                             |

                     NO                            YES

                      |                             |

                      v                             v

     +-----------------------------------+          |

     |  REWORK or OVERRIDE (if valid)    |          |

     +-----------------------------------+          |

                      |                             |

                      +----------->-----------------+

                                                    |

                                                    v

                +====================================+

                |     STEP 3: MODEL EVALUATION        |

                |  Run 10 model responses             |

                |  Target: 3–9 valid failures         |

                |  Justify why failures occurred      |

                +====================================+

                                     |

                                     v

+========================================================================+

|                        STAGE 2: QA                                     |

|                   (Quality Assurance)                                  |

+========================================================================+

                                     |

                                     v

                +------------------------------------+

                |  Reviews Generation task           |

                +------------------------------------+

                                     |

                                     v

                +------------------------------------+

                |  Evaluates against guidelines      |

                |  Runs mandatory AI autochecks      |

                +------------------------------------+

                                     |

                                     v

                +------------------------------------+

                |  All requirements met?             |

                +------------------------------------+

                                     |

                      +--------------+--------------+

                      |                             |

                     NO                            YES

                      |                             |

                      v                             v

        +----------------------------------+   +====================+

        |  RETURN FOR FIX (or REJECT if    |   |     COMPLETE       |

        |  final iteration)                |   +====================+

        +----------------------------------+            |

                      |                                 |

                      +--------------->------------------+

                                                    |

                                                    v

+========================================================================+

|                     STAGE 3: VERIFICATION                              |

|                  (Independent Second Expert)                           |

+========================================================================+

                                     |

                                     v

                +------------------------------------+

                |  Receives prompt only              |

                |  (no original solution visible)    |

                +------------------------------------+

                                     |

                                     v

                +------------------------------------+

                |  Creates independent solution:     |

                |  - Reasoning steps                 |

                |  - Python code                     |

                |  - Final answer + units            |

                +------------------------------------+

                                     |

                                     v

                +------------------------------------+

                |  Solution matches original?        |

                +------------------------------------+

                                     |

                      +--------------+--------------+

                      |                             |

                     NO                            YES

                      |                             |

                      v                             v

               +========================+           |

               | TASK GOES FOR FINAL QA |           |

               +========================+           |

                       |                            |

                       v                            |

                +-------------------------+         |

                |  All requirements met?  |         |

                +-------------------------+         |

                                     |              |

                      +--------------+--------------+

                      |                             |

                     NO                            YES

                      |                             |

                      v                             v

                +------------+           +====================+

                |  REJECTED  |           |     COMPLETE       |

                +------------+           +====================+


 

Task examples
Below are a few examples of prompts that have sufficiently challenged the models, while meeting all other quality criteria as well.

 

Non-explicit deterministic task
Example: First Steps to LAEP (Electrical Engineering/Math)
What is the total carbon output in the districts of York, Sheffield or Leeds for residential dwellings? Choose only one that is highest, and report the value per specification below.

The typical heat energy demand of the premises is 15000 kWh; however, in reality, it varies from 10 MWh to 20 MWh. Assume that 91% of dwellings are equipped with condensed gas boilers with an energy efficiency of 0.98. Assume 9% of dwellings are fully electrical, with electrical systems being 100% fuel efficient. Those that have over and including 14 MWh are gas connected. Those that have less than that amount are considered fully electric. Gas and electric dwellings are normally distributed in their own category, respectively. There are  85,459 residential dwellings in the area. The emission factor of gas is 0.184 kgCO₂/kWh. The emission factor of electricity is 0.274 kgCO₂/kWh. Note that the company that I work for might require the per-building emission information, so in order to get the total carbon output in tonnes, first calculate the output for individual dwellings and then sum them up to get the total value. For numerical integration across each group, use the trapezoidal method with 1000 steps and a tolerance of 1e-8. At each iteration, double the number of subintervals. The nearby town of Leeds has about 341,500 households. The distribution of dwellings is not the same, though with 11% of dwellings being fully electrical and 89% being gas. In Sheffield there are about 231,950 households and 77% are using main gas as heat the rest should be considered as fully electric.

Continue refining until the difference between two consecutive estimates is less than 1e-8, or until a maximum of 200 refinements has been reached. When assigning per-dwelling energy demand values, use probability midpoint sampling ($p_i = (i -0.5)/N$, where N is the Number of dwellings in the sample and i=1,....N). Make sure that the final answer, which is rounded to 2 decimal places, is one number.

 

Numeric Rules and Additional Information

Make all the calculations except for the presentation of the final answer using integer arithmetic, with appropriate scaling, the final answer must be IEEE-754 double precision compliant. Use the Taylor series of 18th order to approximate any transcendental function. Rules for integer calculations: all calculations are performed using scaled integer (fixed-point) arithmetic. Real values are represented as integers scaled by a constant factor; S = 2³². Arithmetic operations follow these rules. Addition and subtraction are exact; Multiplication is rescaled by S rounded once using round-to-nearest (half-up). Division is performed as scaled division and rounded once using round-to-nearest (half-up). The arctangent function is evaluated using a Taylor expansion at the fixed arguments 1/5 and 1/239, as required by the Machin identity for π. The value of π is computed using the exact formula π = 16arctan(1/5) - 4arctan(1/239). The natural logarithm is used only to compute ln(2), which is obtained from the identity ln((1 + y)/(1 - y)) with the uniquely determined value y = 1/3. The exponential function is evaluated via a Taylor expansion with range reduction based on ln(2). Square roots are computed by first applying an exact power-of-two range reduction so that the argument lies in the interval [0.5, 2), after which it is written in the form 1 + u; the Taylor expansion of √(1 + u) is then evaluated with u = a - 1, which guarantees convergence. The Gaussian probability density function uses the fixed normalisation constant 1/√(2π), which is derived from the computed values of π and the square-root function. Group intervals are 4 standard deviations in size, centred around the mean.

 

Numerical specification
Deterministic problem formulation

Single non-contradictory solution path

Explicit numerical methods

Trapezoidal integration mandated

Fixed initial subinterval count

Deterministic refinement scheme

Explicit tolerance threshold

Maximum refinement limit defined

Fixed integration bounds

Deterministic sampling rule

Final output format strictly defined
 

Arithmetic specification
Fixed-point arithmetic required

Explicit scaling factor defined

Exact addition and subtraction

Single-rounding multiplication

Single-rounding division

Half-up rounding rule specified

No floating-point shortcuts allowed

Transcendentals defined via summations

Taylor series order fixed

Deterministic range reduction

π computed from fixed identity

Gaussian normalisation derived
 

Realism and engineering alignment
Inputs are sufficient but not overstated

No redundant parameters required

Contextual values are non-binding

Distractor information tests discipline

Per-dwelling emissions reflect industry practice

Micro-to-macro calculation enforced

Aggregation occurs after calculation

Supports later spatial reassignment

Compatible with digital-twin workflows

Reproducible across platforms
 

Domain specification
Residential dwellings are explicitly defined

Gas and electric categories are separated

Category shares explicitly specified

Assignment thresholds are explicit

Efficiency assumptions are fixed

Emission factors are fixed

Separate demand distributions per category

Normal distributions explicitly bounded

District-level aggregation required

One district selected by the maximum value
 

Determinism despite apparent non-determinism
The problem statement appears open-ended

Multiple modelling paths seem possible

Apparent freedom is constrained by specification

Numerical methods remove ambiguity

Arithmetic rules eliminate implementation variance

Sampling scheme fixes randomness

Distribution bounds are explicitly defined

Category assignment rules are deterministic

Convergence criteria enforce uniqueness

No subjective calibration is allowed

Only one internally consistent pathway exists

Alternative interpretations lead to contradictions

 

Good examples 
Task 1: Financial Mathematics - Compound Interest with Tiered Fees
Prompt

12,000 dollars is invested with an annual interest rate of 10%, compounded daily for 3 years with a daily rate of 0.10/365 (assume 365 days a year). There is however, a standard fee that is deducted daily, 0.01% of the balance if it is less than 14,000 dollars, and 0.02% if it is greater than or equal to 14,000 dollars. Round all intermediate balances to 2 significant digits after each daily update in the iterative method. Calculate the final balance using:

iterative multiplication

continuous compound interest with effective rates.

Use double precision for all computations and round all intermediate balances to 2 decimal places after each daily update for both methods. If the difference between the two methods is more than 10 dollars, provide the iterative method’s result. Otherwise, provide their average. Give the final balance in dollars and round to 2 decimal places.

 Final Answer

14216.99 dollars

Why This is a Good Prompt

Domain: Mathematics - Mathematical Modeling

Complexity Characteristics:

1,095 daily iterations (3 years × 365 days) - massive iteration count

Piecewise fee structure with threshold at $14,000

Two computational methods required (iterative vs continuous)

Comparison logic (if difference > $10, use iterative; else average)

Precision requirements: Round intermediate balances to 2 decimals after EACH daily update

Hardening Elements Applied:

✅ Dependency Chain: 1,095 sequential steps where each day depends on previous balance

✅ Piecewise Logic: Fee rate changes at $14,000 threshold

✅ Mandatory Iteration: Daily compounding with explicit iteration requirement

✅ Precision Policy: Round after each step (precision cascade potential)

✅ Constraint Precedence: Interest applied first, then fee deducted

✅ Verification Hook: Compare two methods and apply decision rule

✅ Unit Specification: Dollars, 2 decimal places

Why Models Fail:

Wrong order of operations (fee before interest)

Incorrect threshold handling (< vs ≤)

Precision cascade errors from intermediate rounding

Incorrect continuous compounding formula

Wrong comparison logic implementation

 

Task 2: Computer Science - Raft Consensus Algorithm Simulation
Prompt

You are simulating a Raft consensus algorithm for 5 nodes (IDs 1-5). Each node has an election timeout uniformly random between 150 ms and 300 ms.

There is a dynamic partition in place, at time 0 Node 5 is isolated, at time 60ms node 3 is partition from node 1, at time 100ms node 4 is isolated from node 1 and node 5, at time 160ms node 2 cannot reach node 3 and node5 and at time 170ms the full network is restored.

At t=0, all nodes are followers. The first node to timeout becomes a candidate and requests votes. Each node can only vote once per term. A vote request is sent immediately after the timeout, and a vote response is sent immediately after the request. The delay in between for both the request and response is a random uniform distribution between 5ms and 15ms. All the clocks of each nodes skew differently, for node 1 it is 1.000, node 2’s skew is 1.005, node 3’s skew is 0.995, Node 4’s is 1.002, Node 5’s skew is 0.998

The effective timeout for each node is the timeout * clock skew

A majority of votes (3) is needed to become leader.

Use the Mersenne Twister algorithm and set seed to 42 for reproducibility.

Simulate timeouts and message passing, accounting for the partition and performing calculations rounded to 3 decimal places

Use a monotonically counter to account for scheduling conflicts, in the case of two events scheduled at the same time, they will still be processed in the order they were added

Determine the time (in ms) when the first leader is elected.

Output: Your code must output a decimal rounded to 3 decimal places: the election time.

Final Answer

173.473 ms

Why This is a Good Task

Domain: Computer Science - Distributed Systems

Complexity Characteristics:

5-node distributed system simulation

Dynamic network partitions at specific timestamps (0ms, 60ms, 100ms, 160ms, 170ms)

Clock skew for each node (different time rates: 1.000, 1.005, 0.995, 1.002, 0.998)

Random timeouts (150-300ms uniform distribution)

Random network delays (5-15ms uniform distribution)

Raft protocol rules: election timeouts, vote requests, term management

Event-driven simulation with precise timing

Hardening Elements Applied:

✅ Dependency Chain: Events cascade through time with state changes

✅ Piecewise Logic: Network topology changes at specific times

✅ Mandatory Iteration: Event loop simulation required

✅ Unit Conversions: Clock skew multipliers (effective timeout = timeout × skew)

✅ Constraint Precedence: Partition rules override communication

✅ Precision Policy: 3 decimal places, specific seed for reproducibility

✅ Algorithm Choice: Mersenne Twister required, monotonic counter for tie-breaking

Why Models Fail:

Incorrect partition topology handling

Wrong clock skew application

Incorrect event scheduling (simultaneous events)

Missing Raft protocol rules (one vote per term)

Wrong random seed or algorithm

Incorrect majority calculation with partitions

 

Task 3: Data Science - Electric Vehicle Fleet Battery Degradation Simulation
Prompt

A logistics company operates 1000 electric delivery vans. Each van’s battery degrades according to a nonlinear rate function of state-of-charge (SOC, denoted s in %) and ambient temperature T in °C:

$$r(s,T)= \begin{cases} 0.01\left(\dfrac{T}{25}\right){2}\left(\dfrac{s}{100}\right){0.5}, & \text{if } s<80,\[6pt] 0.01\left(\dfrac{T}{25}\right){2}\left(\dfrac{s}{100}\right){3}, & \text{if } s\ge 80. \end{cases}$$

Here r is the daily capacity-loss percentage, meaning r = 0.05 represents a loss of 0.05% of initial capacity for that day. Capacity loss is cumulative and irreversible.

Use an hourly time-step, applying r(s,T)/24 as the hourly degradation.

At every hour:

Compute r using the SOC at the start of the hour.

Apply degradation before SOC updates.

Vans must be processed strictly in ascending index order (0 → 999) every hour.

If SOC ≤ 0 before using it in r, clamp SOC to 0 for the degradation computation.

SOC is always clamped to the range [0,100].

Each day has 24 hourly steps in this exact order:

Day shift (06:00–14:00, 8 hours, temperature = 30 °C)

Each hour: Degrade using r(s,T) with T = 30. Then SOC decreases by exactly 5 percentage points. Clamp SOC ≥ 0.

Charging (14:00–22:00, 8 hours, temperature = 25 °C)

Determine balancing at the start of hour 14:00 only: Compute fleet average capacity as the arithmetic mean of all 1000 capacities using IEEE-754 doubles. If a van’s capacity < 0.95 × fleet average, it receives cooling during all 8 charging hours.

Each charging hour: Degrade first using r(s,Tc); if cooled, multiply r by exactly 0.5. Then increase SOC by 30 percentage points, but cap at 90% before computing degradation for the next hour.

Night shift (22:00–06:00, 8 hours, temperature = 20 °C)

Each hour: Degrade using r(s,Tn). Then SOC decreases by 5 percentage points.

Initial Conditions: Fleet size: 1000 vans. Initial SOC: 100%. Initial capacity: 100%. Simulation length: exactly 365 days.

Output: The fleet’s average capacity after 365 days, as a percentage, rounded to 2 decimal places. Use double precision for all computation.

Final Answer

97.62%

Why This is a Good Prompt

Domain: Data Science - Simulation & Modeling

Complexity Characteristics:

1000 vans × 365 days × 24 hours = 8,760,000 iterations

Piecewise degradation function with SOC threshold at 80%

Three daily operational regimes with different temperatures (30°C, 25°C, 20°C)

Fleet-level balancing decision based on statistical threshold (95% of mean capacity)

Conditional cooling logic affecting degradation rates

Strict processing order requirements

Hardening Elements Applied:

✅ Dependency Chain: SOC affects degradation rate, which affects capacity, which affects cooling eligibility

✅ Piecewise Logic: Degradation formula changes at SOC = 80% threshold

✅ Mandatory Iteration: 8.76 million hourly updates required

✅ Precision Policy: Double precision required, output rounded to 2 decimal places

✅ Constraint Precedence: Degradation applied before SOC updates; cooling determined once per day

✅ Processing Order: Vans must be processed in ascending index order

✅ Clamping Rules: SOC clamped to [0,100], charging capped at 90%

Why Models Fail:

Wrong order of operations (SOC update before degradation)

Incorrect piecewise threshold handling (< vs ≤)

Applying cooling decision at wrong time (each hour vs once per day)

Incorrect fleet average calculation timing

Missing SOC clamping at boundaries

Wrong temperature for each shift

 

Task 4: Mathematics - Bankruptcy Game Nucleolus (Cooperative Game Theory)
Prompt

A firm has gone bankrupt. There are 5 creditors, each with a legally verified claim.

The total estate available for distribution is: E = 100.

The claims are: c = (52, 49, 35, 34, 30)

Cooperative game formulation

This defines a bankruptcy game with player set N = {1,2,3,4,5}

For any coalition S ⊆ N, the characteristic function is:

$$v(S) = \max\left(0, E - \sum_{i \notin S} c_i \right)$$

Task

Compute the nucleolus of this TU-game.

Let x = (x₁,…,x₅) be the nucleolus allocation.

Output the value: x₂ + x₄

Output format

Output one real number, rounded to exactly 3 decimal places (banker’s rounding).

Final Answer

41.500

Why This is a Good Prompt

Domain: Mathematics - Game Theory / Operations Research

Complexity Characteristics:

5-player cooperative game with 2⁵-1 = 31 non-empty coalitions

Requires understanding of nucleolus concept (lexicographic minimization of excess vectors)

Connection to Aumann-Maschler (Talmud) rule for bankruptcy games

Involves Constrained Equal Awards (CEA) and Constrained Equal Losses (CEL) algorithms

Boundary case where 2E = Σcᵢ (estate equals half of total claims)

Hardening Elements Applied:

✅ Algorithm Choice: Must recognize nucleolus equals Talmud rule for bankruptcy games

✅ Piecewise Logic: Talmud rule branches based on whether E ≤ C/2 or E > C/2

✅ Boundary Case: E = 100 and C/2 = 100 creates exact boundary condition

✅ Multi-step Computation: CEA/CEL subroutines with water-filling algorithms

✅ Precision Policy: 3 decimal places with banker’s rounding

✅ Verification Hook: Sum of allocations must equal estate (efficiency constraint)

Why Models Fail:

Using generic LP-based nucleolus computation instead of recognizing Talmud rule shortcut

Incorrect handling of the boundary case (E = C/2)

Wrong implementation of CEA or CEL algorithms

Confusion between half-claims and full claims in Talmud rule

Numerical precision issues in lexicographic optimization

Incorrect coalition value calculations

 

Task 5: Physics - Transient Heat Conduction with Exothermic Cure
Prompt

Consider 1D transient heat conduction with exothermic cure in a 2-layer slab of total thickness 0.020 m.

Outer layer (0 ≤ x ≤ 0.006 m): density 1400 kg/m³, conductivity k₁(T) = 0.45(1 + 3.0×10⁻⁴(T - 293)) W/(m·K), specific heat c₁(T) = 950 + 0.25(T - 293) J/(kg·K).

Inner layer (0.006 < x ≤ 0.020 m): density 1600 kg/m³, conductivity k₂(T) = 0.28(1 + 2.5×10⁻⁴(T - 293)) W/(m·K), specific heat c₂(T) = 880 + 0.20(T - 293) J/(kg·K).

Initial conditions: T(x,0)=293 K, Y(x,0)=1.

Volumetric heat source in interior nodes j=1,…,19 only: q_vol = Q A e^(-12000/T) Y with Q=8.0×10⁶ J/m³, A=2.0×10⁵ s⁻¹.

Reactant update: Y_j^(n+1) = Y_j^n / (1 + A Δt e(-12000/T_j(n+1)))

Boundary at x=0: -k(T)∂ₓT|{x=0} = q’'(t{n+1}) - εσ((T₀ⁿ)⁴ - 3⁴) with q’'(t) = 65000 e^(-t/120) W/m², ε = 0.78, σ = 5.67×10⁻⁸ W/(m²·K⁴).

Boundary at x=0.020: -k(T)∂ₓT|_{x=0.020} = h(T - 295) with h=9 W/(m²·K).

Discretize into 21 nodes x_j = j·0.001 m, j=0,…,20. Nodes with x_j ≤ 0.006 use outer-layer formulas, otherwise inner-layer. Time step Δt = 0.5 s to t=300 s (600 steps). Use IEEE 754 double precision.

For interior nodes j=1,…,19 use backward Euler with harmonic means k_{j±1/2} = 2k_j k_{j±1}/(k_j + k_{j±1}).

At each time step, solve the resulting tridiagonal nonlinear system for T^(n+1) by Newton’s method, building the tridiagonal Jacobian by freezing k(T) and c(T) at the current iterate and including only the exact derivative of the source term; use the initial guess T_j^(0) = T_j^n and stop Newton when the max temperature update is below 10⁻¹⁰ K or after 30 iterations. Then update Y^(n+1).

After t=300 s, compute T_{in,max} = max_{0≤n≤600} T₂₀ⁿ and report only the numeric value of T_{in,max} in K to three decimals.

Final Answer

360.286 K

Why This is a Good Prompt

Domain: Physics - Heat Transfer / Thermal Sciences

Complexity Characteristics:

21 spatial nodes × 600 time steps = 12,600 system solves

Each time step requires Newton iteration (typically 5-10 iterations)

Coupled heat conduction with Arrhenius-type chemical reaction kinetics

Temperature-dependent material properties (k and c vary with T)

Mixed boundary conditions: radiation + convection + time-varying heat flux

Two-layer composite with different material properties

Hardening Elements Applied:

✅ Stitched Regions: Two-layer system with interface at x = 0.006 m

✅ Nonlinear Coupling: Temperature affects reaction rate, reaction releases heat

✅ Mandatory Iteration: Newton’s method required for implicit nonlinear system

✅ Precision Policy: IEEE 754 double precision, output to 3 decimals

✅ Harmonic Mean Averaging: Interface conductivities require harmonic means

✅ Boundary Complexity: Radiation (explicit), convection (implicit), decaying flux

✅ Jacobian Construction: Specific instructions for freezing properties vs exact source derivative

Why Models Fail:

Incorrect harmonic mean calculation at layer interface

Wrong handling of half control volumes at boundaries

Radiation term linearization errors

Incorrect Arrhenius source term derivative

Missing or wrong reactant update coupling

Wrong layer assignment for nodes at x = 0.006

Newton convergence issues from poor Jacobian approximation

 

Task 6: Computer Science - State-Dependent Queueing System Simulation
Prompt

A single-server system processes jobs arriving according to a deterministic but state-dependent arrival schedule over a fixed horizon of 10,000 jobs.

Arrival process:

Job 1 arrives at time t = 0

For job i ≥ 2, the inter-arrival time Δᵢ is defined as:

$$\Delta_i = \begin{cases} 0.8 + 0.002 \cdot \ln(1 + W_{i-1}) & \text{if } W_{i-1} < 5 \ 1.1+ 0.005 \cdot \sqrt{W_{i-1}} & \text{if } W_{i-1} \ge 5 \end{cases}$$

where W_{i-1} is the waiting time (not service time) experienced by job i−1. All computations must use float64 precision.

Service process:

The base service time for job i is: S_i = 0.9 + 0.1 · sin(0.01 · i)

Congestion penalty applies: If the queue length at service start is ≥ 7, then S_i ← S_i × 1.25

Queue discipline: FIFO, Single server, Server is never idle if jobs are waiting

Definitions:

Arrival time: A_i

Service start time: B_i = max(A_i, C_{i-1})

Completion time: C_i = B_i + S_i

Waiting time: W_i = B_i - A_i

Task:

Simulate the system for exactly 10,000 jobs

Compute the 99th percentile waiting time

Report the value rounded to exactly 3 decimal places

Final Answer

5.177

Why This is a Good Prompt

Domain: Computer Science - Queueing Theory / Discrete Event Simulation

Complexity Characteristics:

10,000 jobs with state-dependent inter-arrival times

Feedback loop: waiting time affects future arrivals

Congestion-dependent service times (queue length threshold)

Requires tracking queue length at each service start

Statistical output (99th percentile) requiring full simulation

Hardening Elements Applied:

✅ Dependency Chain: W_{i-1} → Δᵢ → Aᵢ → Bᵢ → Wᵢ creates cascading dependencies

✅ Piecewise Logic: Inter-arrival formula changes at W = 5 threshold

✅ Mandatory Iteration: 10,000 sequential job simulations required

✅ Queue Length Tracking: Must count incomplete jobs at each service start

✅ Precision Policy: float64 precision, 3 decimal place output

✅ Congestion Penalty: Service time multiplier when queue ≥ 7

✅ Statistical Aggregation: 99th percentile calculation over all waiting times

Why Models Fail:

Wrong queue length calculation (counting jobs incorrectly)

Incorrect threshold handling (< vs ≤ for W = 5)

Using service time instead of waiting time in arrival formula

Wrong order of operations (service start vs completion tracking)

Incorrect 99th percentile calculation method

Missing the sin function’s argument (0.01·i vs just i)

Applying congestion penalty at wrong time
 

Early Project Example 1
A cargo aircraft must complete a long-range journey from Jakarta (JKT) to Berlin (BER), stopping at a selection of intermediate international airports under strict operational and cost constraints. The aircraft has a maximum flight range of 5000 kilometers, a fuel tank capacity of 20,000 liters, and a fuel consumption rate of 4 liters per kilometer. For safety compliance, the aircraft is required to land at each airport with a minimum fuel reserve of 500 liters.

A list of 12 airports is provided, each with a specified fuel price in USD per liter and a binary indicator of whether refueling is permitted at that location. Additionally, a symmetric distance matrix details the pairwise flight distances between these airports, rounded to the nearest 100 kilometers. The aircraft must not revisit any airport, and refueling is only allowed at designated airports. Refueling may be partial or full and is assumed to be instantaneous. Before beginning any flight leg, the aircraft must have enough fuel to complete the leg and land with at least 500 liters remaining.

The objective is to determine the final total cost according to a valid route from JKT to BER, selecting a subset of intermediate stops that comply with all constraints and minimize the total cost of fuel purchased (in USD). The final total cost is rounded to two decimal places in USD.

 

Airport Information

* Jakarta (JKT), Indonesia: Fuel price is $1.10 per liter, refueling is allowed. Coordinates: (106.8456° E, 6.2088° S)

* Singapore (SIN), Singapore: Fuel price is $1.00 per liter, refueling is allowed. Coordinates: (103.8198° E, 1.3521° N)

* Bangkok (BKK), Thailand: Fuel price is $1.15 per liter, refueling is allowed. Coordinates: (100.5018° E, 13.7563° N)

* Delhi (DEL), India: Fuel price is $1.08 per liter, refueling is allowed. Coordinates: (77.1025° E, 28.7041° N)

* Dubai (DXB), UAE: Fuel price is $0.95 per liter, refueling is allowed. Coordinates: (55.2708° E, 25.2048° N)

* Istanbul (IST), Turkey: Fuel price is $1.02 per liter, refueling is allowed. Coordinates: (28.9784° E, 41.0082° N)

* Cairo (CAI), Egypt: Fuel price is $1.12 per liter, refueling is allowed. Coordinates: (31.2357° E, 30.0444° N)

* Athens (ATH), Greece: Fuel price is $1.18 per liter, refueling is allowed. Coordinates: (23.7275° E, 37.9838° N)

* Rome (ROM), Italy: Fuel price is $1.21 per liter, refueling is allowed. Coordinates: (12.4964° E, 41.9028° N)

* Frankfurt (FRA), Germany: Fuel price is $1.24 per liter, refueling is allowed. Coordinates: (8.6821° E, 50.1109° N)

* Munich (MUC), Germany: Fuel price is $1.26 per liter, refueling is allowed. Coordinates: (11.5820° E, 48.1351° N)

* Berlin (BER), Germany: Fuel price is $1.30 per liter, refueling not allowed. Coordinates: (13.4050° E, 52.5200° N)

 

Early Project Example 2
Consider an axisymmetric system of 30 lenses with air gaps between them. Treat the lenses as thin and solve in the paraxial approximation. Sequences of values along the optical path:

Air gaps (mm): 12, 8, 15, 6, 10, 18, 7, 14, 9, 20, 11, 5, 16, 13, 8, 19, 6, 15, 7, 12, 5, 17, 10, 9, 14, 6, 20, 11, 7.

Lens focal lengths (mm): f1, 80, -120, 60, -50, 150, -70, 90, -200, 110, -90, 75, -60, 130, -85, 55, -140, 95, -65, 180, -75, 100, -160, 70, -55, 125, -100, 200, -180, f30.

Find the focal lengths of the first and last lenses (f1, f30) that satisfy the following conditions:

1. The Petzval sum of the system is zero.

2. The effective focal length of the system is 100 mm.

3. The back focal distance (BFD) from the last lens is in the range from 60 mm to 70 mm.

If the first lens turned out to be diverging, find the new value ​​for the focal length of the 16th lens (f16) so that BFD of the system becomes 70 mm, or the same for the 10th lens (f10) if it is impossible for f16. After it calculate the new value of the Petzval sum as a final answer with 1/mm as units. Otherwise, give in the final answer the values ​​of f1 and f30.

Perform all calculations with a precision of 3 decimal places.
 

Bad Examples 
Bad Task 1: Computer Science - GPU Framegraph Scheduling with MT19937
Prompt

Use IEEE-754 double precision for every real-valued calculation unless a specific rounding, flooring, ceiling, or truncation rule is stated. At the very end, you will output one scalar, rounded to three decimal places using base-10 round-half-away-from-zero, with no extra text.

The only explicit analytic objects you must fully define are:

A Mersenne Twister (MT19937) pseudo-random generator with a fixed 64-bit seed of 2027.

The Box–Muller mapping from pairs of independent U(0,1) samples into independent standard normal samples.

Use MT19937 (seed = 2027) to produce a stream of independent uniforms U ∈ (0,1) in double precision. In strict order, take pairs (U₀,U₁), (U₂,U₃), … and for each pair apply the standard Box–Muller transform to obtain a pair of standard normal variables (Z₀,Z₁). Use the classical polar form (log, sqrt, cos, sin) exactly as given in any standard numerical analysis reference; do not substitute other Gaussian generators.

From the first 12 standard normal values Z₀,…,Z₁₁ obtained in that way, define the nominal execution time of pass Pₖ (k = 0,…,11) as follows:

Start with T_raw(k) = 1.2 + 0.18·|Zₖ| (in milliseconds).

Round T_raw(k) to four decimal place (still in milliseconds).

Truncate that rounded value toward zero to six decimal places in milliseconds.

Call the result T_nom(k). These 12 numbers are the only per-pass numerical inputs you need later.

Now consider a single framegraph instance with 12 passes P₀,…,P₁₁ and 8 logical resources R₀,…,R₇. The global submission order is:

P₀, P₁, P₂, P₃, P₄, P₅, P₆, P₇, P₈, P₉, P₁₀, P₁₁.

Queue assignments:

Graphics queue G: passes P₀, P₁, P₃, P₅, P₇, P₉, P₁₁.

Compute queue C: passes P₂, P₄, P₆, P₈, P₁₀.

Read/write access:

P₀ (G): writes R₀ and R₁.

P₁ (G): reads R₀; writes R₂.

P₂ ©: reads R₁; writes R₃.

P₃ (G): reads R₂ and R₃; writes R₄.

P₄ ©: reads R₄; writes R₅.

P₅ (G): reads R₃; writes R₆.

P₆ ©: reads R₅ and R₆; writes R₇.

P₇ (G): reads R₇; writes R₂ (overwriting).

P₈ ©: reads R₂ and R₄; writes R₁ (overwriting).

P₉ (G): reads R₁; writes R₀ (overwriting).

P₁₀ ©: reads R₀ and R₆; writes R₃ (overwriting).

P₁₁ (G): reads R₃ and R₇; writes R₅ (overwriting).

Resource aliasing policy:

Alias group A: {R₀, R₄, R₇} share one physical allocation.

Alias group B: {R₁, R₅} share one physical allocation.

Alias group C: {R₂, R₃, R₆} share one physical allocation.

Compute structural alias-safety score S_struct based on lifetime overlaps and dependency validation. Compute numerical scheduling score S_num by formulating and solving a precedence-constrained two-machine scheduling LP using a primal–dual interior-point method. Combine scores as M = (S_struct + S_num) / 2, apply specified rounding, multiply by 1000, and round to three decimal places.

Final Answer

Solution 1: 82.966

Solution 2: 498.057

Why This is a Bad Task

Domain: Computer Science - GPU Scheduling / Optimization

Critical Failure: Non-Deterministic Output

Two valid implementations produce completely different answers (82.966 vs 498.057), indicating the prompt is fundamentally ambiguous.

Problems Identified:

❌ Underspecified LP Formulation: “Use the textbook precedence-constrained scheduling LP” doesn’t specify which formulation. Different aliasing constraint implementations yield different optimal makespans.

❌ Ambiguous Aliasing Constraints: The two solutions handle aliasing non-overlap constraints completely differently, leading to divergent results.

❌ Precision Cascade: Multiple rounding steps (3 sig figs → 6 decimal truncation → 6 decimal rounding → 3 decimal rounding) amplify small interpretation differences.

❌ Over-Complexity: Combining PRNG, Box-Muller, graph analysis, LP solving, and multiple rounding rules creates too many failure points.

Lesson: Even detailed prompts can be ambiguous if they reference “standard” methods without specifying exactly which variant to use.

 

Bad Task 2: Mathematics - Simplicial Complex Homology on Hypercube
Prompt

A simplicial complex K is constructed from the 2-skeleton of a 4-dimensional hypercube: vertices are the 16 binary strings of length 4, edges connect strings differing in exactly one bit, and 2-simplices are triangles where all three pairwise Hamming distances equal 2. Compute the rank of the second homology group H₂(K; ℤ₂) over the field ℤ₂ by constructing the boundary matrices ∂₃: C₃→C₂ and ∂₂: C₂→C₁, where C₂ has dimension equal to the number of 2-simplices (triangular faces), C₁ counts edges (32 total from hypercube), and C₃ contains 3-simplices (tetrahedra with all six pairwise Hamming distances equal to 2). The rank is computed as rank(H₂) = dim(ker ∂₂) - dim(im ∂₃) where all matrix operations use arithmetic modulo 2, and ker ∂₂ is found via Gaussian elimination on the 32×m₂ boundary matrix (m₂ = number of triangles), while im ∂₃ is the column space of the m₂×m₃ matrix (m₃ = number of tetrahedra). Report rank(H₂(K; ℤ₂)) as an integer.

Final Answer

Solution 1: 0

Solution 2: 34

Why This is a Bad Task

Domain: Mathematics - Algebraic Topology

Critical Failure: Mathematically Inconsistent Definition

The QA reviewer noted: “The problem statement appears to be incorrect. None of the edges of any triangle lies in the complex’s edge list, which contradicts the definition of a simplicial complex.”

Problems Identified:

❌ Self-Contradictory Definition:

Edges defined as: Hamming distance = 1 (standard hypercube edges)

Triangles defined as: all pairwise Hamming distances = 2

But triangle edges have distance 2, which are NOT in the edge set!

This violates the fundamental requirement that all faces of a simplex must be in the complex.

❌ Two Incompatible Interpretations:

Interpretation A: Redefine edges to have distance 2 → answer is 0

Interpretation B: Keep hypercube edges, triangles “float” with zero boundary → answer is 34

❌ Model Failures Are Prompt Failures: Different answers arise from mathematical ambiguity, not reasoning errors.

❌ Passed All Automated Checks: Scored 100 on completeness, objectivity, precision—but contains a fundamental mathematical flaw.

Lesson: Domain expertise is essential. Automated checks cannot detect mathematical inconsistencies in definitions.

 

Bad Task 3: Machine Learning - Preconditioned Momentum Optimizer
Prompt

Let the map J : ℝ² → ℝ be

J(x,y) = (1 - x)² + 40(y - x²)² + x sin(y) - y cos(x).

For each integer t ≥ 0, let the state be wₜ = [xₜ,yₜ]ᵀ ∈ ℝ² with associated velocity vₜ = [vₜ⁽ˣ⁾,vₜ⁽ʸ⁾]ᵀ. Initialize w₀ = [-2.0,2.0]ᵀ and v₀ = [0.0,0.0]ᵀ.

For every t for which wₜ is defined, set gₜ = ∇J(wₜ) and let Hₓₓ(wₜ), Hᵧᵧ(wₜ) denote the exact second partial derivatives d²J/dx² and d²J/dy² at (xₜ,yₜ); no numerical or automatic differentiation may be used.

Define the diagonal preconditioner Dₜ = diag(dₓ,ₜ,dᵧ,ₜ) with dₓ,ₜ = 1/(√|Hₓₓ(wₜ)| + 10⁻³) and dᵧ,ₜ = 1/(√|Hᵧᵧ(wₜ)| + 10⁻³).

Fix γ = 0.9 and η_base = 10⁻³ and define the time-indexed step size ηₜ = η_base if t is even and ηₜ = η_base/2 if t is odd.

Given (wₜ,vₜ), obtain (wₜ₊₁,vₜ₊₁) by:

vₜ₊₁ = γvₜ - ηₜDₜgₜ

wₜ₊₁ = wₜ + vₜ₊₁

Perform a single forward sweep for t = 0,1,…,5000. For each t ∈ {0,…,5000}, define Gₜ = ‖gₜ‖₂ and Δₜ = |J(wₜ₊₁) - J(wₜ)|.

Let τ_grad = 10⁻⁴, τ_plateau = 10⁻⁶ and L = 20.

Define the gradient-candidate set C = {t ∈ {0,…,5000} : Gₜ < τ_grad}. If C = ∅, set t_final = 5000. Otherwise, let t_low = min C and define the plateau set P = {k ∈ {max(L,t_low),…,5000} : max_{s=k-L+1,…,k} Δₛ ≤ τ_plateau}. If P ≠ ∅, set t_final = min P; otherwise set t_final = 5000.

For each integer t with 0 ≤ t ≤ t_final, define rₜ = ‖wₜ‖₂ and vₙ,ₜ = ‖vₜ‖₂.

The trajectory functional is Ψ = Σₜ₌₀^{t_final} (rₜ + 0.01·J(wₜ) + 0.1·vₙ,ₜ).

Report only the numeric value of Ψ rounded to four decimal places.

Final Answer

Both solutions claim: 5843.2572

But: Solution 2 has python_matches_value: "no"

Why This is a Bad Task

Domain: Machine Learning - Numerical Optimization

Critical Failure: Solutions Don’t Actually Match

Despite both claiming 5843.2572, the implementations contain fundamental errors that should produce different results.

Problems Identified:

❌ Inconsistent Hessian Formulas:

Solution 1: H_yy = 80.0 - x * sin(y)

Solution 2: Hyy = 40 + x * sin(y)

Different coefficient (80 vs 40) and different sign!

❌ Missing Square Root in Preconditioner:

Prompt specifies: d = 1/(√|H| + 10⁻³)

Solution 2 implements: d = 1/(|H| + 10⁻³) (missing sqrt!)

❌ Squared vs Non-Squared Norms:

Prompt: rₜ = ‖wₜ‖₂ (L2 norm)

Solution 2: ||wₜ||² (squared norm in trajectory functional)

❌ Gradient Norm Definition:

Prompt: Gₜ = ‖gₜ‖₂

Solution 2: Gt = ||grad||² (squared)

❌ False Positive Verification: The task appears to pass because both claim the same answer, but the code implementations are mathematically different.

Lesson: Always verify that code actually produces the claimed answer. Check that formulas in code match the prompt exactly (sqrt, squared terms, signs, coefficients).

 

Project support
Discord Channels:

#stem-updates – a read-only channel where all major project updates are shared. Be sure to stay current with all updates provided here.

#stem-experts – channel for experts, QAs, and the project team to discuss all project-related questions and issues. Key project updates will be shared here as well.

#stem-qas – channel for QAs and the project team to discuss QA-related questions and issues. Key project updates will be shared here as well.

#stem-verifiers – channel for verifiers and the project team to discuss verification-specific issues. Key project updates will be shared here as well.

Technical Support:

Mindrift Support Chat function (dashboard, bottom-right).

Escalation:

Bugs → report via Support Chat first, then flag in Discord.

Usage:
- Keep this file as the canonical local reference.
- Update it when project guidance changes.

# Hofflebrockian Code Recompiler v0.1

A procedural demonstration of contract-led software reconstruction and source-withholding.

Status: superseded experimental design. Version 0.1 does not physically enforce source denial, uses the legacy implementation as the toy evaluator's oracle, and does not blind interpretive assessment. No natural-code evidence exists. Use this package only to rehearse the procedure.

## The shortest path

If you are not a coder, use an AI coding assistant that can open a folder and run terminal commands. The bundled toy is a walkthrough, not a validating trial. Do not begin with live or production software.

1. Open this package as a folder in your AI coding tool.
2. Read `MANUAL.md`, especially the risk gate and source-isolation rules.
3. Run the fast evidence pass with `prompts/00_FAST_PACKET.md` against `toy_trial/legacy` and `toy_trial/visible_tests`.
4. Save its outputs in copies of the files under `templates/`.
5. Ask the tool to run:

   `python toy_trial/tools/prepare_workspaces.py --packet templates/04_RECONSTRUCTION_PACKET.md`

6. Open `toy_trial/runs/control` in a fresh AI session and use `prompts/07_CONTROL_REFACTOR.md`.
7. Open `toy_trial/runs/blind` in a different fresh AI session and use `prompts/05_BUILDER.md`.
8. Return to the package root in a fresh session and use `prompts/06_AUDITOR.md`. The audit command is:

   `python toy_trial/auditor_only/evaluate_candidates.py`

The intended builder condition excludes `toy_trial/legacy`, `toy_trial/auditor_only`, repository history, and the other candidate. The bundled generator does not enforce that condition: it creates sibling directories under a shared parent. A fresh chat and an instruction not to navigate upward do not constitute physical denial.

## What is included

- `MANUAL.docx` and `MANUAL.md`: the full independent-use guide.
- `prompts/`: copy-ready role prompts for a fast pass, the six-role protocol, a conventional-refactor control, and final adjudication.
- `templates/`: trial manifest, protection register, diagnostic map, reconstruction packet, architect handoff, build record, audit report, and result summary.
- `toy_trial/`: a dependency-free Python module, visible tests, legacy-parity evaluator, and sibling-workspace generator.

## Non-negotiable limits

- Work on a disposable copy, branch, or clone with a verified rollback.
- Stop if the baseline does not pass before any rewrite.
- Do not use the first trial on authentication, authorization, payments, cryptography, safety systems, database migrations, concurrency, production infrastructure, regulated logic, or code with irreversible side effects.
- Do not deploy a candidate merely because visible tests pass.
- If the contract was incomplete, repair the contract, erase the failed blind candidate, and derive it again in a fresh builder context.

## Original hypothesis

Version 0.1 was intended to test whether a source-denied candidate could preserve behavior while reducing total complexity without moving that complexity into new dependencies, wrappers, configuration, or corrective patches. The current package cannot support that inference.

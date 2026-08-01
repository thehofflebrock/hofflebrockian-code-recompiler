# Hofflebrockian Code Recompiler v0.1

An independent trial kit for testing whether source-blind reconstruction can preserve software behavior while reducing total complexity.

Status: experimental application protocol. This is a testable hypothesis, not a proven replacement for refactoring.

## The shortest path

If you are not a coder, use an AI coding assistant that can open a folder and run terminal commands. Start with the bundled toy trial. Do not begin with live or production software.

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

The builder session must not have access to `toy_trial/legacy`, `toy_trial/auditor_only`, repository history, or the control candidate. A fresh chat is not sufficient if the old implementation remains in the workspace.

## What is included

- `MANUAL.docx` and `MANUAL.md`: the full independent-use guide.
- `prompts/`: copy-ready role prompts for a fast pass, the six-role protocol, a conventional-refactor control, and final adjudication.
- `templates/`: trial manifest, protection register, diagnostic map, reconstruction packet, architect handoff, build record, audit report, and result summary.
- `toy_trial/`: a dependency-free Python module, visible tests, sealed audit evaluator, and workspace-preparation tool.

## Non-negotiable limits

- Work on a disposable copy, branch, or clone with a verified rollback.
- Stop if the baseline does not pass before any rewrite.
- Do not use the first trial on authentication, authorization, payments, cryptography, safety systems, database migrations, concurrency, production infrastructure, regulated logic, or code with irreversible side effects.
- Do not deploy a candidate merely because visible tests pass.
- If the contract was incomplete, repair the contract, erase the failed blind candidate, and derive it again in a fresh builder context.

## Primary hypothesis

The trial supports the method only if the blind candidate preserves behavior on evidence withheld from the builder while reducing total complexity without moving that complexity into new dependencies, wrappers, configuration, or corrective patches.

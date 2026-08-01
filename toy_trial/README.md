# Toy Demonstration: Order Quote

This disposable Python module gives the procedure a bounded rehearsal target before anyone touches a real repository. It has no third-party dependencies and no external side effects.

> **This is not an evidentiary trial.** The module and its deliberate sediment were authored with the hypothesis. The evaluator uses the legacy implementation as its behavioral oracle, and the workspace generator does not enforce physical source denial. A successful run shows only that the package mechanics operate.

## Contents

- `legacy/order_quote.py`: inherited implementation visible to evidence roles and the control Builder.
- `visible_tests/`: cases both builders may use.
- `builder_stub/order_quote.py`: blank public seam for the blind Builder.
- `auditor_only/evaluate_candidates.py`: legacy-parity, boundary, complexity, and timing evaluator. Do not place this in either builder workspace.
- `tools/prepare_workspaces.py`: creates matched sibling workspaces from a packet for procedural rehearsal.

## Baseline command

From the package root:

`ORDER_QUOTE_MODULE_PATH=toy_trial/legacy/order_quote.py python -m unittest discover -s toy_trial/visible_tests -v`

On a system that does not accept the inline environment variable, set `ORDER_QUOTE_MODULE_PATH` to the absolute path of `legacy/order_quote.py`, then run the remainder of the command.

## Prepare candidates

After producing the Reconstruction Packet and Architect Handoff:

`python toy_trial/tools/prepare_workspaces.py --packet templates/04_RECONSTRUCTION_PACKET.md --handoff templates/05_ARCHITECT_HANDOFF.md`

The tool refuses to overwrite an existing `toy_trial/runs` directory. Move or archive an old run before creating a new one.

Open `runs/control` and `runs/blind` as separate workspace roots in separate AI sessions. This is instructional separation only: both directories share a readable parent, so the arrangement cannot substantiate a claim that the builder was denied the source.

## Audit command

After both candidates are sealed:

`python toy_trial/auditor_only/evaluate_candidates.py`

The evaluator compares both candidates to legacy behavior over fixed boundaries and seeded randomized cases, runs visible tests, reports source and branch metrics, inventories imports, and measures rough execution time. Its output is legacy parity, not independent contract conformance.

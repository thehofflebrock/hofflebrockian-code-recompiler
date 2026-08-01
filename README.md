# Hofflebrockian Code Recompiler

[![Package checks](https://github.com/thehofflebrock/hofflebrockian-code-recompiler/actions/workflows/tests.yml/badge.svg)](https://github.com/thehofflebrock/hofflebrockian-code-recompiler/actions/workflows/tests.yml)

A procedural demonstration of contract-led software reconstruction and source-withholding.

> **Status: superseded experimental design.** Version 0.1 does not support a reportable claim about source-blind reconstruction. No natural-code trial has yet produced evidence for or against the hypothesis. The repository remains public so the original design, its useful components, and its defects can be inspected.

## Why v0.1 was superseded

- The bundled workspace tool creates sibling directories. It does not physically deny an agent access to the legacy source or repository history. A run using it cannot substantiate a source-denial claim.
- The toy evaluator derives expected behavior from the legacy implementation. It measures legacy parity, not independent contract correctness, and can score sediment as behavior to preserve.
- The Auditor sees which candidate is which before assigning interpretive scores. The assessment is not blinded.
- Both builders receive the reconstruction packet and differ chiefly in access to the legacy source. The design therefore concerns implementation anchoring inside contract-led reconstruction, not reconstruction versus conventional refactoring.
- The toy module and its deliberate sediment were authored with the hypothesis. The toy proves that the package mechanics run; it is not evidence that the method improves natural code.

The passing badge means only that the package checks complete. It is not a validation badge.

## What remains useful

The durable core is the discipline of characterizing before erasing, typing consequential claims as observed, documented, inferred, implementation-only, unexplained, or unknown, and refusing to patch around a contract gap. When the governing contract changes, correct it upstream and rebuild from blank state.

`characterize -> protect -> compress -> isolate -> rederive -> falsify -> promote, recompile, reject, or retain`

## Start here

Use the bundled toy only to rehearse the procedure. Do not treat its output as experimental evidence, and do not begin with live or production software.

1. Read [`START_HERE.md`](START_HERE.md), then the risk gate and source-isolation rules in [`MANUAL.md`](MANUAL.md).
2. Use `prompts/00_FAST_PACKET.md` against the toy legacy module and visible tests.
3. Put the resulting records into copies of the files in `templates/`.
4. Generate the paired sibling workspaces used by the demonstration.
5. Run the two reconstruction conditions in separate fresh sessions.
6. Return to an auditor session and compare both candidates against sealed evidence.

The complete command-by-command route is in [`START_HERE.md`](START_HERE.md).

## Original research question

Version 0.1 was built to ask whether a source-denied candidate could:

1. preserve required behavior on evidence withheld from its builder;
2. introduce no security, performance, compatibility, side-effect, or operational regression; and
3. reduce total complexity or corrective burden relative to both the legacy implementation and a conventional-refactor control.

Moving complexity into dependencies, wrappers, configuration, or corrective patches does not count as simplification.

The current package does not answer that question. Its isolation, oracle, and assessment design are insufficient for a reportable comparison.

## Repository contents

- `MANUAL.md`: the original protocol, its operating details, and the supersession notice.
- `prompts/`: the fast packet, six role prompts, conventional-refactor control, and trial adjudicator.
- `templates/`: eight handoff and evidence records.
- `toy_trial/`: a dependency-free Python procedural example, 11 visible tests, a legacy-parity evaluator, and a sibling-workspace generator.
- `START_HERE.md`: the shortest independent route through the kit.

The [`v0.1 release`](https://github.com/thehofflebrock/hofflebrockian-code-recompiler/releases/tag/v0.1) preserves the original formatted manual and downloadable kit as superseded artifacts.

## Do not use an initial trial on

- authentication, authorization, identity, secrets, or permission checks;
- payments, financial calculations, cryptography, licensing, or regulated logic;
- database migrations, destructive jobs, irreversible side effects, concurrency, or production infrastructure;
- safety-critical, medical, legal, industrial, or emergency systems;
- code whose baseline already fails or that cannot be restored immediately.

## Licensing

The Python and automation code is available under the [MIT License](LICENSE-CODE). The manual, prompts, templates, and other written material are available under [Creative Commons Attribution 4.0 International](LICENSE-CONTENT.md). See [`LICENSE.md`](LICENSE.md) for the exact file boundaries and attribution form.

Copyright (c) 2026 J. Nicholas.

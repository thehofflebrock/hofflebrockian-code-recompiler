# Hofflebrockian Code Recompiler

[![Toy baseline](https://github.com/thehofflebrock/hofflebrockian-code-recompiler/actions/workflows/tests.yml/badge.svg)](https://github.com/thehofflebrock/hofflebrockian-code-recompiler/actions/workflows/tests.yml)

An independent trial kit for testing whether source-blind reconstruction can preserve software behavior while reducing total complexity.

> **Status:** Experimental application protocol. This is a falsifiable hypothesis, not a proven replacement for refactoring and not permission to deploy unreviewed code.

The method does not ask an AI to delete code, guess what belonged there, and patch until visible tests pass. It first characterizes and protects observable behavior, withholds the inherited implementation from the builder, rebuilds from an implementation-neutral contract, and audits the result against evidence the builder never saw.

`characterize -> protect -> compress -> isolate -> rederive -> falsify -> promote, recompile, reject, or retain`

## Start here

If you are not a coder, use an AI coding assistant that can open a folder and run terminal commands. Begin with the bundled toy trial. Do not begin with live or production software.

1. Read [`START_HERE.md`](START_HERE.md), then the risk gate and source-isolation rules in [`MANUAL.md`](MANUAL.md).
2. Use `prompts/00_FAST_PACKET.md` against the toy legacy module and visible tests.
3. Put the resulting records into copies of the files in `templates/`.
4. Generate structurally separate control and blind workspaces.
5. Run the conventional refactor and source-blind rebuild in separate fresh sessions.
6. Return to an auditor session and compare both candidates against sealed evidence.

The complete command-by-command route is in [`START_HERE.md`](START_HERE.md).

## Primary hypothesis

The trial supports the method only when the blind candidate:

1. preserves required behavior on evidence withheld from its builder;
2. introduces no security, performance, compatibility, side-effect, or operational regression; and
3. reduces total complexity or corrective burden relative to both the legacy implementation and a conventional-refactor control.

Moving complexity into dependencies, wrappers, configuration, or corrective patches does not count as simplification.

## Repository contents

- `MANUAL.md`: the full independent-use protocol and A/B experiment design.
- `prompts/`: the fast packet, six role prompts, conventional-refactor control, and trial adjudicator.
- `templates/`: eight handoff and evidence records.
- `toy_trial/`: a dependency-free Python example, 11 visible tests, a sealed evaluator, and workspace-isolation tooling.
- `START_HERE.md`: the shortest independent route through the kit.

The [`v0.1 release`](https://github.com/thehofflebrock/hofflebrockian-code-recompiler/releases/tag/v0.1) includes the formatted DOCX manual and a complete downloadable trial kit.

## Do not use an initial trial on

- authentication, authorization, identity, secrets, or permission checks;
- payments, financial calculations, cryptography, licensing, or regulated logic;
- database migrations, destructive jobs, irreversible side effects, concurrency, or production infrastructure;
- safety-critical, medical, legal, industrial, or emergency systems;
- code whose baseline already fails or that cannot be restored immediately.

## Licensing

The Python and automation code is available under the [MIT License](LICENSE-CODE). The manual, prompts, templates, and other written material are available under [Creative Commons Attribution 4.0 International](LICENSE-CONTENT.md). See [`LICENSE.md`](LICENSE.md) for the exact file boundaries and attribution form.

Copyright (c) 2026 J. Nicholas.

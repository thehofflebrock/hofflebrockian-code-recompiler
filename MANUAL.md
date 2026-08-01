---
title: "Hofflebrockian Code Recompiler v0.1"
subtitle: "Superseded Procedural Demonstration"
author: "J. Nicholas"
date: "1 August 2026"
---

# Read this first

The Hofflebrockian Code Recompiler v0.1 was built to test a narrow proposition: an inherited implementation can be withheld from a builder after its required behavior has been characterized and compressed, allowing the software to be rederived from local requirements rather than edited around accumulated compromises.

> **Status: superseded experimental design.** Version 0.1 does not support a reportable claim about source-blind reconstruction. No natural-code trial has yet produced evidence for or against the hypothesis. This manual is retained as a procedural demonstration and design record, not as a validated experiment or permission to replace production code.

The decisive defects are:

- The bundled tool creates sibling workspaces but does not physically deny an agent access to the legacy source or history.
- The toy evaluator derives expected outputs from the legacy implementation, so it measures legacy parity rather than independent contract correctness.
- The Auditor sees candidate identity before assigning interpretive scores.
- Both builders receive the reconstruction packet. The comparison varies legacy-source access inside contract-led reconstruction; it does not compare reconstruction with conventional refactoring.
- The toy code and its deliberate sediment were authored with the hypothesis. The toy demonstrates package mechanics only.

Treat every later claim of blindness, validation, or experimental support in this v0.1 record as superseded by this notice.

The method is not `delete -> guess -> patch until tests pass`. Its governed cycle is:

`characterize -> protect -> compress -> isolate -> rederive -> falsify -> promote, recompile, reject, or retain`

The package lets another person run that cycle without J. Nicholas present. It contains copy-ready prompts, handoff records, an A/B protocol, a scoring rule, and a disposable toy codebase.

## The original claim, not established by v0.1

The primary hypothesis is:

> A source-blind candidate can preserve required behavior on evidence withheld from its builder while reducing total complexity more effectively than a conventional refactor given the same contract, tools, model, tests, and work budget.

The null hypothesis is that source-blind reconstruction performs no better, performs worse, or only appears simpler because it loses behavior or moves complexity elsewhere.

The original decision rule proposed support for one trial only when all three conditions held:

1. The blind candidate achieves semantic parity on the sealed audit set and repository integration checks.
2. It introduces no new security, performance, compatibility, side-effect, or operational regression.
3. It reduces total complexity or corrective burden relative to both the legacy implementation and the conventional-refactor control.

One success does not establish generality. One failure must be routed before interpretation: the missing fact may belong to the contract, architecture, implementation, test instrument, or the legacy system itself.

Because the v0.1 isolation, oracle, and assessment instruments are invalid for that inference, satisfying this rule does not establish support.

## What the method does not claim

- Erasure is not intelligence and does not solve requirement drift, bad objectives, changing dependencies, security, task selection, or incomplete evidence.
- Old-looking code is not presumed accidental. Strange branches, odd constants, duplicated logic, and edge handling are treated as historical residue until tested.
- Passing visible tests is not behavioral proof.
- Cleaner syntax is not lower total complexity if the candidate adds dependencies, wrappers, configuration, network calls, hidden state, or new operational burden.
- A blind rebuild is not always the right operation. Retention, ordinary refactoring, architectural repair, or deletion may be the correct result.

# Before any trial

## Minimum setup

You need:

- a disposable copy, branch, or clone of the code;
- a bounded target with a stable public seam;
- a command that proves the current baseline;
- a way to run the same tests against two candidates;
- at least two isolated builder sessions or workspaces;
- an auditor that can see evidence the builders cannot;
- authority from the code owner to inspect and modify the chosen copy.

If you are not a coder, an AI coding assistant may operate the tools, but it does not assume deployment authority. Start with the toy trial. For someone else's repository or any live system, involve the responsible developer before choosing the target and before promoting a result.

## Risk gate

Do not use an initial trial on:

- authentication, authorization, identity, secrets, or permission checks;
- payments, financial calculations, cryptography, licensing, or regulated logic;
- database migrations, storage formats, destructive jobs, or irreversible side effects;
- concurrency, distributed coordination, queues, caches, or production infrastructure;
- safety-critical, medical, legal, industrial, or emergency systems;
- generated code, vendored code, framework internals, or code the team does not own;
- a module whose baseline already fails;
- a target without a verified rollback.

A strong first target is deterministic, local, side-effect-light, covered by tests, small enough to specify, and separated from the rest of the system by a visible interface.

## Target selection test

Proceed only when every required answer is yes.

| Question | Required answer |
|---|---|
| Does the current baseline pass? | Yes |
| Can the target be replaced without rewriting unrelated modules? | Yes |
| Are inputs, outputs, errors, and side effects observable? | Yes |
| Can both candidates be tested under the same conditions? | Yes |
| Can the original be restored immediately? | Yes |
| Can the builder be physically denied the legacy source and audit set? | Yes |
| Is failure low-consequence inside the trial environment? | Yes |

If any answer is no, retain the target and choose another seam. Better documentation is useful, but it does not make an invalid experiment valid.

# Structural source blindness

A fresh conversation does not create source blindness when the model can still open the original file, repository history, hidden tests, or another candidate. Isolation must be structural.

**The bundled v0.1 tooling does not meet this requirement.** It creates sibling directories under one package root and relies on an instruction not to navigate upward. Use it only to rehearse the procedure. Do not report a run made with it as physically source-denied.

| Role | Legacy | History | Visible tests | Audit | Packet | Candidate |
|---|---:|---:|---:|---:|---:|---:|
| Custodian | Yes | Yes | Yes | Seals | No | No |
| Diagnostician | Yes | If needed | Yes | No | No | No |
| Translator | No | No | Evidence | No | Creates | No |
| Architect | No | No | Interface | No | Yes | No |
| Blind Builder | No | No | Yes | No | Yes | Blind output |
| Control Builder | Yes | Optional | Yes | No | Yes | Control output |
| Auditor | Yes | Yes | Yes | Yes | Yes | Both |

For the rigorous protocol, run one role per fresh session. The fast packet prompt combines the first four roles for convenience, but weakens independence and must be labeled `FAST` in the result.

# The six-role protocol

## 1. Custodian

The Custodian protects the experiment before anyone improves the code.

Required output:

- trial manifest and authority boundary;
- exact target and excluded scope;
- baseline command and result;
- protection register;
- snapshot or tombstone location;
- sealed audit material or a plan for creating it;
- builder-denial list;
- stop conditions.

**Custodian gate:** Pass only when the baseline is green, rollback is verified, the seam is bounded, risk is acceptable, and the audit set can be withheld. Otherwise stop.

## 2. Diagnostician

The Diagnostician maps behavior beneath implementation. It may inspect the old code, tests, callers, logs, documentation, and integration points. It does not rewrite.

Every claim is typed as one of:

- observed behavior;
- documented requirement;
- inferred intent;
- implementation fact;
- unexplained residue;
- unknown or conflict.

Odd behavior remains visible. “This looks stupid” is not a deletion warrant.

**Diagnostic gate:** Pass only when inputs, outputs, state transitions, errors, side effects, dependencies, compatibility surfaces, and meaningful anomalies are mapped well enough for another role to write an implementation-neutral contract.

## 3. Translator

The Translator receives the evidence records, not the legacy implementation. It creates the shortest packet capable of reconstructing required behavior without leaking the old algorithm.

The reconstruction packet includes:

- interface and accepted inputs;
- outputs and invariants;
- state transitions and error semantics;
- side effects and ordering requirements;
- determinism, concurrency, security, and performance constraints;
- compatibility promises;
- examples and counterexamples;
- forbidden outcomes;
- unknowns and conflicts;
- visible tests and success command;
- escalation rules for contract gaps.

It excludes old control flow, private helper names, line-by-line descriptions, algorithmic hints, and style judgments unless one is itself a compatibility requirement.

**Translation gate:** Pass only when every protected behavior is represented or explicitly marked unknown, and the packet does not prescribe the inherited implementation.

## 4. Architect

The Architect defines the replacement seam and builder environment. It sees the packet and surrounding interfaces, not the legacy source.

Required output:

- target file or module boundary;
- allowed and forbidden dependencies;
- interface stubs and integration adapters;
- complexity budget;
- visible test command;
- clean-workspace contents;
- promotion and rollback route.

**Architecture gate:** Pass only when the builder can work without inventing an upstream decision or reaching back into forbidden sources.

## 5. Builder

The Builder sees only the reconstruction packet, architectural handoff, interface context, approved dependencies, and visible tests. It must not inspect the legacy implementation, git history, sealed tests, auditor tools, or control candidate.

The Builder may implement, run visible tests, and record uncertainties. It must emit `CONTRACT BLOCK` rather than guess when required behavior is absent or contradictory.

**Builder gate:** Pass only when the candidate compiles or loads, visible tests pass, the allowed dependency boundary holds, and every deviation or unresolved ambiguity is recorded.

## 6. Auditor

The Auditor sees everything the Builder could not. It compares the legacy system, control candidate, blind candidate, packet, hidden corpus, repository integration, benchmarks, security checks, and total complexity.

Every failure is routed to the smallest responsible layer:

| Failure class | Required response |
|---|---|
| Contract gap | Repair the packet, erase the blind candidate, rebuild in a fresh context |
| Architecture gap | Repair the seam or dependency rules, then rebuild |
| Implementation defect | Reject or rebuild the candidate; do not rewrite the contract to excuse it |
| Test defect | Repair the instrument and rerun all candidates |
| Legacy defect | Record separately; do not silently canonize or silently fix it |
| Unknown conflict | Hold promotion until an authority or new observation resolves it |

**Audit gate:** The Auditor returns exactly one decision: `PROMOTE BLIND`, `PROMOTE CONTROL`, `RECOMPILE`, `RETAIN LEGACY`, or `REJECT TRIAL`.

# Run the bundled toy trial

The toy trial is a dependency-free Python order-shipping calculator with deliberately sedimented control flow. The visible tests cover ordinary behavior. The auditor holds boundary cases and deterministic differential fuzzing outside the builder workspaces.

## Fast path

1. Open the package root in an AI coding assistant.
2. Paste `prompts/00_FAST_PACKET.md` and identify `toy_trial/legacy/order_quote.py` as the target.
3. Tell it to use `toy_trial/visible_tests` as visible evidence and to write its outputs into copies of the files in `templates/`.
4. Review the packet. Any unresolved `UNKNOWN` must remain visible.
5. Ask it to run:

   `python toy_trial/tools/prepare_workspaces.py --packet templates/04_RECONSTRUCTION_PACKET.md`

6. Open `toy_trial/runs/control` as a new workspace. Paste `prompts/07_CONTROL_REFACTOR.md`.
7. Open `toy_trial/runs/blind` as a different new workspace. Paste `prompts/05_BUILDER.md`.
8. Close both builder sessions. From the package root, paste `prompts/06_AUDITOR.md` in a new session and run:

   `python toy_trial/auditor_only/evaluate_candidates.py`

9. Complete `templates/07_AUDIT_REPORT.md` and `templates/08_RESULT_SUMMARY.md`.

The fast path rehearses the intended source-withholding mechanism. It neither enforces physical denial nor supplies the same role independence as six fresh evidence sessions, and it cannot produce evidence for the hypothesis.

## Rigorous path

Use prompts 01 through 04 in separate sessions before preparing the two builder workspaces. Each role receives only the previous role's permitted handoff. Do not let the Translator or Architect reopen the legacy source. Then run the control, blind builder, and auditor as above.

# Historical natural-code protocol

The following section records the original design. Do not use v0.1 to publish a source-denied comparison. A future protocol must first correct physical isolation, separate legacy parity from independently authoritative conformance, and blind interpretive assessment.

1. Precommit the target, time or turn budget, model/tool version, allowed dependencies, visible test set, sealed audit set, metrics, and stop conditions.
2. Run the existing baseline and save the exact result before any modification.
3. Create two clean branches or copies from the same baseline.
4. Produce and seal the reconstruction packet before either builder starts.
5. Give both builders the same packet, interface context, visible tests, tools, and work budget. Give only the control builder the legacy implementation.
6. Prevent both builders from seeing the audit corpus or one another's output.
7. Seal both candidates before the Auditor runs hidden, differential, property, fuzz, benchmark, security, and integration checks appropriate to the possible failure.
8. Count complexity across the whole replacement, including new dependencies and operational configuration.
9. Route failures before allowing correction.
10. Promote only through the code owner's normal review and deployment process. This protocol never replaces repository policy, human review, staging, canarying, or rollback.

# A/B comparison protocol

The only intended experimental difference is access to the inherited implementation.

| Controlled factor | Rule |
|---|---|
| Starting point | Same clean baseline |
| Contract | Same sealed reconstruction packet |
| Interface context | Same |
| Visible tests | Same |
| Model and tool | Same version and settings when possible |
| Work budget | Same time, turns, or token ceiling |
| Dependencies | Same allowed list |
| Audit evidence | Withheld from both builders |
| Legacy source | Control: visible; Blind: physically absent |
| Cross-contamination | Neither builder sees the other candidate |

If the control receives more time, extra tests, a different model, or a corrected contract that the blind builder did not receive, the result is descriptive but not an A/B test.

# Scoring and decision rule

Record objective results first. Score interpretive dimensions only after the raw evidence is preserved.

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Semantic parity | Major mismatch | Several hidden failures | One bounded mismatch | Full sealed-set parity |
| Integration | Breaks callers | Material regression | Minor repair needed | Full repository pass |
| Security and side effects | New serious risk | Material change | Unclear or bounded drift | No detected regression |
| Performance | Materially worse | Worse beyond budget | Within budget | Equal or better |
| Total complexity | Increased or displaced | No meaningful reduction | Moderate reduction | Clear reduction without displacement |
| Dependency burden | Material increase | Small unjustified increase | Neutral | Reduced or better bounded |
| Corrective burden | Repeated patches | Several corrections | One bounded correction | No post-audit correction |
| Explainability | Behavior cannot be traced | Major gaps | Mostly traceable | Packet-to-code-to-test trace is complete |

Hard gates outrank the total score. A candidate cannot be promoted with a zero in semantic parity, integration, security and side effects, or explainability. The blind method wins a trial only when it passes all hard gates and improves total complexity or corrective burden over the control. A tie is a tie, not evidence of superiority.

## Complexity displacement audit

Count all of the following:

- executable branches and state transitions;
- new files, wrappers, adapters, configuration, and generated artifacts;
- direct and transitive dependencies introduced by the candidate;
- external services, runtime assumptions, environment variables, and deployment steps;
- error-handling burden transferred to callers;
- corrective patches or contract exceptions added after the first audit.

The evaluator in the toy trial reports source lines, an AST branch score, imports, behavior mismatches, and rough timing. These measures are evidence, not a universal maintainability formula.

# The recompile rule

When an audit failure reveals an incomplete contract, do not patch the blind candidate around the newly discovered example.

1. Record what the old packet failed to specify.
2. Update the protection register and reconstruction packet at the source.
3. Tombstone the failed candidate and record what it may no longer claim.
4. Create a clean builder workspace.
5. Start a fresh Builder session with the corrected packet.
6. Rerun the complete audit, not only the failed case.

This is the mechanism that prevents the rebuilt code from immediately inheriting the same add-patch-keep sediment.

# Reading the result honestly

## Promote blind

Use only when the blind candidate passes all hard gates and materially beats both legacy and control on a precommitted dimension without complexity displacement.

## Promote control

Use when ordinary refactoring preserves behavior more reliably or produces the better total system. The experiment exists to discover this result too.

## Recompile

Use when the protocol is viable but the packet or architecture was incomplete. Correct the upstream record and begin a new blind build from blank state.

## Retain legacy

Use when unexplained behavior, weak evidence, integration cost, or risk makes replacement unjustified. A better protection register may be the entire useful yield.

## Reject trial

Use when the baseline, isolation, target choice, audit instrument, or comparison conditions were invalid. Do not score an invalid experiment as a method failure or success.

# Recording a v0.1 run

Do not report a v0.1 run as evidence for or against source-blind reconstruction. It may be shared as a procedural rehearsal or as evidence about defects in the protocol itself.

Publish or share:

- protocol version and date;
- repository and target, or a privacy-safe description;
- model/tool versions and work budgets;
- target-selection answers and baseline evidence;
- packet version and any known unknowns;
- exact isolation method;
- objective results for legacy, control, and blind candidates;
- failure classifications and number of rebuild or patch cycles;
- total-complexity accounting;
- final Auditor decision;
- deviations from this protocol.

Do not publish proprietary code, secrets, private tests, production data, or another party's material without permission. A result can be reported without exposing the protected substrate.

# Provenance and method status

This protocol is an application of the Hofflebrockian Language Specification v2.0 to executable systems. Its strongest direct sources are:

- subject versus representation;
- expression, mechanism, invariant, and world-claim separation;
- production and audit as separate commissions;
- baseline before absence;
- preservation of anomaly;
- structural enforcement;
- observable specifications;
- audit at the scale of failure;
- correction at the mutable source;
- compression for reconstruction;
- re-entry as validation;
- explicit custody;
- stripping borrowed referents and rederiving from local requirements.

The six-role code chain and structural source-withholding rule are experimental developments for this application. They should be revised from completed trials, failed transfer, and independent use, not promoted because the architecture sounds persuasive.

# Package map

| Path | Purpose |
|---|---|
| `START_HERE.md` | Shortest independent route |
| `MANUAL.docx` / `MANUAL.md` | Full operating guide |
| `prompts/00_FAST_PACKET.md` | Combined Custodian-to-Architect evidence pass |
| `prompts/01` through `06` | Rigorous role prompts |
| `prompts/07_CONTROL_REFACTOR.md` | Conventional-refactor control condition |
| `prompts/08_TRIAL_ADJUDICATOR.md` | Final comparison and result summary |
| `templates/` | Records and handoffs |
| `toy_trial/` | Disposable procedural demonstration |

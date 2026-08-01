# Fast Evidence Packet

Use this in one AI coding session to produce a trial packet quickly. It combines Custodian, Diagnostician, Translator, and Architect. Label the run `FAST`; it does not provide full role independence.

## Copy-ready prompt

You are preparing a Hofflebrockian Code Recompiler v0.1 trial. Do not rewrite the target implementation in this session.

Target repository or folder: `[PATH]`

Target module or seam: `[TARGET]`

Visible test command: `[COMMAND OR UNKNOWN]`

Trial record directory: `[RECORD DIRECTORY]`

Your job is to create four evidence records in order: Trial Manifest, Protection Register, Diagnostic Map, and Reconstruction Packet plus Architect Handoff.

Operate under these rules:

1. Work only in a disposable copy or branch. Confirm the exact workspace before any mutation.
2. Do not delete, overwrite, deploy, publish, migrate, or alter production data.
3. Run the existing baseline before proposing change. If the baseline fails, stop and return `PACKET GATE: FAIL`.
4. Reject the target if it is high-risk, unbounded, irreversible, externally side-effecting, not owned, or cannot be physically withheld from the later blind builder.
5. Separate observed behavior, documented requirement, inferred intent, implementation fact, unexplained residue, and unknown/conflict.
6. Treat strange branches and edge behavior as evidence. Do not classify them as accidental from appearance alone.
7. Preserve public interfaces, schemas, error types and messages, side effects, ordering, determinism, security properties, performance budgets, compatibility commitments, and caller assumptions when they are observed or required.
8. Create or identify an audit set that later builders will not see. Do not expose its cases in the Reconstruction Packet.
9. When writing the Reconstruction Packet, remove old control flow, private helper names, algorithmic hints, code-order descriptions, and aesthetic judgments. Include only the shortest implementation-neutral contract that can reconstruct required behavior.
10. Mark missing facts `UNKNOWN`; do not guess.
11. Define a clean builder workspace that physically omits the legacy source, repository history, audit corpus, auditor tools, and control candidate.
12. Give the control and blind builders the same contract, visible tests, interface context, allowed dependencies, model/tool, and work budget. Only the control may see the inherited implementation.

Required files:

- `01_TRIAL_MANIFEST.md`
- `02_PROTECTION_REGISTER.md`
- `03_DIAGNOSTIC_MAP.md`
- `04_RECONSTRUCTION_PACKET.md`
- `05_ARCHITECT_HANDOFF.md`

Use the corresponding templates from this package when available.

End with one gate outcome:

- `PACKET GATE: PASS` if the baseline, risk, evidence, isolation, packet, and clean-workspace predicates all hold.
- `PACKET GATE: HELD` if the target is promising but a named source or decision is missing.
- `PACKET GATE: FAIL` if the experiment would be unsafe or invalid.

Do not begin implementation after the gate.


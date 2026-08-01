# Audit Report

## Trial validity

- Trial ID:
- Auditor:
- Baseline common to both candidates: YES / NO
- Same packet: YES / NO
- Same visible tests: YES / NO
- Same model/tool and work budget: YES / NO
- Blind isolation verified: YES / NO
- Audit set sealed from both builders: YES / NO
- Protocol deviations:
- Trial valid for A/B inference: YES / NO

## Raw objective results

| Measure | Legacy | Control | Blind | Budget or pass condition |
|---|---:|---:|---:|---|
| Baseline / visible tests |  |  |  |  |
| Sealed semantic mismatches |  |  |  | 0 |
| Repository integration failures |  |  |  | 0 |
| Security or side-effect regressions |  |  |  | 0 |
| Performance |  |  |  |  |
| Source lines |  |  |  |  |
| Branch score |  |  |  |  |
| Runtime dependencies |  |  |  |  |
| Corrective attempts |  |  |  |  |

## Audit coverage

- Visible tests:
- Sealed tests:
- Differential cases:
- Property or fuzz cases:
- Performance and memory:
- Security and side effects:
- Dependency and supply chain:
- Repository integration:
- Compatibility:

## Failure routing

| Failure ID | Candidate | Evidence | Layer | Why this is the smallest responsible layer | Required response |
|---|---|---|---|---|---|
| AF-001 |  |  | CONTRACT / ARCHITECTURE / IMPLEMENTATION / TEST / LEGACY / UNKNOWN |  |  |

## Scorecard

Score 0 to 3 after preserving raw evidence.

| Dimension | Control | Blind | Evidence |
|---|---:|---:|---|
| Semantic parity |  |  |  |
| Integration |  |  |  |
| Security and side effects |  |  |  |
| Performance |  |  |  |
| Total complexity |  |  |  |
| Dependency burden |  |  |  |
| Corrective burden |  |  |  |
| Explainability |  |  |  |

## Complexity displacement audit

- New files and wrappers:
- New dependencies:
- New configuration or environment assumptions:
- Burden transferred to callers:
- Operational or deployment steps:
- Post-audit patches or recompile cycles:

## Hard gates

| Gate | Control | Blind |
|---|---|---|
| Semantic parity nonzero | PASS / FAIL | PASS / FAIL |
| Integration nonzero | PASS / FAIL | PASS / FAIL |
| Security and side effects nonzero | PASS / FAIL | PASS / FAIL |
| Explainability nonzero | PASS / FAIL | PASS / FAIL |

## Auditor decision

- Decision: PROMOTE BLIND / PROMOTE CONTROL / RECOMPILE / RETAIN LEGACY / REJECT TRIAL
- Evidence:
- What may now be claimed:
- What may not be claimed:
- Reopen if:
- Next permitted move:


# Protection Register

## Trial reference

- Trial ID:
- Target:
- Governing baseline:
- Register version:

## Protection rows

Use one row per observable or constraint. `Status` is OBSERVED, DOCUMENTED, INFERRED, UNEXPLAINED, UNKNOWN, or CONFLICT.

| ID | Layer | Protected item | Status | Evidence | Invariant | Allowed drift | Failure signal | Audit method | Authority |
|---|---|---|---|---|---|---|---|---|---|
| PR-001 | Interface |  |  |  |  |  |  |  |  |

## Required coverage

### Interface and compatibility

- Public names and signatures:
- Callers:
- Schemas and serialization:
- Version or platform compatibility:

### Behavior

- Accepted inputs:
- Normalization:
- Outputs:
- State transitions:
- Determinism:
- Ordering:

### Failure behavior

- Error types:
- Error messages:
- Retry or recovery semantics:
- Partial-failure behavior:

### Effects and limits

- Side effects:
- Forbidden side effects:
- Security and privacy:
- Performance and memory:
- Concurrency:
- External dependencies:

## Anomaly register

| ID | Observed anomaly or residue | Evidence | What it may encode | What is unknown | Required treatment |
|---|---|---|---|---|---|
| AN-001 |  |  |  |  | Preserve / test / authority decision |

## Unknowns and conflicts

| ID | Missing or conflicting fact | Consequence if guessed | Minimum resolving source or authority |
|---|---|---|---|
| UN-001 |  |  |  |

## Protection gate

- Complete enough for diagnosis: YES / NO
- Items that cannot yet be protected:
- Reopen if:


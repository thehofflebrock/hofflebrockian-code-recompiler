# Reconstruction Packet

## Control

- Trial ID:
- Packet version:
- Target:
- Translator:
- Evidence inputs:
- Legacy implementation viewed in this session: NO
- Repository history viewed in this session: NO
- Sealed audit material viewed in this session: NO

## Target seam

- Module or component:
- Public names and signatures:
- Authorized replacement boundary:
- Callers and integration surface:

## Behavioral contract

### Accepted inputs

| ID | Input | Type / shape | Normalization | Valid range | Evidence |
|---|---|---|---|---|---|
| RC-IN-001 |  |  |  |  |  |

### Outputs and invariants

| ID | Condition | Required output or transition | Invariant | Evidence |
|---|---|---|---|---|
| RC-OUT-001 |  |  |  |  |

### Errors

| ID | Trigger | Error type | Required message or semantics | Side effects before failure | Evidence |
|---|---|---|---|---|---|
| RC-ERR-001 |  |  |  |  |  |

### Effects, order, and state

- Required side effects:
- Forbidden side effects:
- Ordering:
- Determinism:
- State read or written:
- Idempotence or retry semantics:

### Nonfunctional limits

- Security and privacy:
- Performance budget:
- Memory or resource budget:
- Concurrency:
- Compatibility:
- Environmental assumptions:

## Examples and counterexamples

| ID | Input or state | Required result | What this example distinguishes | Evidence |
|---|---|---|---|---|
| RC-EX-001 |  |  |  |  |

## Forbidden outcomes

| ID | Outcome that must not occur | Failure signal | Evidence |
|---|---|---|---|
| RC-NO-001 |  |  |  |

## Allowed dependencies and implementation freedom

- Allowed dependencies:
- Forbidden dependencies:
- Required language or runtime:
- Internal design choices left open to the Builder:

## Visible validation

- Build command:
- Visible test command:
- Visible acceptance conditions:
- Claims these checks do not prove:

## Unknowns and conflicts

| ID | Missing or conflicting requirement | Consequence | Required authority | Builder behavior |
|---|---|---|---|---|
| RC-UN-001 |  |  |  | Emit CONTRACT BLOCK |

## Failure routing

If required behavior is absent or contradictory, the Builder must emit `CONTRACT BLOCK` and stop rather than guess. If audit later exposes a packet gap, revise this packet, tombstone the failed blind candidate, and start a fresh Builder context.

## Translation gate

- Outcome: PASS / HELD / FAIL
- Protected items represented:
- Unknowns preserved:
- Algorithmic inheritance removed:
- Reopen if:


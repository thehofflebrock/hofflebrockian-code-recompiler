# Architect Handoff

## Trial reference

- Trial ID:
- Reconstruction Packet version:
- Target seam:
- Architect:

## Builder workspace

- Workspace root:
- Files permitted in blind workspace:
- Files permitted in control workspace:
- Files physically excluded from blind workspace:
- Parent or sibling access rule:
- Isolation verification:

## Modification boundary

- Files Builder may modify:
- Files Builder may read but not modify:
- Files Builder must not read:
- Public interfaces that must remain stable:

## Dependencies and complexity

- Allowed dependencies:
- Forbidden dependencies:
- Maximum new runtime dependencies:
- Complexity budget:
- Configuration or operational budget:

## Commands

- Build or load command:
- Visible test command:
- Formatting or static check:
- Commands prohibited in Builder sessions:

## Integration and recovery

- Integration seam:
- Candidate output location:
- Build Record location:
- Tombstone location:
- Rollback route:
- Promotion authority:

## Architecture gate

- Outcome: PASS / HELD / FAIL
- Builder has sufficient state without legacy access: YES / NO
- Missing upstream decisions:
- Scope and dependency limits:
- Reopen if:


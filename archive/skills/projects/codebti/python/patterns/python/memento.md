# Memento

## Pattern Intent

Save and restore object state without exposing internal implementation details.

## Python Shape

Use snapshots, immutable state objects, serialized records, dataclass copies, or explicit history entries. Avoid capturing resources that cannot be restored safely.

## When This Style Fits

- Undo, rollback, checkpoints, or audit history are needed.
- State restoration must not leak internals.
- The state model is explicit and bounded.

## When To Avoid

- State is huge or contains external resources.
- Snapshots would hide transaction boundaries.
- A database transaction or event log is more appropriate.

## CodeBTI Signals

The user values reversible workflows, state traceability, and controlled mutation.

## Agent Guidance

Make snapshot boundaries explicit. Test restoration after intermediate mutations and failed operations.

## Related Patterns

Command, Prototype, State.

## Source Reference

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Memento/Conceptual/main.py

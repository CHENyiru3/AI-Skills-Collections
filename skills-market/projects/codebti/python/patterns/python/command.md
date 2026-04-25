# Command

## Pattern Intent

Represent a request as an object so it can be queued, logged, retried, composed, or undone.

## Python Shape

Use dataclasses, callable objects, functions with explicit input models, or command classes. CLI subcommands, job queues, undo stacks, and agent tool calls often fit this shape.

## When This Style Fits

- Work must be scheduled, retried, serialized, or audited.
- Actions need metadata and validation.
- Undo or replay is important.

## When To Avoid

- A direct function call is enough.
- Command objects contain too little behavior.
- The system does not need queuing or history.

## CodeBTI Signals

The user values explicit actions, traceability, and separable execution.

## Agent Guidance

Prefer immutable command data plus explicit handlers. Keep side effects in handlers, not constructors.

## Related Patterns

Chain of Responsibility, Memento, Strategy.

## Source Reference

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Command/Conceptual/main.py

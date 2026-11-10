# State

## Pattern Intent

Let an object change behavior when its internal state changes.

## Python Shape

Use state objects, enums with transition tables, dataclass state models, or explicit workflow classes. Pick the simplest form that makes transitions visible.

## When This Style Fits

- Behavior changes substantially by lifecycle state.
- Transitions have rules worth testing.
- Large conditional blocks are growing around state.

## When To Avoid

- There are only two simple states.
- State classes scatter a small amount of logic.
- The transition model is not well understood.

## CodeBTI Signals

The user wants lifecycle rules encoded in structure rather than repeated conditionals.

## Agent Guidance

Document allowed transitions. Prefer enums and tables before state classes unless behavior truly differs per state.

## Related Patterns

Strategy, Memento, Template Method.

## Source Reference

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/State/Conceptual/main.py

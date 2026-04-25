# Template Method

## Pattern Intent

Define an algorithm skeleton while allowing selected steps to vary.

## Python Shape

Use base classes with hook methods when subclasses share a stable workflow. For simpler cases, use higher-order functions or composition with injected steps.

## When This Style Fits

- The workflow order is fixed and important.
- Subclasses customize only specific steps.
- Shared setup, teardown, or validation should stay centralized.

## When To Avoid

- Subclasses override too many steps.
- Inheritance makes the workflow hard to trace.
- Composition would make variation clearer.

## CodeBTI Signals

The user accepts inheritance when it protects a standard lifecycle or algorithm order.

## Agent Guidance

Keep hooks narrow and named by intent. Prefer final public methods that call overridable protected steps.

## Related Patterns

Strategy, State, Builder.

## Source Reference

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/TemplateMethod/Conceptual/main.py

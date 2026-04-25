# Strategy

## Pattern Intent

Define interchangeable algorithms behind a shared interface.

## Python Shape

Use functions, callable objects, protocols, or small classes. In Python, passing a function is often the most direct Strategy implementation.

## When This Style Fits

- Algorithm choice varies by configuration, data, or user preference.
- The caller should not contain branching for every algorithm.
- Tests should validate algorithms independently.

## When To Avoid

- There are only one or two tiny branches.
- Strategy names are less clear than direct code.
- Shared interface requirements are artificial.

## CodeBTI Signals

The user likes composable behavior, explicit algorithm choice, and testable variation points.

## Agent Guidance

Start with typed callables. Move to classes only when strategies need state, metadata, lifecycle hooks, or multiple methods.

## Related Patterns

State, Template Method, Bridge.

## Source Reference

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Strategy/Conceptual/main.py

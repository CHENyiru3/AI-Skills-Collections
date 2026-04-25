# Prototype

## Pattern Intent

Create new objects by copying existing objects without depending on their concrete classes.

## Python Shape

Use `copy.copy`, `copy.deepcopy`, dataclass `replace`, model copy methods, or explicit clone methods. Prefer explicit copy semantics when objects contain mutable fields, resources, or identifiers.

## When This Style Fits

- Objects are expensive or verbose to construct from scratch.
- A base configuration needs safe variants.
- Tests need small changes to rich fixtures.

## When To Avoid

- Copy depth is ambiguous.
- Objects wrap files, sockets, database sessions, or other external resources.
- Direct construction communicates intent better.

## CodeBTI Signals

The user likes template objects, fixture reuse, and data-oriented variation, but needs clear mutability rules.

## Agent Guidance

Document shallow vs. deep copy behavior. For dataclasses, prefer immutable objects and `dataclasses.replace` where possible.

## Related Patterns

Builder, Memento, Flyweight.

## Source Reference

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Prototype/Conceptual/main.py

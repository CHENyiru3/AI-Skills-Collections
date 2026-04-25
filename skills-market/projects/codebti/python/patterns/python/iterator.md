# Iterator

## Pattern Intent

Traverse a collection without exposing its internal representation.

## Python Shape

Use Python's iterator protocol, generators, iterable objects, and lazy pipelines. Prefer generator functions for simple traversal and classes when traversal needs stateful configuration.

## When This Style Fits

- Data should stream lazily.
- The collection structure should remain private.
- Multiple traversal strategies are needed.

## When To Avoid

- A plain list is clearer and small enough.
- Lazy behavior hides errors too late.
- Iteration order is ambiguous.

## CodeBTI Signals

The user likes data flow clarity, streaming, and encapsulated traversal.

## Agent Guidance

Use idiomatic `__iter__`, generators, and type hints such as `Iterable[T]` or `Iterator[T]`. Document whether iteration is repeatable.

## Related Patterns

Composite, Visitor, Generator Pipelines.

## Source Reference

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Iterator/Conceptual/main.py

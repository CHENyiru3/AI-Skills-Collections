# Flyweight

## Pattern Intent

Share common state across many objects to reduce memory use.

## Python Shape

Use interning, caches, immutable value objects, shared lookup tables, or factories that reuse intrinsic state. Dataclasses with `frozen=True` can make shared state safer.

## When This Style Fits

- Many objects repeat large immutable data.
- Memory pressure is real and measured.
- Object identity is less important than value identity.

## When To Avoid

- Memory is not a proven constraint.
- Shared mutable state would create bugs.
- The cache lifecycle is unclear.

## CodeBTI Signals

The user is performance-aware and accepts indirection when resource pressure justifies it.

## Agent Guidance

Require a measurable reason before using Flyweight. Prefer immutable shared state and explicit cache ownership.

## Related Patterns

Factory Method, Prototype, Singleton.

## Source Reference

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Flyweight/Conceptual/main.py

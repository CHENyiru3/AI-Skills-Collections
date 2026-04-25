# Builder

## Pattern Intent

Construct complex objects step by step while keeping construction separate from the final object.

## Python Shape

Use a builder when object creation has meaningful stages, validation, defaults, or alternative representations. In Python, a dataclass, Pydantic model, keyword-only constructor, or plain helper function is often enough.

## When This Style Fits

- Construction has many optional parts with rules between them.
- The same build process can produce different representations.
- The user wants readable setup code in tests or pipelines.

## When To Avoid

- The object is simple and can be initialized directly.
- Fluent chaining hides invalid intermediate states.
- A builder only duplicates constructor arguments.

## CodeBTI Signals

The user prefers explicit construction phases, readable setup, and controlled object creation over large constructors.

## Agent Guidance

Start with dataclasses and named factory functions. Use a builder class only when staged construction or validation materially improves clarity.

## Related Patterns

Abstract Factory, Factory Method, Template Method.

## Source Reference

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Builder/Conceptual/main.py

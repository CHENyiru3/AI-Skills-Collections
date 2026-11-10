# Factory Method

## Pattern Intent

Let subclasses or specialized creators decide which concrete object to create.

## Python Shape

Use class methods, small factory functions, registries, or overridable methods that return objects behind a shared interface. Prefer explicit names such as `from_config`, `for_backend`, or `create_client`.

## When This Style Fits

- Creation varies by subclass, configuration, or plugin.
- Client code should depend on a stable product interface.
- The project needs controlled extension points.

## When To Avoid

- A direct constructor is clearer.
- Dynamic selection would hide important behavior.
- The factory becomes a catch-all service locator.

## CodeBTI Signals

The user wants extension points but still values clear object lifecycles and named construction paths.

## Agent Guidance

Keep creation logic close to the abstraction it serves. Avoid global registries unless plugin behavior is a real requirement.

## Related Patterns

Abstract Factory, Builder, Strategy.

## Source Reference

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/FactoryMethod/Conceptual/main.py

# Abstract Factory

## Pattern Intent

Create families of related objects without binding client code to concrete classes.

## Python Shape

Use a small factory object or module that returns compatible implementations behind protocols or abstract base classes. Keep the family boundary obvious: database adapters, storage backends, UI widgets, model providers, or environment-specific services.

## When This Style Fits

- The project has multiple related implementations that must be swapped together.
- Client code should not know concrete classes.
- Tests need easy replacement of whole dependency families.

## When To Avoid

- There is only one implementation.
- A simple function parameter or constructor injection is enough.
- The factory hierarchy would be larger than the product code.

## CodeBTI Signals

The user values explicit boundaries, consistency across related components, and dependency replacement without scattering conditionals.

## Agent Guidance

Prefer protocols plus clear factory functions before deep abstract class trees. In generated code, keep factory selection near configuration and keep product usage free of implementation checks.

## Related Patterns

Factory Method, Builder, Strategy, Dependency Injection.

## Source Reference

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/AbstractFactory/Conceptual/main.py

# Bridge

## Pattern Intent

Split an abstraction from its implementation so both can vary independently.

## Python Shape

Use protocols or abstract base classes for implementation backends, with a high-level abstraction delegating to them. This is useful for storage engines, renderers, model providers, notification channels, and execution backends.

## When This Style Fits

- Two dimensions vary independently.
- The project needs multiple backends behind one workflow.
- Inheritance would create a combinatorial class hierarchy.

## When To Avoid

- There is only one meaningful dimension of variation.
- Simple dependency injection is enough.
- The bridge adds vocabulary users do not need.

## CodeBTI Signals

The user thinks in stable interfaces and replaceable backends, and wants to control dependency boundaries.

## Agent Guidance

Name both sides plainly. Keep the abstraction focused on user intent and the implementation focused on technical detail.

## Related Patterns

Adapter, Strategy, Abstract Factory.

## Source Reference

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Bridge/Conceptual/main.py

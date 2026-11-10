# Singleton

## Pattern Intent

Ensure one instance exists and provide a global access point to it.

## Python Shape

Python modules, dependency injection containers, cached factory functions, or process-level configuration objects often replace explicit Singleton classes. If thread safety matters, initialization must be deliberate and tested.

## When This Style Fits

- The object represents truly process-wide infrastructure.
- Repeated construction is incorrect or expensive.
- The lifecycle is simple and controlled by application startup.

## When To Avoid

- It hides dependencies from tests.
- It creates mutable global state.
- Different callers need different configurations.

## CodeBTI Signals

The user accepts centralized infrastructure but may be trading testability for convenience.

## Agent Guidance

Default to dependency injection or module-level constants. Use Singleton only when the generated `CodeStyle.md` explicitly allows process-global state.

## Related Patterns

Facade, Factory Method, Proxy.

## Source Reference

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream examples:
  - https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Singleton/Conceptual/NonThreadSafe/main.py
  - https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Singleton/Conceptual/ThreadSafe/main.py

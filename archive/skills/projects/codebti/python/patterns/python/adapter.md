# Adapter

## Pattern Intent

Allow incompatible interfaces to collaborate through a compatibility layer.

## Python Shape

Use wrapper classes, thin functions, protocols, or small modules that normalize third-party APIs into project-native interfaces. Python supports both object adapter style and class inheritance style, but composition is usually clearer.

## When This Style Fits

- A third-party library does not match project conventions.
- Legacy code must be used behind a stable interface.
- Tests need a simple fake for a complex dependency.

## When To Avoid

- The adapter only renames one method without reducing coupling.
- Wrapping hides important behavior or failure modes.
- The project can directly use the dependency cleanly.

## CodeBTI Signals

The user values local consistency and wants external APIs contained at boundaries.

## Agent Guidance

Prefer composition-based adapters. Put adapters near integration boundaries and keep domain code free of vendor-specific types.

## Related Patterns

Facade, Proxy, Bridge, Dependency Injection.

## Source Reference

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream examples:
  - https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Adapter/Conceptual/object/main.py
  - https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Adapter/Conceptual/class/main.py

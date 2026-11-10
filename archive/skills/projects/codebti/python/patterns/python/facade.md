# Facade

## Pattern Intent

Provide a simple interface over a complex subsystem.

## Python Shape

Use a module-level API, service class, CLI command layer, or orchestration function that hides internal sequencing while preserving clear domain language.

## When This Style Fits

- Users need one clear entrypoint.
- Internal dependencies are complex or unstable.
- The project benefits from separating orchestration from low-level details.

## When To Avoid

- The facade becomes a giant god object.
- It hides errors or important configuration.
- It merely forwards every method unchanged.

## CodeBTI Signals

The user values approachable APIs, stable public surfaces, and readable workflows.

## Agent Guidance

Make facades thin, named by user intent, and easy to test through behavior. Keep complex logic in dedicated collaborators.

## Related Patterns

Adapter, Proxy, Mediator.

## Source Reference

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Facade/Conceptual/main.py

# Decorator

## Pattern Intent

Add behavior by wrapping an object without changing its interface.

## Python Shape

Use wrapper objects for runtime composition and function decorators for call behavior. Keep Python's `@decorator` syntax distinct from the GoF object-wrapper pattern when writing guidance.

## When This Style Fits

- Behavior must be composed in different combinations.
- Cross-cutting behavior should stay outside core logic.
- The wrapped interface remains stable.

## When To Avoid

- Wrapper chains obscure control flow.
- State is split across too many layers.
- A direct function call or option flag is clearer.

## CodeBTI Signals

The user likes composable behavior and clean cores, but may need guardrails against invisible magic.

## Agent Guidance

Use decorators for logging, caching, retries, validation, or instrumentation only when behavior remains obvious in tests and docs.

## Related Patterns

Proxy, Adapter, Composite.

## Source Reference

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Decorator/Conceptual/main.py

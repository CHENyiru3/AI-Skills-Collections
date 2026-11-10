# Chain of Responsibility

## Pattern Intent

Pass a request through handlers until one handles it or the chain ends.

## Python Shape

Use ordered handler lists, middleware stacks, validation pipelines, command routers, or exception fallback chains. Functions are often enough; classes help when handlers carry state.

## When This Style Fits

- Multiple handlers may process the same request type.
- Handler order is configurable or domain meaningful.
- The caller should not know which handler succeeds.

## When To Avoid

- The flow must be easy to trace step by step.
- Handler order is accidental or fragile.
- A simple `if`/`elif` table is clearer.

## CodeBTI Signals

The user prefers extensible pipelines and localized responsibility over central branching.

## Agent Guidance

Make chain order explicit and test both handled and unhandled requests. Keep handler contracts small.

## Related Patterns

Command, Middleware, Strategy.

## Source Reference

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/ChainOfResponsibility/Conceptual/main.py

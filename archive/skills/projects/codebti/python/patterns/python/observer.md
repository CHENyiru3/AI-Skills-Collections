# Observer

## Pattern Intent

Notify subscribers when an observed object changes.

## Python Shape

Use callbacks, event emitters, signal systems, async queues, or typed event dispatch. Keep subscription lifecycle visible to avoid leaks and surprise side effects.

## When This Style Fits

- Multiple independent consumers react to events.
- The publisher should not know subscribers.
- Events are part of the domain or integration boundary.

## When To Avoid

- Synchronous control flow is easier to reason about.
- Subscriber order matters but is hidden.
- Side effects become hard to test.

## CodeBTI Signals

The user prefers decoupled event-driven extension and accepts indirect flow when it is documented.

## Agent Guidance

Use typed event payloads and explicit subscribe/unsubscribe APIs. In tests, assert emitted events as behavior.

## Related Patterns

Mediator, Command, Chain of Responsibility.

## Source Reference

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Observer/Conceptual/main.py

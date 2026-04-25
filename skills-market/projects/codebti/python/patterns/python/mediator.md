# Mediator

## Pattern Intent

Reduce direct dependencies between components by routing collaboration through a mediator.

## Python Shape

Use an event bus, coordinator object, workflow service, controller, or orchestration layer. The mediator should own interaction policy, not all business logic.

## When This Style Fits

- Many components otherwise depend on each other directly.
- Interaction rules change independently of components.
- A workflow needs centralized coordination.

## When To Avoid

- The mediator becomes a god object.
- Components can collaborate directly without coupling problems.
- Events make control flow hard to follow.

## CodeBTI Signals

The user wants low coupling and centralized orchestration, but needs limits on abstraction sprawl.

## Agent Guidance

Keep mediator methods use-case oriented. Avoid generic event strings when typed method calls or explicit event models are clearer.

## Related Patterns

Observer, Facade, Command.

## Source Reference

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Mediator/Conceptual/main.py

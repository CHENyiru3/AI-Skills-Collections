# Python Design Pattern Database

This database covers the classic GoF pattern catalog for Python and adapts it for CodeBTI style inference.

Use each page to answer three questions:

1. Does this pattern match the user's project problem?
2. Does this pattern match the user's preferred coding style?
3. Should generated code actively use it, permit it, or avoid it?

## Creational Patterns

- [Abstract Factory](abstract-factory.md)
- [Builder](builder.md)
- [Factory Method](factory-method.md)
- [Prototype](prototype.md)
- [Singleton](singleton.md)

## Structural Patterns

- [Adapter](adapter.md)
- [Bridge](bridge.md)
- [Composite](composite.md)
- [Decorator](decorator.md)
- [Facade](facade.md)
- [Flyweight](flyweight.md)
- [Proxy](proxy.md)

## Behavioral Patterns

- [Chain of Responsibility](chain-of-responsibility.md)
- [Command](command.md)
- [Iterator](iterator.md)
- [Mediator](mediator.md)
- [Memento](memento.md)
- [Observer](observer.md)
- [State](state.md)
- [Strategy](strategy.md)
- [Template Method](template-method.md)
- [Visitor](visitor.md)

## Python Guidance

Modern Python often has simpler alternatives to classic class-heavy patterns: functions, protocols, dataclasses, context managers, generators, decorators, dependency injection, and small modules. Prefer the simplest shape that preserves the user's desired boundaries.

When generating a `CodeStyle.md`, translate each preferred pattern into enforceable rules:

- naming and module boundaries,
- typing policy,
- allowed abstraction depth,
- test shape,
- and review checks for overuse.

# Proxy

## Pattern Intent

Control access to another object by standing in front of it.

## Python Shape

Use proxies for lazy loading, authorization, caching, rate limiting, remote clients, or instrumentation. In Python, wrapper classes and descriptors can both act as proxies.

## When This Style Fits

- Access needs checks or side effects.
- Expensive resources should initialize lazily.
- The real object is remote, slow, or protected.

## When To Avoid

- The proxy hides network or IO costs.
- It changes behavior in surprising ways.
- Direct dependency injection is clearer.

## CodeBTI Signals

The user wants controlled boundaries and accepts a wrapper when it protects correctness or resources.

## Agent Guidance

Make proxy behavior visible in names, docs, and tests. Do not let a proxy silently alter domain semantics.

## Related Patterns

Adapter, Decorator, Facade.

## Source Reference

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Proxy/Conceptual/main.py

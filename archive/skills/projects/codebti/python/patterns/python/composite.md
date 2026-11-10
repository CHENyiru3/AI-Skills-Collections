# Composite

## Pattern Intent

Represent tree structures so leaves and containers can be used through one interface.

## Python Shape

Use recursive dataclasses, protocols, or simple node classes for filesystems, ASTs, UI trees, menu trees, pipelines, or nested validation rules.

## When This Style Fits

- The domain is naturally hierarchical.
- Operations should work uniformly on single items and groups.
- Recursive traversal is central to the project.

## When To Avoid

- The hierarchy is shallow and fixed.
- Leaf and container behavior is too different.
- A plain list or dictionary is easier to read.

## CodeBTI Signals

The user accepts structural abstraction when it makes recursive workflows fluent and consistent.

## Agent Guidance

Define the common interface narrowly. Avoid forcing every leaf to support container-only operations.

## Related Patterns

Iterator, Visitor, Decorator.

## Source Reference

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Composite/Conceptual/main.py

# Visitor

## Pattern Intent

Add operations to object structures without changing the objects themselves.

## Python Shape

Use visitor classes for stable object hierarchies with many operations. Python alternatives include singledispatch, pattern matching, explicit methods, or plain recursion.

## When This Style Fits

- The object structure is stable.
- New operations are added more often than new node types.
- Traversal and operation logic should be separated.

## When To Avoid

- New node types are added frequently.
- The visitor interface becomes noisy.
- Pattern matching or direct methods are clearer.

## CodeBTI Signals

The user values separation between data structures and operations, and accepts ceremony for extensibility.

## Agent Guidance

Use Visitor sparingly in Python. Consider `functools.singledispatch` or `match` first unless double dispatch is genuinely useful.

## Related Patterns

Composite, Iterator, Command.

## Source Reference

- Catalog: https://refactoring.guru/design-patterns/python
- Upstream example: https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Visitor/Conceptual/main.py

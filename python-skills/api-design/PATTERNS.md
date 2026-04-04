# API Patterns

Use these patterns when a Python library needs to grow without becoming confusing.

## Progressive Disclosure

- Start with a simple function for the common path.
- Add a class only when configuration or shared state makes it easier to use.
- Reserve low-level modules for advanced users and document them as such.

## Good Patterns

### Options Object for Many Knobs

Prefer a dataclass or config object when a function is accumulating many keyword-only flags.

### Builder for Multi-Step Assembly

Use a builder when the user naturally constructs an object in stages before calling `build()`.

### Factory for Variant Selection

Use `from_*` classmethods or top-level factory functions when the caller chooses between input formats.

## Return-Type Rules

- Return one primary shape for one operation.
- Avoid returning unrelated types based on flags.
- Prefer rich result objects over tuples once the meaning is no longer obvious.

## Public API Boundaries

- Keep `_internal` modules private.
- Re-export the intended public surface from `__init__.py`.
- Mark experimental APIs clearly in names or docs.

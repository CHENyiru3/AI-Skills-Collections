---
name: designing-python-apis
domain: programming
description: 'Design or review a public Python package API: signatures, return/error contracts, naming and compatibility. Use for explicit interface design or deprecation work; not every internal function edit.'
metadata:
  version: "1.0.1"
---

# Python API Design

Start from representative calling code and the package's current supported users.
Preserve established naming and behavior unless the requested change includes a
migration. Optimize a common call without making exceptional use impossible.

- Distinguish public exports from internal implementation. A new abstraction needs
  a concrete caller; underscore naming alone does not enforce privacy.
- Specify accepted types/shapes, mutability/ownership, return types and side effects.
  Decide whether an iterable may be consumed once, copied or modified in place.
- Use keyword-only options when adjacent positional values are ambiguous. Preserve
  positional/keyword compatibility when changing an existing signature.
- Distinguish absent values from valid false/empty values. Avoid mutable defaults
  and coercions that silently erase caller intent.
- Document actionable exception types and failure conditions; keep diagnostic
  messages useful without exposing secrets. Do not invent exception classes that
  the package does not define.
- For a deprecation, identify affected callers, a replacement, a supported warning
  path and removal policy. Test that compatibility wrappers preserve results and
  warning attribution. A rename is not compatible merely because it reads better.

Read [EVOLUTION.md](EVOLUTION.md) for migration work and [PATTERNS.md](PATTERNS.md)
when a builder/factory solves an actual interface problem. Treat examples as
illustrative, not a mandate to add patterns.

Validate representative calls and a relevant error/compatibility case. Stop when
the requested interface contract is clear and verified; do not require a package
redesign for a narrow API question.

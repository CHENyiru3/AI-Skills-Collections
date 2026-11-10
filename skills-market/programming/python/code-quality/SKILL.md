---
name: improving-python-code-quality
domain: programming
description: Fix Python lint/type-checking problems or perform a requested focused maintainability refactor. Use the project’s configured tools and supported Python versions; not a mandatory reconfiguration for every Python edit.
metadata:
  version: "1.0.1"
---

# Python Code Quality

Inspect `pyproject.toml`, supported Python versions and existing Ruff/type-checker
configuration before changing rules or syntax. Run the relevant existing checks
without autofix first when diagnosing a problem; limit edits to the requested scope.

Distinguish behavior fixes from mechanical style changes. Avoid a formatter sweep
that obscures a small functional diff. Keep public names, exception behavior and
mutation semantics unless an interface change is requested.

For types, model real optional/union cases and ownership rather than silencing
errors with `Any`, ignores or casts. Respect the project's strictness and version
floor; do not impose Python 3.10 syntax or strict mypy on an older codebase. Add a
`py.typed` marker only when distributing a typed package, including it in the build.

When replacing a mutable default with `None`, initialize only when the value is
`None`; `items or []` can discard the identity of a valid empty container. Catch
specific expected exceptions without swallowing failures or logging secrets.

Load only the relevant resource:

- [RUFF_CONFIG.md](RUFF_CONFIG.md) for a requested lint configuration change.
- [MYPY_CONFIG.md](MYPY_CONFIG.md) for strictness/override choices.
- [TYPE_PATTERNS.md](TYPE_PATTERNS.md) for protocols and advanced typing.

Re-run changed-file checks and tests for behavior the refactor can affect. Report
pre-existing failures separately. Stop when the requested quality issue is resolved;
new tools, full coverage and repository-wide cleanup are not automatic prerequisites.

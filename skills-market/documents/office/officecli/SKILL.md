---
name: officecli
domain: documents
description: Use the local OfficeCLI backend to inspect or modify Office files when OfficeCLI is requested, selected by the project, or already in use. Route format-specific work to its adapter; do not override a requested Marp, native Office or other backend.
metadata:
  version: "1.0.1"
---

# OfficeCLI Backend

Discover `officecli` with `command -v officecli` and inspect its version/help.
A user-local binary such as `~/.local/bin/officecli` is a fallback only if it exists;
do not assume that installation path or install/upgrade globally by default.

Read before editing: use `view`, `get`, `query` or `validate` to identify the file
and actual element paths. Prefer structured DOM operations over raw XML when they
cover the task. Use the installed property help rather than inventing selectors:

```bash
officecli docx set paragraph
officecli pptx set shape
officecli xlsx get
```

Quote indexed paths in shells such as zsh. Prefer structured JSON output when
parsing results. Re-query after operations that can shift element indices; stale
paths can edit the wrong object.

For repeated edits, consider batch or resident mode only when supported and useful.
Close/flush a resident file before inspecting its saved result. The number of
operations alone does not require a stateful session. Use raw part edits only with
a known package/relationship contract and validate the resulting file.

Use `officecli-docx`, `officecli-pptx` or `officecli-xlsx` only for the matching
format when this backend is selected. Preserve the original template/content and
check changed structure plus the relevant rendering or formulas. A tool's issue
list is evidence, not proof that layout or calculations are correct. Stop after
the requested changes and relevant verification; do not demand a full-file rewrite.

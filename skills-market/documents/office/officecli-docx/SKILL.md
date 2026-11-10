---
name: officecli-docx
domain: documents
description: Inspect or edit DOCX through OfficeCLI when that backend is requested, selected by the project or already in use. Not a universal router for every Word document or a substitute for a chosen document backend.
metadata:
  version: "1.0.1"
---

# OfficeCLI DOCX

Discover the installed OfficeCLI version/help, then inspect the document's text,
outline and relevant DOM nodes before editing. Use [editing.md](editing.md) for an
existing document or [creating.md](creating.md) for a new one; verify example
properties with installed help.

Quote indexed paths such as `"/body/p[1]"` in zsh. Reuse named paragraph styles
and actual section/page settings. Prefer paragraph spacing to empty paragraphs
for layout, while preserving intentional content and the user's template.

Inspect tracked changes, comments and fields before changing affected ranges.
Do not accept/reject revisions or remove comments merely to simplify editing.
For raw XML, preserve run formatting, relationships and whitespace semantics.
Batch/resident mode is optional; close/flush before checking the saved file.

Check affected text, outline and structure with `view`/`validate`, and inspect a
rendered preview when layout changed. Queries for empty paragraphs or missing alt
text are leads, not a reason to delete intentional content. Stop when the requested
edit is valid and readable; preserve the explicit output path and original file.

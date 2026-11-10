---
name: officecli-pptx
domain: documents
description: Create or edit PPTX through OfficeCLI when that backend is requested, selected by the project or already in use. Exclude Marp source decks and presentations being handled through another chosen backend.
metadata:
  version: "1.0.1"
---

# OfficeCLI PPTX

Inspect the installed OfficeCLI help and the deck's slides, outline, notes and
actual shape paths. Read [creating.md](creating.md) for a new deck or
[editing.md](editing.md) for a targeted update. Preserve an existing template,
master/layout, reading order and intended animations unless the task changes them.

Quote indexed paths such as `"/slide[1]/shape[1]"`. Re-query after z-order or shape
changes because indices can shift. Use installed `pptx set shape`/`pptx add` help
rather than guessing properties. A blank layout is suitable for a custom slide,
not a reason to discard an existing master.

Inspect changed slides visually with a supported preview/rendering tool and check
structure with `view issues` and `validate`. Check text fit, contrast, overlaps and
notes/links affected by edits. Valid XML alone does not prove readable layout.
Fix actual defects; no forced defect-finding, extra polish cycle or independent
agent is required for an already acceptable result. Stop at the requested deck edit.

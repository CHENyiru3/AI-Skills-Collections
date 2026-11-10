---
name: pptx
domain: documents
description: Create, inspect or edit a PowerPoint .pptx artifact, including its layout, notes, charts and template structure. Honor an explicit OfficeCLI or other backend; exclude Marp source decks and prose-only presentation planning.
license: Proprietary. LICENSE.txt has complete terms
metadata:
  version: "1.0.1"
---

# PowerPoint Work

Identify the requested output, template, slide range and backend. Preserve master
layouts, theme, notes, relationships and media outside the requested changes.
Extracted text is useful for content review but cannot establish visual correctness.

- For a template or existing deck, read [editing.md](editing.md). Inspect slides
  visually before editing and preserve shape/slide identities where they matter.
- For a new PptxGenJS deck, read [pptxgenjs.md](pptxgenjs.md) only when that backend
  is selected. Verify API behavior against its installed version.
- Use `scripts/thumbnail.py` for a visual overview and `scripts/office/unpack.py`
  for relevant OOXML parts; inspect helper help before using its arguments.

Follow the brief and established design system. Choose typography, color and
spacing for the content/audience; a fixed palette, dark/light sandwich, motif or
visual on every slide is optional design advice. Text-only slides can be appropriate.
Keep evidence, chart units and citations faithful to supplied sources.

For layout edits, render the changed slides and inspect text fit, overlap, contrast,
reading order, image crops and source/footnote placement. Validate package structure
and compare extracted content/order to the requested changes. Check actual leftover
placeholders, distinguishing them from legitimate quoted/example text.

When LibreOffice and Poppler are available, the bundled conversion helper can render:

```bash
python scripts/office/soffice.py --headless --convert-to pdf output.pptx
pdftoppm -jpeg -r 150 output.pdf slide
```

Use an output directory that distinguishes fresh renders from stale files. A
successful conversion alone does not prove layout quality. Fix actual issues and
recheck affected slides; if the first inspection passes, no forced defect or
fix-and-verify cycle is required. Independent review is optional when authorized
and useful, not mandatory even for a small deck.

Report delivered artifacts and checks, including unavailable rendering. Stop when
the requested deck content/layout is correct and reviewable; do not invent defects
or redesign an acceptable deck to satisfy a style checklist.

---
name: docx
domain: documents
description: Create, inspect or edit a Word .docx artifact when its document structure, layout, tracked changes or comments need handling. Honor a requested OfficeCLI or other document backend; exclude prose-only drafts and non-DOCX artifacts.
license: Proprietary. LICENSE.txt has complete terms
metadata:
  version: "1.0.1"
---

# Word DOCX Work

Identify the source, requested changes, output path and backend. Preserve existing
styles, sections, fields, comments and revision history unless the task changes them.
A DOCX is an OOXML package; plain text extraction does not preserve its semantics.

## Select the operation

- For reading, use a document-aware extractor or inspect relevant package parts.
  If revisions matter, include them rather than silently accepting changes.
- For a new document, use the chosen document library/backend and existing template.
  Install dependencies only in a suitable task environment, not globally by default.
- For existing-package edits, unpack → change affected parts → repack/validate.
  Work on a copy and retain the original for comparison.
- Convert legacy `.doc` with an available office engine before OOXML editing.

Bundled helpers are available under `scripts/`; inspect their `--help` before use:

```bash
python scripts/office/unpack.py document.docx unpacked/
python scripts/office/pack.py unpacked/ output.docx --original document.docx
python scripts/office/validate.py output.docx
```

Unpacking can merge adjacent runs; use the supported merge-runs option when run
boundaries matter. Repacking validation/auto-repair does not fix all malformed
relationships or semantic errors. Do not disable checks just to obtain an output.
`scripts/accept_changes.py` is only for a requested clean copy accepting revisions.

## Creation contracts that affect rendering

Use real paragraph/list/heading structures, not bullet characters and blank lines
to imitate them. Set page size, orientation and margins from the user's template or
brief. DXA is 1440 per inch; drawings commonly use 914400 EMU per inch. Verify the
saved section dimensions, especially when a library transforms landscape settings.

Use named styles and appropriate outline levels for navigable headings/TOCs.
Respect the template's typography; Arial, black titles and fixed page dimensions
are not universal requirements. Fields/TOCs may need an office engine to update.

For fixed-width tables, keep table grid, column and cell widths consistent and
within the section's content width. Padding reduces cell content space. Choose
width/shading behavior for the target renderer rather than assuming every Word or
Google Docs version has identical behavior. Avoid layout tables when paragraph
borders or tab stops express the intent more reliably.

Supply image format, dimensions and meaningful alt text as required by the chosen
library/version. Preserve aspect ratio unless a crop/distortion was requested.
Represent page breaks inside valid paragraph structure. Check library-specific
API details against the installed version instead of copying a large stale tutorial.

## XML edits and redlines

Use an XML-aware method or a precise supported editor; Python is not prohibited.
Escape text correctly and preserve `xml:space="preserve"` where leading/trailing
spaces matter. Retain namespaces, element order, IDs, content types and relationship
targets. Do not use regular expressions to rewrite arbitrary nested XML.

Use the requested author or a truthful agent identity for comments/revisions; do
not impersonate another author. Mark only the changed range and preserve `w:rPr`
formatting. Common revision structure is:

```xml
<w:del w:id="1" w:author="Agent"><w:r><w:delText>old</w:delText></w:r></w:del>
<w:ins w:id="2" w:author="Agent"><w:r><w:t>new</w:t></w:r></w:ins>
```

The wrappers are siblings at a valid parent, not inserted inside a run. Deletions
use `w:delText` (or `w:delInstrText` for field instructions). Allocate valid unused
IDs and timestamps. When deleting an entire paragraph/list item, handle the
paragraph-mark revision as well; otherwise accepting changes can leave an empty
paragraph. Preserve another author's revisions rather than rewriting their history.

For comments, `scripts/comment.py` handles related comment parts; follow its help
for author/reply syntax. It does not automatically anchor every range in document
XML. Range-start/end markers must be at valid sibling positions around runs, with
matching IDs and comment references, not inside `w:r`. Validate reply/thread parts.

For images, add the media, content type, package relationship and drawing reference
together. A placeholder relationship URI is not a complete OOXML element. Compare
the original and changed package to catch accidental loss of headers, fields,
footnotes or links outside the intended range.

## Verify the delivered document

Run structural validation and inspect extracted changed text. When layout changes,
render the output with the target or a suitable office engine and inspect affected
pages for clipping, page breaks, table overflow and typography. The bundled
`scripts/office/soffice.py` can support conversion when LibreOffice is available;
Poppler can render the resulting PDF. Report any unavailable render check.

Stop when the requested content/revision and relevant structure/layout checks pass.
Do not require a new font system, global installation or extra review cycle.

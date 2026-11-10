---
name: pdf
domain: documents
description: Extract, transform, create or fill a PDF artifact when PDF-specific page, text, form or rendering behavior matters. Use for an actual PDF operation; a PDF citation alone does not require file processing.
license: Proprietary. LICENSE.txt has complete terms
metadata:
  version: "1.0.1"
---

# PDF Processing

Establish the source, requested operation, page range and output path. Preserve
originals and use the available PDF backend suited to the task. Text extraction,
page transformation, OCR and rendering have different correctness criteria.

## Read or transform

Extract page text with a document-aware library/Poppler and preserve page provenance.
An extraction may return `None` or empty text; distinguish image-only pages from
missing content before choosing OCR. Reading order and extracted tables are not
guaranteed by a successful API call. Check representative rows, headers and page
boundaries before concatenating tables into one dataset.

For page operations, verify one-based CLI page numbers versus zero-based library
indices, rotation and page boxes. Check bookmarks, annotations and forms when they
must survive merging/splitting. Choose output filenames that do not overwrite inputs
mid-operation. Access/decryption requires the user's legitimate password/access;
do not expose credentials in commands or reports.

Read [reference.md](reference.md) for a relevant advanced/library operation. Check
installed APIs/help before using version-sensitive options; do not load a whole
copied API manual for a simple extraction.

## Fill forms

Read [forms.md](forms.md) when filling a form. Identify actual AcroForm fields
before choosing field values, including checkbox/radio export values. If the form
is an image/flat document, use an overlay with verified coordinates rather than
pretending it has editable fields. Distinguish PDF bottom-origin coordinates from
rendered-image top-origin pixels, accounting for scale, crop and rotation.
Use the bundled `scripts/` helpers for the relevant branch and inspect the filled
pages. Do not fabricate missing personal information or flatten an editable form
unless that is wanted.

## Create and verify

Respect requested page dimensions, font hierarchy and layout. Ensure the selected
font covers required glyphs; built-in ReportLab fonts may lack Unicode sub/superscripts.
Paragraph sub/super markup or a suitable embedded font are alternatives, not a
universal ban on Unicode. Do not assume successful PDF generation proves legibility.

Check page count and requested content. Render affected pages and inspect clipping,
font substitution, table alignment and overlays when layout changed. For OCR, label
recognition uncertainty and verify consequential values against the page image.
Stop when the requested PDF operation and its relevant checks are complete.

# Editing existing scientific PDFs

Read this when modifying PDF artwork directly. Use the current environment's PDF skill and bundled dependencies where available. This reference records fragile mechanics learned from the figure work, not a replacement PDF manual.

## Choose the editing route

Prefer a current plotting/vector source when it reproduces the author-approved artwork and preserves manual changes. An Affinity-authored publication PDF can differ materially from the repository's reproduction components. Trace that relationship before rebuilding.

For a PDF-only adjustment, retain existing scientific graphics and alter text or layout locally. Avoid replacing measured plots with generated bitmap artwork. Editable vector text, curves, cells, and network paths are valuable for later author edits.

Snapshot the current file and its SHA-256 before modification. Recheck the hash before replacing it. Old backups and historical helper scripts are references; they are not the next edit's automatic input. If the author has changed the file during work, preserve those changes and reconcile the candidate.

## Text and coordinates

- Render the page. Text extraction cannot establish visual alignment on its own.
- Inspect the MediaBox, CropBox, origin, and page rotation. A page can have a nonzero origin. Do not reuse old placement coordinates after a new author revision.
- Embedded Identity-H subset fonts need their ToUnicode mapping. Blind ASCII or global case replacement can damage glyphs or scientific names.
- If an intended glyph is absent from the subset, use an appropriate embedded matching font for that label. Preserve actual point sizes after transforms.
- Rotated text can produce misleading per-character font-size values in extraction. Inspect text matrices and the rendered page before deciding that a font is undersized.
- Existing repeated labels may sit inside raster artwork. If relabeling is necessary, mask only the old label area and preserve the scientific image beneath; do not regenerate or distort the anatomy.

## Group geometry and preserve artwork

- A single visible map can contain multiple registered rasters. Move/scale the complete group with one transform.
- Normalize map cells by equal viewports, isotropic fitting, and consistent centers. Preserve relative scale when it represents biology or a controlled comparison.
- For charts, define the intended inner data frames explicitly and move tick labels, legends, and captions coherently with them. Verify axis-value-to-gridline alignment after changing frame height or width.
- A rectangle clipped from the entire source page can include fragments of neighboring artwork if source regions overlap. Isolate the unit's drawing operations or a genuine source group when necessary. Inspect complete 3D cube corners, network loops, and faint points.
- Reuse source paths and images rather than redrawing scientific results unnecessarily. Check raster/mask hashes and unchanged drawing operations where practical. Hashes alone do not prove condition identity or complete visible content.

## PDF structure and verification

In pypdf, assign stream objects through indirect references, including `/Contents`, image XObjects, and Form XObjects. For example:

```python
page[NameObject('/Contents')] = writer._add_object(stream)
xobjects[NameObject('/Map')] = writer._add_object(image_stream)
# When reusing an existing indirect resource, preserve its raw reference:
xobjects[NameObject('/Map')] = source_xobjects.raw_get('/Map')
```

Direct inline image streams inside resource dictionaries produced a PDF that rendered in Poppler but appeared to have zero pages to pdfminer/pdfplumber. Validate with both a renderer and a parser; confirm page count, extracted text, and valid resource references.

Avoid unnecessary reserialization of all drawing numbers for a tiny label change. A local content patch or well-scoped transform often preserves scientific artwork more precisely. When content is reserialized, compare the relevant operations and final render.

For a text-only correction, a localized pixel comparison is useful: changes should be confined to the intended old/new text regions. For layout changes, verify unit geometry and artwork integrity rather than expecting an unchanged whole-page image. Inspect the latest rendered result after the last edit.

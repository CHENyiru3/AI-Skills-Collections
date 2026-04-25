# Editing Existing `.docx` Files

Use this path when the document already exists.

## Inspect First

```bash
officecli view doc.docx issues
officecli view doc.docx outline
officecli view doc.docx text --max-lines 200
officecli get doc.docx /body --depth 1
```

## Safe Editing Order

1. Structural changes first: add, remove, move
2. Re-query paths after structural changes
3. Update text, tables, images, headers, or charts
4. Re-run QA

## Examples

```bash
officecli set doc.docx "/body/p[1]" --prop text="Updated Title"
officecli set doc.docx "/body/tbl[1]/tr[2]" --prop c1="North America" --prop c2="$4.2M" --prop c3="$5.1M"
officecli set doc.docx "/body/tbl[1]/tr[2]/tc[3]" --prop bold=true --prop color=2C5F2D
officecli set doc.docx "/header[1]" --prop text="Updated Company Name"
officecli remove doc.docx "/body/p[10]"
officecli move doc.docx "/body/p[8]" --index 2
```

## Pitfalls

- Remove elements from highest index to lowest.
- Row-level table `set` is for content shortcuts, not full formatting.
- Verify formulas, charts, and cross-references after structural changes.
- Use raw XML only when high-level commands cannot express the change.

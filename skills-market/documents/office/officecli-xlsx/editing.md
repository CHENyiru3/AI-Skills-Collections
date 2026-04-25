# Editing Existing `.xlsx` Files

Use this path when the workbook already exists.

## Inspect First

```bash
officecli view data.xlsx issues
officecli view data.xlsx outline
officecli view data.xlsx annotated
officecli get data.xlsx "/Sheet1/A1:F20"
```

## Safe Editing Order

1. Structural changes first: add/remove sheets, rows, columns
2. Re-check formulas and named ranges after structure changes
3. Update values, formulas, charts, and formatting
4. Re-run QA

## Examples

```bash
officecli set data.xlsx "/Sheet1/B14" --prop formula="SUM(B2:B13)"
officecli set data.xlsx "/Sheet1/C4" --prop value=12500 --prop numFmt='$#,##0'
officecli remove data.xlsx "/OldSheet"
officecli add data.xlsx / --type sheet --prop name="Summary"
officecli set data.xlsx "/namedrange[RevenueTotal]" --prop ref="Sheet1!B14"
```

## Pitfalls

- Cross-sheet formulas can break if written with bad shell quoting; verify with `get`.
- After inserting or removing rows, check formula ranges manually.
- Use batch mode for bulk edits instead of many single-cell commands.
- Validation does not catch every spreadsheet logic error; inspect formulas explicitly.

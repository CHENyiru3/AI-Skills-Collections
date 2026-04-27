---
name: officecli-xlsx
domain: documents
description: Use this skill any time a `.xlsx` file is involved, including creating spreadsheets, financial models, dashboards, trackers, or editing existing workbooks with formulas, charts, validations, and named ranges.
---

# OfficeCLI XLSX Skill

## First Check

```bash
command -v officecli
officecli --version
```

## Workflow

1. Inspect first: `view`, `get`, `query`
2. For new workbooks, read [creating.md](creating.md)
3. For existing workbooks, read [editing.md](editing.md)
4. Run QA: `view issues`, formula checks, `validate`

## Reading

```bash
officecli view data.xlsx text --start 1 --end 40 --cols A,B,C
officecli view data.xlsx outline
officecli view data.xlsx annotated
officecli view data.xlsx stats
officecli view data.xlsx issues
officecli get data.xlsx "/Sheet1/A1"
officecli query data.xlsx 'cell:has(formula)'
```

## Editing Rules

- Quote indexed paths in zsh: `"/Sheet1/row[1]"`
- Use formulas for calculated values instead of hardcoding results
- Use `officecli xlsx set cell` or `officecli xlsx add` before guessing properties
- Prefer batch mode for many cell updates
- Verify cross-sheet formulas after writing them

## QA

```bash
officecli view data.xlsx issues
officecli query data.xlsx 'cell:contains("#REF!")'
officecli query data.xlsx 'cell:contains("#DIV/0!")'
officecli validate data.xlsx
```

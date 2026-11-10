---
name: xlsx
domain: documents
description: Create, inspect or edit a spreadsheet artifact when workbook formulas, formatting, sheets or tabular-file contracts matter. Honor an explicitly chosen backend; not a universal router for database pipelines, live Excel or prose reports containing tables.
license: Proprietary. LICENSE.txt has complete terms
metadata:
  version: "1.0.1"
---

# Spreadsheet Files

Identify the workbook, requested sheets/ranges, output and chosen backend. Preserve
existing template conventions, formulas, charts, names, validation and workbook
features. For XLSM, links, pivots or advanced objects, select an engine that preserves
them; a generic read/write library may discard unsupported parts.

## Data and formula contracts

Keep IDs as strings when leading zeros matter; establish date/timezone, unit and
missing-value conventions. Excel indices are one-based, and a DataFrame header
changes the row offset. Verify sheet/range identity rather than assuming the active
sheet is the target. Do not insert/delete rows blindly when references depend on them.

Use formulas for a model that should update with user inputs. A static analysis
export can contain computed values; not every result needs a dynamic formula.
Keep assumptions/source provenance visible and preserve the requested precision.
Financial colors/negative-number conventions apply only when the brief/template
calls for them, not to all workbooks.

With openpyxl, load normally to preserve formula text. `data_only=True` reads cached
results and must not be saved over the formula-bearing workbook. openpyxl does not
calculate formulas; an existing cache may be stale, and a missing cache is not zero.
Pandas exports can replace a workbook rather than preserve its structure.

## Recalculation and validation

Choose an available calculation engine compatible with the workbook. Check changed
formulas and relevant dependencies, reference anchoring, units and meaningful edge
cases. Distinguish intentional/pre-existing error signals from new unintended errors;
never suppress a real error simply to achieve a zero-error count.

The optional helper operates on an XLSX working copy:

```bash
python scripts/recalc.py output.xlsx 30
```

It uses an isolated temporary LibreOffice profile, disables workbook macros and
external-link updates, confirms calculation/save completion and then replaces the
working copy. It does not modify the user's macro profile. Timeouts/failures leave
the input in place. It reports actual error cells and missing formula caches; a
recalculated LibreOffice workbook is not a guarantee of Excel feature compatibility.
Use a native/feature-preserving engine for unsupported formats or features.

Inspect saved formulas and representative calculated values independently of tool
status, and check changed layout/number formats when relevant. Report the engine,
checks, cache freshness and any unavailable recalculation. Stop at the scoped valid
spreadsheet; global tool installation and user macro changes are not prerequisites.

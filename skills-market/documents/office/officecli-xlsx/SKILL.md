---
name: officecli-xlsx
domain: documents
description: Inspect or edit XLSX through OfficeCLI when that backend is requested, selected by the project or already in use. Not a universal spreadsheet router or a requirement to recalculate unrelated workbook ranges.
metadata:
  version: "1.0.1"
---

# OfficeCLI XLSX

Discover installed OfficeCLI help, then inspect sheet names, affected ranges,
formulas and workbook features. Read [creating.md](creating.md) for a new workbook
or [editing.md](editing.md) for an existing one. Preserve formulas, named ranges,
validation, formats and the template outside the requested change.

Quote indexed paths such as `"/Sheet1/row[1]"`. Check actual cell property names
with `officecli xlsx set cell` before editing. Batch updates can help many cells;
resident mode is optional and must be flushed before inspecting the saved result.

Use formulas when the result should update with workbook inputs; static source
exports need not become dynamic models. Keep references, units and source facts
traceable. Check cross-sheet/relative references and distinguish formula text from
fresh calculated values; discover a suitable calculation engine if needed.

Validate affected formulas and their dependency ranges. Inspect new errors and
explain intentional error signals or pre-existing defects separately. `#REF!` or
`#DIV/0!` queries are useful leads but are not a complete formula audit. Check
structure and relevant visual output, then stop when the scoped workbook change
is valid. Do not alter user macros or install a calculation engine automatically.

---
name: obsidian-bases
domain: writing
description: Create or edit an Obsidian .base file with scoped filters, formulas and views. Use for Bases artifacts; not ordinary note properties, generic tabular analysis or automatic image hosting.
metadata:
  version: "1.0.1"
---

# Obsidian Bases

Inspect the vault's property conventions and an existing base before editing.
Preserve view names/configuration and unrelated formulas. Bases are YAML files,
but valid YAML alone does not establish that Obsidian supports a formula or view.
Check the installed Obsidian/plugin version when using version-sensitive features.

## Minimal structure

```yaml
filters:
  and:
    - 'file.ext == "md"'
    - 'file.hasTag("task")'
formulas:
  is_overdue: 'if(due, date(due) < today(), false)'
properties:
  formula.is_overdue:
    displayName: "Overdue"
views:
  - type: table
    name: "Tasks"
    order:
      - file.name
      - status
      - formula.is_overdue
```

Adapt property names and scope to real notes. Global filters apply to all views;
view-specific filters refine the selected view. Use a string expression or nested
`and`/`or`/`not` filter structures without confusing YAML syntax with formula syntax.
Quote expressions containing YAML punctuation, and escape nested quotes deliberately.

Distinguish note properties (`status` or `note.status`), file metadata (`file.name`)
and derived properties (`formula.is_overdue`). Define each referenced formula.
Guard missing values without confusing valid zero/false with absence. Date subtraction
returns a duration; check the installed version's supported duration fields before numeric arithmetic.
`this` changes with embedding/sidebar context, so test contextual filters there.

Configure only the requested views/order/grouping/summary. Cards/list/map support
can depend on application/plugins; do not install a community plugin just to satisfy
an example. Summary aggregation is distinct from a per-note formula.

Read [references/FUNCTIONS_REFERENCE.md](references/FUNCTIONS_REFERENCE.md) only
for needed function details and verify against the installed/current API. Embed a
base with `![[Name.base]]` or a named view with `![[Name.base#View Name]]` when wanted.
Online image intent does not select Imgur or authorize public uploads; honor the
chosen storage and privacy context.

Parse YAML, check property/formula references and inspect representative matching
and excluded notes. Open the base in the target Obsidian context when available;
report an unverified view honestly. Stop when the requested base behaves correctly.
Reference: [Bases syntax](https://help.obsidian.md/bases/syntax).

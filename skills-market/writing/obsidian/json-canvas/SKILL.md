---
name: json-canvas
domain: writing
description: Create or edit a JSON Canvas .canvas artifact with nodes, edges and layout. Use for an actual canvas file or explicit JSON Canvas workflow; not generic illustrations, HTML canvas code or automatic public image uploads.
metadata:
  version: "1.0.1"
---

# JSON Canvas

Read the current file and preserve existing IDs, content, paths, edges and visual
order outside the requested change. The top-level object can contain `nodes` and
`edges` arrays. Use a JSON serializer, not manual string concatenation.

## Node and edge contracts

Each node has a unique string `id`, a `type`, and integer `x`, `y`, `width`, `height`.
IDs need not be sixteen-character hex; that is a useful generation convention, not
a schema requirement. Preserve existing IDs rather than renumbering the graph.

| Node type | Specific fields |
| --- | --- |
| `text` | `text` string, with Markdown when wanted |
| `file` | `file` path; optional `subpath` beginning with `#` |
| `link` | `url` |
| `group` | optional `label`, `background`, `backgroundStyle` (`cover`, `ratio`, `repeat`) |

Node array order is visual stacking order, bottom first. Positions are top-left,
x right/y down, and negative coordinates are valid. Keep positive useful dimensions
and enough space for the actual content; fixed gutter/size tables are suggestions.
A group is a visual container, not a separate coordinate system for its children.

Edges have unique string IDs and valid `fromNode`/`toNode` references. Optional
`fromSide`/`toSide` are `top`, `right`, `bottom`, `left`; `fromEnd`/`toEnd` are
`none` or `arrow` (defaults none/arrow). Optional labels and colors preserve meaning.
Colors are hex strings or preset strings `"1"` through `"6"`; applications choose
the precise preset colors, so do not rely on an exact RGB mapping.

Use real newline characters in parsed text and let JSON encode them as `\n`.
Double-escaped `\\n` displays literal backslash/n. Resolve file paths in the
application/vault context and check heading/block subpaths when relevant. A remote
image request does not select a public hosting service; use the authorized URL/storage.

Read [references/EXAMPLES.md](references/EXAMPLES.md) only for a relevant complete
layout pattern. Treat sample IDs/paths as examples, not fixed identifiers.

After editing, parse JSON and check required type-specific fields, ID uniqueness,
edge endpoints and retained content. Inspect in the target app when layout matters;
a JSON parse does not prove previews or links load. Stop when the requested graph
change is valid and readable. Reference: [JSON Canvas 1.0](https://jsoncanvas.org/spec/1.0/).

---
name: officecli
domain: documents
description: Create, inspect, validate, and modify Office documents (.docx, .xlsx, .pptx) using the locally installed `officecli` binary. Use when the user wants to create, read, check formatting, find issues, add charts, or modify Office documents.
---

# officecli

Use the local binary at `~/.local/bin/officecli`.

## First Check

Before using the tool:

```bash
command -v officecli
officecli --version
```

If `officecli` is missing from `PATH`, use the absolute path:

```bash
$HOME/.local/bin/officecli --version
```

## Strategy

Prefer this progression:

1. L1 read: `view`, `get`, `query`, `validate`
2. L2 DOM edit: `set`, `add`, `remove`, `move`, `swap`, `batch`
3. L3 raw XML: `raw`, `raw-set`, `add-part`

Always add `--json` when structured output helps.

## Help System

When unsure about element names, paths, or properties, run help instead of guessing:

```bash
officecli pptx set
officecli pptx set shape
officecli pptx set shape.fill
officecli docx add
officecli xlsx get
```

## Core Commands

```bash
officecli create <file>
officecli view <file> <mode>
officecli get <file> <path> --depth N
officecli query <file> <selector>
officecli set <file> <path> --prop key=value
officecli add <file> <parent> --type <type> --prop key=value
officecli remove <file> <path>
officecli move <file> <path> --to <parent> --index N
officecli swap <file> <path1> <path2>
officecli validate <file>
officecli batch <file>
officecli raw <file> <part>
officecli raw-set <file> <part> --xpath "..." --action replace --xml '<xml/>'
```

## Performance

For 3 or more operations on one file, prefer resident mode:

```bash
officecli open file.docx
officecli set file.docx ...
officecli add file.docx ...
officecli close file.docx
```

For many edits, prefer batch mode:

```bash
cat <<'EOF' | officecli batch file.xlsx
[
  {"command":"set","path":"/Sheet1/A1","props":{"value":"Name","bold":"true"}}
]
EOF
```

## Validation

Before considering the document done:

```bash
officecli view file.docx issues
officecli validate file.docx
```

For large files, use targeted reads:

```bash
officecli view file.docx text --max-lines 100
officecli view file.xlsx text --start 1 --end 40 --cols A,B,C
officecli view file.pptx text --start 1 --end 5
```

## Specialized Skills

Use these more specific skills when the format is clear:

- `officecli-docx` for Word documents
- `officecli-pptx` for PowerPoint presentations
- `officecli-xlsx` for Excel workbooks

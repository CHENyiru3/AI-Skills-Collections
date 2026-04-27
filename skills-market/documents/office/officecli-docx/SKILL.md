---
name: officecli-docx
domain: documents
description: Use this skill any time a `.docx` file is involved, including creating Word documents, reports, letters, memos, proposals, or editing existing documents with tables, headers, footers, and comments.
---

# OfficeCLI DOCX Skill

## First Check

```bash
command -v officecli
officecli --version
```

## Workflow

1. Inspect first: `view`, `get`, `query`
2. For existing docs, read [editing.md](editing.md)
3. For new docs, read [creating.md](creating.md)
4. Run QA: `view issues`, `view outline`, `validate`

## Reading

```bash
officecli view doc.docx text --max-lines 200
officecli view doc.docx outline
officecli view doc.docx annotated
officecli view doc.docx stats
officecli view doc.docx issues
officecli get doc.docx /body --depth 1
officecli query doc.docx 'paragraph[style=Heading1]'
```

## Editing Rules

- Quote indexed paths in zsh: `"/body/p[1]"`
- Use paragraph spacing, not empty paragraphs, for layout
- Define or reuse styles instead of spraying inline formatting everywhere
- Run `officecli docx set paragraph` or `officecli docx add` before guessing properties
- For 3+ operations, prefer `open`/`close` or `batch`

## QA

```bash
officecli view doc.docx issues
officecli query doc.docx 'p:empty'
officecli query doc.docx 'image:no-alt'
officecli validate doc.docx
```

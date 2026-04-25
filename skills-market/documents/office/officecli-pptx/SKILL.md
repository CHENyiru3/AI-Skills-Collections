---
name: officecli-pptx
description: Use this skill any time a `.pptx` file is involved, including creating slide decks, presentations, or editing existing presentations with charts, tables, images, animations, and notes.
---

# OfficeCLI PPTX Skill

## First Check

```bash
command -v officecli
officecli --version
```

## Workflow

1. Inspect first: `view`, `get`, `query`
2. For new decks, read [creating.md](creating.md)
3. For existing decks, read [editing.md](editing.md)
4. Run QA with `view issues`, visual preview, and `validate`

## Reading

```bash
officecli view slides.pptx text --start 1 --end 5
officecli view slides.pptx outline
officecli view slides.pptx annotated
officecli view slides.pptx stats
officecli view slides.pptx issues
officecli get slides.pptx /slide[1] --depth 1
officecli query slides.pptx 'shape:contains("Revenue")'
```

## Editing Rules

- Quote indexed paths in zsh: `"/slide[1]/shape[1]"`
- Use `layout=blank` for custom-designed slides
- Re-query slide contents after z-order changes because shape indices can shift
- Use `officecli pptx set shape` or `officecli pptx add` before guessing properties
- Prefer `html` preview for multi-slide QA

## QA

```bash
officecli view slides.pptx issues
officecli view slides.pptx html --browser
officecli validate slides.pptx
```

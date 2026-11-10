---
name: obsidian-markdown
domain: writing
description: Create or edit Obsidian-specific Markdown links, embeds, callouts or properties in a vault note. Use when these extensions matter; not ordinary Markdown outside a vault or a requirement to add metadata/callouts to every note.
metadata:
  version: "1.0.1"
---

# Obsidian Markdown

Read the current note and vault conventions before changing structure. Preserve
frontmatter types, note identity, aliases, backlinks and the existing link style.
Wikilinks and Markdown links can both be valid internal links; do not rewrite a
vault's conventions solely to satisfy a generic preference.

| Purpose | Syntax example |
| --- | --- |
| Note/display text | `[[Note]]`, `[[Note|Label]]` |
| Heading/block | `[[Note#Heading]]`, `[[Note#^block-id]]` |
| Embed | `![[Note#Heading]]`, `![[image.png|300]]` |
| PDF page | `![[document.pdf#page=3]]` |
| Highlight/comment | `==text==`, `%%hidden comment%%` |

A paragraph block ID is appended as `^block-id`; lists/quotes may need a separate
ID line after the block. Check that target names/headings/IDs really exist and
resolve ambiguities when duplicate note names are present. Hidden comments are
still plaintext in the source, not a privacy mechanism.

Use callouts only when useful: `> [!note]` or `> [!warning] Title`, with `-`/`+`
for collapsible state where supported. Preserve quoted content and indentation.
Read [CALLOUTS.md](references/CALLOUTS.md) for nested/custom variants,
[EMBEDS.md](references/EMBEDS.md) for a needed media type, and
[PROPERTIES.md](references/PROPERTIES.md) for property/date/tag semantics.

New notes should follow the vault's schema; title/tags/aliases/callouts are not
universal requirements. Keep YAML parseable and preserve dates/strings as intended.
Use the vault's math/Mermaid support only when needed and verify the rendered syntax.
External image intent does not choose Imgur or authorize publishing private assets.

Check changed links, frontmatter and relevant reading-view rendering. Stop when
the requested note edit is correct; do not reorganize the vault or update unrelated
navigation merely because the file lives in Obsidian.

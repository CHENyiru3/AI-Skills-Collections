---
name: obsidian-cli
domain: writing
description: Use a configured Obsidian CLI for a requested vault operation or Obsidian plugin/theme debugging. Target an explicit vault/file; not a requirement to launch the app or use CLI for every local Markdown edit.
metadata:
  version: "1.0.1"
---

# Obsidian CLI

Discover the installed `obsidian help` contract and application availability.
CLI behavior changes with version; use command-specific help rather than guessing.
Choose the target vault explicitly as the first parameter, especially before a
mutation. Defaults can depend on the current directory or active vault/file.

```bash
obsidian vault="My Vault" read path="folder/note.md"
obsidian vault="My Vault" search query="search term" limit=10
```

Use `path=` for an exact vault-relative target when name resolution is ambiguous;
`file=` follows wikilink-like lookup. Quote spaces and shell-sensitive content.
Multiline CLI text uses supported `\n`/`\t` escapes; check saved content rather than
assuming shell quoting produced the intended newlines.

Read before writing, preserve current author edits and choose a non-overwriting
create operation by default. Use `overwrite`, permanent deletion, clipboard copying,
plugin reload or arbitrary app-context eval only for their named, authorized task.
A query should not alter the active note or publish images through a chosen service.

For plugin/theme debugging, reload only the target plugin and inspect its errors,
console and relevant DOM/rendering. Restore task-created debug state when needed;
do not change global appearance or other plugins to validate a local edit.

Verify the actual target/result, not just command status. Report unavailable app/CLI
capabilities and use another suitable path when allowed. Stop at the requested vault
operation. Reference: [Obsidian CLI](https://help.obsidian.md/cli).

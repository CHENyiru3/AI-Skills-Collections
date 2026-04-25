# Vault Discovery Checklist

Use this checklist before making structural or factual edits.

## Schema and contracts

- Find `AGENTS.md` or equivalent schema files.
- Identify whether `index.md`, `log.md`, and `inbox.md` are required contracts.
- Check for workflow docs, templates, and naming rules.

## Layout

- Map top-level folders such as `raw/`, `wiki/`, `templates/`, `.obsidian/`.
- Identify first-class page families and any semantic subfolders.
- Check whether legacy areas are still active or compatibility-only.

## Page model

- Inspect frontmatter shape on a few canonical pages.
- Inspect heading/body structure on a few canonical pages.
- Check how references are stored: inline links, source pages, or both.

## Source discipline

- Determine whether raw sources are immutable.
- Determine how new sources are registered.
- Check whether web enrichment is mandatory, optional, or disallowed.

## Navigation discipline

- Check whether new pages must be added to `index.md`.
- Check whether edits must be recorded in `log.md`.
- Check whether unresolved questions belong in `inbox.md`.

## Structural hazards

- Find path-based links that will break on moves.
- Check for duplicate page names in different folders.
- Check for folders that are intentionally flat.

## Protected boundaries

- Identify read-only upstreams or external reference repos.
- Confirm the writable scope before editing.

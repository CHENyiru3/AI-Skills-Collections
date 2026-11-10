---
name: wiki-keeper
domain: writing
description: Query, ingest, reorganize or lint a Markdown wiki/Obsidian vault while preserving its schema, canonical pages and links. Ordinary queries are read-only; index/log/inbox updates follow the actual mutation and vault contract.
metadata:
  version: "1.0.1"
---

# Wiki Keeper

Inspect the target vault, applicable AGENTS/schema files, navigation and a few
representative canonical pages. Map only the folders/page families needed for the
request, including protected/raw layers and existing link/property conventions.
Use [vault-discovery-checklist.md](references/vault-discovery-checklist.md) when
substantial structure is unfamiliar; it is not mandatory ceremony for a known note.

## Choose the requested mode

- **Query:** answer from canonical pages and trace sources as needed. Remain read-only
  unless the user requested saving or an applicable vault contract requires it.
- **Ingest:** preserve source provenance, integrate supported facts into the right
  durable pages, and distinguish contradictions/missing evidence from new facts.
- **Reorganize:** preserve identities/content and update affected links/navigation
  with the moves. Do not restructure unrelated page families.
- **Lint:** report concrete stale links, schema drift, duplicate subjects or evidence
  gaps. Findings do not automatically authorize repairs or deleting shallow pages.

Prefer existing canonical targets over duplicate pages. Follow the vault's threshold
for new entity/event pages rather than imposing a universal taxonomy. Treat raw
sources as immutable when that is the vault contract; a new source does not justify
rewriting unrelated narrative or inferring private facts.

For a content mutation, update indexes/logs/inbox only where the actual change and
local convention require it. One fact does not automatically require touching every
related person/theme/page. Read [maintenance-loop.md](references/maintenance-loop.md)
for a relevant larger operation, keeping optional opportunities out of acceptance.

Verify affected frontmatter, link targets, page placement and navigation after moves.
Protect manually edited/shared targets against intervening changes when replacing
content. Report the useful result, implemented changes and unresolved evidence gaps
at the task's scale. Stop when the scoped answer or graph change is complete; no
seven-part report or automatic query write-back is required.

---
name: wiki-keeper
domain: writing
description: Maintain markdown wiki and Obsidian vault repositories safely and consistently. Use when the user wants to build, reorganize, ingest into, query against, or lint a markdown wiki, personal knowledge base, second brain, or Obsidian vault. Inspect the vault first, read local schema files such as AGENTS.md, preserve canonical pages and cross-links, and keep index/log/inbox style support files in sync with content updates.
---

# Wiki Keeper

`wiki-keeper` is a direct maintenance skill for markdown wiki repositories.
It borrows the inspect-first discipline from `page-keeper`, but adapts it to
vaults where markdown pages, navigation files, source layers, and local schema
files must stay coherent over time.

## When To Use

Use this skill when the task involves any of the following:

- Obsidian vault maintenance
- markdown wiki or personal knowledge base design
- ingesting sources into a wiki
- creating or refining page families and folder taxonomy
- adding or updating canonical pages
- updating `index.md`, `log.md`, `inbox.md`, or workflow docs
- linting a wiki for orphan pages, stale claims, weak links, or schema drift

## First Moves

1. Inspect the vault before editing.
2. Read local schema and navigation files first:
   - `AGENTS.md`
   - `index.md`
   - `log.md`
   - `inbox.md`
   - `templates/`
   - workflow docs under the operations area, if present
3. Build a compact vault map:
   - writable area
   - raw/source layer
   - derived wiki layer
   - page families and semantic subfolders
   - frontmatter and body conventions
4. Separate inferred rules from user-only rules.
5. Ask only blocking, high-impact questions.

For the inspection checklist, read
`references/vault-discovery-checklist.md`.

## Default Workflow

### 1. Inspect the vault

- Locate top-level contracts such as `AGENTS.md`, `index.md`, `log.md`,
  `inbox.md`, `raw/`, `wiki/`, `templates/`, and `.obsidian/`.
- Identify page families and subfolder rules before inventing new pages.
- Sample a few canonical pages in each family to learn the page contract.

### 2. Choose durable targets

Prefer enduring subjects over transient notes:

- canonical entity pages over repeated mentions
- period/theme/thread/knowledge/work pages over isolated event pages
- map and navigation pages over ad hoc chat-only summaries

### 3. Preserve source discipline

- Keep raw sources immutable when the vault treats them as immutable.
- Register new sources the way the vault expects.
- If the vault requires web enrichment, do it before finalizing fact-bearing
  pages.
- Treat external search as reference input, not silent truth.

### 4. Edit as a graph

One new source or one new fact usually touches more than one file. Update the
graph, not only the local page.

Common touches:

- the target canonical page
- connected people, places, themes, threads, knowledge pages, or works
- `index.md` if inventory or one-line summaries changed
- `log.md` with a chronological record
- `inbox.md` for unresolved gaps or follow-up tasks

### 5. Verify

- internal wikilinks still resolve
- frontmatter remains valid
- page placement matches folder taxonomy
- navigation files reflect additions, moves, or reframes
- no stale old paths remain after restructures

For the maintenance loop, read `references/maintenance-loop.md`.

## Editing Rules

- Prefer one canonical page per enduring subject.
- Create standalone pages for important named people, places, institutions,
  works, or recurring concepts when the vault benefits from independent identity
  and connections.
- Do not create event pages by default.
- Respect the vault's taxonomy even if a flatter structure seems simpler.
- If the vault already defines a page contract, follow it instead of inventing a
  new one.
- Keep Obsidian-compatible markdown consistent with existing repo style.
- Do not touch protected upstreams unless the user explicitly asks.

## Query, Ingest, and Lint Modes

### Ingest

Read source, identify touched durable pages, update those pages, update
navigation files, then record follow-ups.

### Query

Answer from existing canonical pages first. Read source pages only as needed for
grounding. File reusable syntheses back into the wiki when they have long-term
value.

### Lint

Check for orphans, duplicate subjects, missing links, stale claims, missing
references, shallow stubs, misplaced files, and schema drift.

## Output Contract

When using `wiki-keeper`, structure the response around:

1. `Vault assessment`
2. `Discovered rules`
3. `Questions for the user` only if blocking
4. `Edit plan`
5. `Implemented updates`
6. `Verification`
7. `Open follow-ups`

## Safety Boundaries

- Do not infer private facts when the vault does not support them.
- Do not rewrite large narrative sections just because a new source exists;
  integrate surgically unless the user asks for a rewrite.
- Do not move large families of files without updating navigation and links.
- Do not treat formatting inconsistencies as mistakes until the repo pattern is
  clear.
- Do not let chat-only syntheses remain unfiled when the vault is meant to
  compound knowledge.

## Common Vault Patterns To Recognize

- raw/source layer vs derived wiki layer
- chronological spine vs conceptual spine
- map and index pages
- entity pages
- source registry or legacy source folders
- templates for page families
- append-only activity log
- inbox or unresolved-questions queue
- web-enrichment policies
- repo-local schema in `AGENTS.md`

## Example Prompts

**Example 1**
User: "Ingest this new article into my Obsidian wiki and update the affected
pages."

**Example 2**
User: "Reorganize the People and Themes folders in this markdown wiki without
breaking links."

**Example 3**
User: "Lint this personal wiki for orphan pages, missing references, and stale
claims."

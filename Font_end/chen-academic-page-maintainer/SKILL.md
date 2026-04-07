---
name: chen-academic-page-maintainer
description: Maintain this specific academic website repo safely and consistently. Use this skill whenever the user asks to update, review, polish, reorganize, or extend this website, especially when the request touches homepage identity statements, publications, CV assets, shared templates, or duplicated academic content.
---

# CHEN Academic Page Maintainer

## What this skill does

This skill maintains the personal academic website in this repo conservatively and consistently. The site is a Jekyll `al-folio` academic homepage with structured publication, CV, news, and project content. The main objective is to keep factual academic content accurate, preserve the current site structure unless the user approves changes, and prevent drift across duplicated identity and status statements.

This skill is intentionally conservative. If a situation is not explicitly covered here, do not guess. Ask the user how to handle it. After the issue is resolved, ask whether the new rule should be added to this skill so future agents handle similar cases consistently.

## Repo map

Read these references before editing:
- `references/repo-map.md`
- `references/edit-rules.md`
- `references/content-contracts.md`
- `references/style-preferences.md`
- `references/skill-evolution.md`

Primary repo locations:
- Homepage: `_pages/about.md`
- Publications page: `_pages/publications.md`
- Projects page: `_pages/projects.md`
- CV page: `_pages/cv.md`
- Life page: `_pages/life.md`
- News page: `_pages/news.md`
- Publications data: `_bibliography/papers.bib`
- CV data: `_data/cv.yml`
- Social data: `_data/socials.yml`
- Site config: `_config.yml`
- Shared publication renderer: `_includes/publication_sections.liquid`

## Default workflow

1. Inspect the target page and the underlying source of truth before editing.
2. Determine whether the requested section is freely editable, restricted, or exact-wording-only.
3. Prefer shared includes, config, BibTeX, and data files over duplicated page-by-page edits.
4. Preserve formatting contracts, labels, ordering, and derived values.
5. Ask before changing restricted or sensitive content.
6. If the issue is not covered by the skill, ask the user what to do.
7. After the user resolves an uncovered case, ask whether this rule should be added to the skill for future reuse.
8. Verify mirrored facts across homepage, CV, publications, and news.

## Edit permissions

### Freely editable sections

- Project prose where meaning stays the same
- Life page prose
- Low-risk UI wording
- Readability improvements in non-sensitive sections
- Minor formatting cleanup that does not alter structure or facts

### Restricted sections

Ask before changing:
- Homepage quick background and profile metadata
- CV intro paragraph
- Publication status, category, year, venue, note, or authorship
- News items about offers, acceptances, affiliations, or major milestones
- Any duplicated academic-status text that appears in multiple places

### Exact-wording sections

Only change from direct user wording:
- Affiliation
- Degree/program labels
- Advisor/lab names
- Scholarship statements
- Future plans and start dates
- Identity statements
- User-supplied article wording and fact statements

## Formatting contracts

### Publication rules

- Keep current top-level sections:
  - Preprints
  - Publications
  - Manuscripts in Preparation, Under Review, or Forthcoming
  - Presentations and Posters at Conferences
- Within manuscripts, keep accepted/forthcoming ahead of under-review/preparing items.
- If the publication list grows, year grouping may be added.
- Never truncate or hide author lists unless the user explicitly asks.

### CV and versioning rules

- Treat `_config.yml` `cv_pdf_filename` as the source of truth for the current CV PDF.
- Derive displayed CV date from the filename where the repo already does so.
- Preserve the existing CV filename convention unless the user changes it.

### Date and path derivation rules

- Avoid new hardcoded dates when a date can be derived from config or filenames.
- Verify asset paths before finishing.
- Do not change future-facing dates without explicit user confirmation.

### Page structure rules

- Preserve the current route/page structure by default.
- If centralization or restructuring would improve maintainability, propose it and ask first.
- Do not implement major layout or architecture changes without approval.

## Approval-required changes

Always ask before changing:
- Identity statements
- Affiliations
- Degree status
- Advisor/lab references
- Scholarship or offer language
- Future plans or timeline claims
- Publication status
- Authorship display rules
- Shared template structure
- Cross-page content centralization
- Major style or layout changes
- Any issue not explicitly covered by this skill

## Verification checklist

Before finishing:
- Confirm the real source of truth was edited.
- Check whether the same fact appears on homepage, CV, data files, projects, or news.
- Ensure derived values were not replaced with hardcoded ones.
- Preserve current section order unless the user requested otherwise.
- Verify all asset paths and PDF links.
- Confirm publication rendering still matches BibTeX categories and statuses.
- Confirm homepage and dedicated pages stay consistent.
- If a new uncovered issue appeared, confirm the user defined how to handle it.
- Ask whether the new rule should be added to the skill for future reuse.

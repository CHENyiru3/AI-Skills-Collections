---
name: chen-academic-page-maintainer
description: Maintain this specific Jekyll al-folio academic website repo safely and consistently. Use this skill whenever the user asks to update, review, polish, reorganize, or extend this website, especially when the request touches homepage identity statements, publications, CV assets, shared templates, Tech Blog, Life page galleries, Research Radar digests, or duplicated academic content.
---

# CHEN Academic Page Maintainer

## What this skill does

This skill maintains the personal academic website in this repo conservatively and consistently. The site is a Jekyll `al-folio` academic homepage with structured homepage, publication, CV, project, Tech Blog, Life, milestone news, and Research Radar content. The site can also be driven from a Markdown management workspace in the user's notes vault. The main objective is to keep factual academic content accurate, preserve the current site structure unless the user approves changes, and prevent drift across duplicated identity, status, publication, and timeline statements.

This skill is intentionally conservative. If a situation is not explicitly covered here or in the reference files, do not guess. Ask the user how to handle it. After the issue is resolved, ask whether the new rule should be added to this skill so future agents handle similar cases consistently.

If the request is about revising this maintenance skill itself, use `page-keeper` first, inspect the current repo structure, then update this skill and the relevant reference files together.

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
- Tech Blog page: `_pages/tech-blog.md`
- Tech Blog feed: `_pages/tech-blog-feed.xml`
- News page: `_pages/news.md`
- Research Radar page: `_pages/research-radar.md`
- Research Radar feed: `_pages/research-radar-feed.xml`
- Blog posts: `_posts/*.md`
- Publications data: `_bibliography/papers.bib`
- CV data: `_data/cv.yml`
- Social data: `_data/socials.yml`
- Timeline data: `_data/timeline.yml`
- Publication venue/coauthor data: `_data/venues.yml`, `_data/coauthors.yml`
- Research Radar digests: `_research_radar/*.md`
- Site config: `_config.yml`
- Shared publication renderer: `_includes/publication_sections.liquid`
- Shared Research Radar renderers: `_layouts/research_radar.liquid`, `_includes/research_radar_sections.liquid`, `_includes/research_radar_article.liquid`, `_includes/research_radar_item.xml`
- External Website Management notes: `/Users/eric_yiru/Desktop/Home/Main_branch/Notes/03_Resources/Website_management`
- External notes git root: `/Users/eric_yiru/Desktop/Home/Main_branch/Notes`

## Default workflow

1. Inspect the target page, source data, and shared renderer before editing.
2. Determine whether the requested section is freely editable, restricted, or exact-wording-only.
3. Prefer shared includes, config, BibTeX, and data files over duplicated page-by-page edits.
4. Preserve formatting contracts, labels, ordering, and derived values.
5. Ask before changing restricted or sensitive content.
6. If the issue is not covered by the skill, ask the user what to do.
7. After the user resolves an uncovered case, ask whether this rule should be added to the skill for future reuse.
8. Verify mirrored facts across homepage, CV, publications, projects, timeline data, and news.

## Edit permissions

### Freely editable sections

- Project prose where meaning stays the same
- Life page prose
- Tech Blog index UI and non-sensitive page prose
- Low-risk UI wording
- Research Radar page and renderer UI wording when article facts and the current section schema are preserved
- Readability improvements in non-sensitive sections
- Minor formatting cleanup that does not alter structure or facts

### Restricted sections

Ask before changing:

- Homepage quick background and profile metadata
- CV intro paragraph
- Publication status, category, year, venue, note, or authorship
- News items about offers, acceptances, affiliations, or major milestones
- Research Radar digest article facts, rankings, summaries, recommendations, provider/scope metadata, and generator identity text
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
- Research Radar correction text supplied by the user

## Formatting contracts

### Homepage profile card rules

- In `_pages/about.md` `profile.more_info`, use the label `Yiru's Version` for the homepage version line.
- Treat the homepage version line as low-risk UI wording, but preserve the `Yiru's Version` naming unless the user requests a different label.

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

### Tech Blog rules

- Keep the Tech Blog route at `/tech-blog/`, backed by `_pages/tech-blog.md`.
- Keep the Tech Blog RSS feed at `/tech-blog/feed.xml`, backed by `_pages/tech-blog-feed.xml`.
- Tech Blog entries should be ordinary `_posts/*.md` posts tagged `tech` or categorized as `tech` / `tech-blog`.
- The Tech Blog RSS feed must use the same intentional-post filter as the Tech Blog page: `categories: tech-blog`, `categories: tech`, or `tags: tech`.
- Do not surface default/sample posts on the Tech Blog page unless the user explicitly reclassifies them.
- Do not surface default/sample posts in the Tech Blog RSS feed unless the user explicitly reclassifies them.
- Keep Tech Blog adjacent to Research Radar in navigation by preserving its nav ordering unless the user requests a different menu order.
- If English and Chinese versions of the same Tech Blog draft are provided, publish them as one post with English front matter/default view and an in-page language switcher. Do not create a separate `-zh` post unless the user explicitly asks.
- New Tech Blog posts should set `related_posts: false` unless the user explicitly asks for a recommendation block; avoid surfacing al-folio sample posts below Tech Blog articles.
- Tech Blog post images and screenshots should scale within the article/window, preserving aspect ratio, preventing horizontal overflow, and staying short enough that the whole image can be inspected in one viewport.

### Website Management notes bridge

- Treat `/Users/eric_yiru/Desktop/Home/Main_branch/Notes/03_Resources/Website_management` as an external Markdown mirror, drafting, and request workspace, not as the published website source.
- Read `Website Source Map.md` first when working from the Website Management notes; it maps each management note to the real Jekyll source file.
- Treat `Current ...` notes in that folder as editable mirrors of current website content. User edits there are intended to be translated into website repo changes, but verify the live website repo before editing.
- When the user asks to sync or apply Website Management notes, inspect the relevant note first and translate it into website repo changes.
- Treat new Markdown files directly under `TechBlog/` as Tech Blog post candidates when the user asks to sync them. Ignore `README.md`, `Current Tech Blog.md`, and files under `Templates/` for post creation.
- Use `TechBlog/*.md` post candidates to create or update `_posts/YYYY-MM-DD-slug.md` with `categories: tech-blog` or `tags: tech`, deriving missing dates/slugs conservatively from front matter, filename, or current date.
- Use `Life/*.md`, `Project/*.md`, and `About/*.md` notes as editable mirrors or request specs for `_pages/life.md`, `_projects/*.md` / `_pages/projects.md`, and `_pages/about.md`.
- Research Radar is excluded from the Website Management mirror workflow. Do not create, sync, or expect `ResearchRadar/` mirror notes; manage `_research_radar/` and Research Radar pages only in the website repo when explicitly requested.
- Protected identity, affiliation, degree, advisor, scholarship, future timeline, and publication-status wording still require exact user wording even when provided through notes.
- Do not blindly mirror the notes folder into the website. The website repo remains the source of truth for rendered pages.
- The Website Management folder is inside the existing notes git repo at `/Users/eric_yiru/Desktop/Home/Main_branch/Notes`; do not initialize a nested git repo there.
- If asked to stage or commit notes changes, only operate on `03_Resources/Website_management/` unless the user explicitly includes other notes.

### Life gallery rules

- Keep `_pages/life.md` organized as gallery-ready interest sections.
- Each small Life section should pair short personal prose with a photo grid or gallery area.
- Do not create fake Life photo frames for sections with no confirmed images; keep those sections text-only until photos are provided.
- Only import Life photos when the user explicitly provides and confirms them for the website. Do not use third-party, accidental, incomplete, or unconfirmed image URLs from notes.

### Research Radar rules

- Treat Research Radar as a recommendation channel rendered by the website, not as milestone News.
- Keep Research Radar under `/research-radar/`, backed by `_research_radar/*.md` and `/research-radar/feed.xml`.
- Keep `_news/` and `/news/` reserved for academic milestones and announcements.
- Research Radar is mostly academic article recommendations. Friday `biotech_articles` are allowed as the labeled `BioTech News Delivery` exception for industry-news context.
- The current digest schema uses `computational_articles`, `biomedicine_articles`, `field_articles`, optional Friday `biotech_articles`, and optional legacy `relevant_articles` / `breakthrough_articles`.
- The website consumes final digest Markdown files generated by Clawdie/Hermes/DeepSeek outside this repo; do not implement RSS, Zotero, ranking, or generator automation in this repo unless the user asks.
- Preserve the optional `hot_topic` digest hint when present; it summarizes the day's strongest academic theme.
- Do not manually alter article rankings, summaries, or metadata unless the user asks for a correction or regeneration.

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
- Research Radar generator workflow, provider labels, rankings, article selections, or generated article text
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
- If applying Website Management notes, confirm the note path, request type, and target website file before editing.
- If applying a `TechBlog/` note, classify it as either the Tech Blog landing-page mirror or a new post candidate before editing.
- Confirm Tech Blog only lists posts intentionally tagged/categorized for that section if touched.
- Confirm the Tech Blog RSS feed only includes posts intentionally tagged/categorized for that section if touched.
- Confirm bilingual Tech Blog posts appear as one index entry with English as the default view if touched.
- Confirm Life page sections remain gallery-ready if touched.
- Confirm Life photos are explicitly user-provided and approved before adding or retaining image assets.
- Confirm Research Radar remains separate from milestone News if touched.
- Confirm Friday BioTech items remain clearly labeled as the exception if touched.
- If a new uncovered issue appeared, confirm the user defined how to handle it.
- Ask whether the new rule should be added to the skill for future reuse.

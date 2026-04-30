---
name: chen-academic-page-maintainer
description: Maintain this specific academic website repo safely and consistently. Use this skill whenever the user asks to update, review, polish, reorganize, or extend this website, especially when the request touches homepage identity statements, publications, CV assets, shared templates, or duplicated academic content.
---

# CHEN Academic Page Maintainer

## What this skill does

This skill maintains the personal academic website in this repo conservatively and consistently. The site is a Jekyll `al-folio` academic homepage with structured publication, CV, news, and project content. The main objective is to keep factual academic content accurate, preserve the current site structure unless the user approves changes, and prevent drift across duplicated identity and status statements.

This skill is intentionally conservative. If a situation is not explicitly covered here, do not guess. Ask the user how to handle it. After the issue is resolved, ask whether the new rule should be added to this skill so future agents handle similar cases consistently.

## Repo map

Read these references before editing. They are skill-local files — load them with `skill_view(name='chen-academic-page-maintainer', file_path='references/...')`. Do NOT use `read_file` with a bare relative path; that will resolve against the working directory and fail in cron/workdir contexts.
- `references/repo-map.md`
- `references/edit-rules.md`
- `references/content-contracts.md`
- `references/style-preferences.md`
- `references/skill-evolution.md`

**Workdir note:** When running as a cron job with a specific workdir, these reference files must exist in `<workdir>/references/` — not just in the skill directory. Cron agents resolve relative paths against the workdir. Copy them from `~/.hermes/skills/chen-academic-page-maintainer/references/` and add `references/` to the workdir's `.gitignore`.

Primary repo locations:
- Homepage: `_pages/about.md`
- Publications page: `_pages/publications.md`
- Projects page: `_pages/projects.md`
- CV page: `_pages/cv.md`
- Life page: `_pages/life.md`
- News page: `_pages/news.md`
- Research Radar page: `_pages/research-radar.md`
- Research Radar digests: `_research_radar/YYYY-MM-DD.md`
- Research Radar feed: `_pages/research-radar-feed.xml`
- Research Radar layouts: `_layouts/research_radar.liquid`, `_includes/research_radar_sections.liquid`, `_includes/research_radar_article.liquid`
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

## Research Radar maintenance

### Source discipline (critical)

- **Recommendations (articles in the digest)**: use ONLY unread RSS articles from NetNewsWire AOP feeds. Never use Zotero papers for recommendations — Boss already added those manually.
- **Hot topic signal**: use ONLY Zotero recent additions as a read-only pattern detector. Detect themes from what Boss is collecting, but do NOT expose private Zotero details.
- **Hallucination rule**: fewer real articles > made-up ones. Every paper must have a verified URL from RSS. Include DOI when available.

### NetNewsWire AOP feeds (query for unread articles)

NNW database: `~/Library/Containers/com.ranchero.NetNewsWire-Evergreen/Data/Library/Application Support/NetNewsWire/Accounts/OnMyMac/DB.sqlite3`

AOP feed IDs (used as `feedID` in `articles` table):
- `https://www.cell.com/cell/inpress.rss` — Cell
- `https://www.cell.com/cell-systems/inpress.rss` — Cell Systems
- `https://www.nature.com/nbt/journal/vaop/ncurrent/rss.rdf` — Nature Biotechnology
- `https://www.nature.com/ng/journal/vaop/ncurrent/rss.rdf` — Nature Genetics
- `https://www.nature.com/ni/journal/vaop/ncurrent/rss.rdf` — Nature Immunology
- `https://www.nature.com/nm/journal/vaop/ncurrent/rss.rdf` — Nature Medicine
- `https://www.nature.com/nmeth/journal/vaop/ncurrent/rss.rdf` — Nature Methods
- `http://www.sciencemag.org/rss/current.xml` — Science

Filter by Boss's interests: spatial omics/transcriptomics/multi-omics, single-cell, computational immunology, tumor microenvironment, immunotherapy, CAR-T, macrophage/T cell biology, biomedical AI, foundation models, representation learning, bioinformatics methods, translational cancer biology.

### Digest structure

Each `_research_radar/YYYY-MM-DD.md` uses this YAML front matter with THREE article sections (counts are dynamic, 3-6 each — fewer is fine if signal is thin):

```yaml
layout: research_radar
title: "Research Radar — YYYY-MM-DD"
date: YYYY-MM-DD
generated_at: "YYYY-MM-DD HH:MM +0800"
provider: "DeepSeek-V4-Pro"
scope: "Academic articles only"
hot_topic:
  title: "Optional theme title"
  summary: "Optional 1-sentence summary"
  signals: ["Evidence signal 1", "Evidence signal 2"]
computational_articles:  # dynamic count, computational/AI/methods
  - rank: 1
    title: "..."
    authors: "First Author et al."
    source: "Journal"
    published: "YYYY-MM-DD"
    url: "https://..."
    doi: "10.xxxx/..."
    article_type: "research article"
    topics: ["topic1", "topic2"]
    recommendation: "READ FULL"
    summary: "One concise factual summary from RSS."
    why_it_matters: "Scientific significance."
    why_for_me: "Why relevant to Boss's interests."
biomedicine_articles:  # dynamic count, biomedical discoveries
  # same shape, items relevant to Boss's bio interests (can be experimental)
field_articles:  # dynamic count, AI-related breakthroughs from NON-biomedical fields
  # same shape, items must have an AI angle and come from outside biomedicine
  # (robotics, AI safety, AI+education, AI+physics, AI+climate, etc.)
```

The template (`_includes/research_radar_sections.liquid`) supports: `computational_articles`, `biomedicine_articles`, `field_articles` (current), plus legacy `relevant_articles` / `breakthrough_articles` for backward compatibility. Section headings are plain labels ("Computational", "Biomedicine", "Other Fields") — no "Top N" prefix; the count badge on the side shows the dynamic count.

No `zotero_candidate` field — Boss removed it. Do not include it in any new digest.

**Field type contract (critical for RSS feed and Jekyll build):**
Every article in any section MUST use these exact types:
- `doi`: string, NEVER null. Use `""` when no DOI available. Null dois cause Liquid `append` filter crashes in `research-radar-feed.xml`.
- `topics`: array, NEVER null. Use `[]` when no topics. Non-array topics crash Liquid `for` loops.
- All string fields: use empty string `""` for missing values, never `null` or omit the key.
- Abstract is optional but prefer `""` over null if absent.
Always run the null-doi and array-topics checks (see Post-generation workflow) before committing.

Computational articles must feature: deep learning, representation learning, graph neural networks, foundation models, algorithm development, computational biology tools, bioinformatics methods. Pure biology/experimental papers go in biomedicine_articles, never in computational_articles.

Other Fields (field_articles) must feature AI-related content from non-biomedical domains. The Science RSS feed is a good source — look for AI-related research articles, reviews, or editorials about AI in fields like robotics, physics, climate, materials, education, or policy. Exclude purely non-AI content (geology, primatology, astrophysics without AI angle).

### Post-generation workflow

After writing the digest:
1. Validate YAML: `python3 -c "import yaml; fm=yaml.safe_load(open('_research_radar/YYYY-MM-DD.md').read().split('---\\n',2)[1]); print(f'comp:{len(fm.get(\\\"computational_articles\\\",[]))} biomed:{len(fm.get(\\\"biomedicine_articles\\\",[]))} fields:{len(fm.get(\\\"field_articles\\\",[]))}')\"`
2. Check for null dois (MUST pass — causes Liquid build error): `python3 -c "import yaml; d=yaml.safe_load(open('_research_radar/YYYY-MM-DD.md').read().split('---\\n',2)[1]); bad=[(k,a['rank']) for k in ['computational_articles','biomedicine_articles','field_articles'] for a in d.get(k,[]) if a.get('doi') is None]; assert not bad, f'NULL dois: {bad}'; print('OK')"`
3. Check topics are arrays (MUST pass): `python3 -c "import yaml; d=yaml.safe_load(open('_research_radar/YYYY-MM-DD.md').read().split('---\\n',2)[1]); bad=[(k,a['rank']) for k in ['computational_articles','biomedicine_articles','field_articles'] for a in d.get(k,[]) if not isinstance(a.get('topics'),list)]; assert not bad, f'Non-array topics: {bad}'; print('OK')"`
4. Auto-format with prettier: `npx prettier --write "_includes/research_radar_sections.liquid" "_includes/research_radar_article.liquid" "_layouts/research_radar.liquid" "_pages/research-radar.md" "_pages/research-radar-feed.xml" "_includes/research_radar_item.xml" "_research_radar/YYYY-MM-DD.md"`
5. Git push: `git add _research_radar/YYYY-MM-DD.md && git commit -m "Research Radar: YYYY-MM-DD" && git push`. If prettier touched other files, `git add` those too — but only Research Radar files.
6. Never add/commit/push other files. Never touch `_news/`. Never mark NNW articles as read. Never edit Zotero.

### Strict exclusions

Never include: AI industry news, product announcements, blogs, newsletters, non-academic press releases, author corrections, publisher corrections, Research Radar's own RSS feed, or items without a verifiable source URL.

### Cron job reference

- Job ID: `bcd10b8825f3`, name: "Research Radar daily digest"
- Schedule: `0 11 * * *` (daily at 11:00 AM Asia/Shanghai)
- Provider: `deepseek` / Model: `deepseek-v4-pro`
- Workdir: `/Users/eric_yiru/Desktop/Github/CHENyiru3.github.io`
- Toolsets: `terminal`, `file`, `web`
- Preloads `chen-academic-page-maintainer` skill
- Deliver: `local` (output saved to `~/.hermes/cron/output/`)

When recreating or updating: keep the prompt under ~2000 chars (long prompts cause model truncation errors), explicitly set provider/model, include the three-section structure and AI-focused Other Fields requirement, and ensure git push is in the prompt.

### RSS feed synchronization and pitfalls

When the digest section keys change (e.g., `relevant_articles` → `computational_articles`), the RSS feed template at `_pages/research-radar-feed.xml` must also be updated. The template iterates over specific YAML keys to generate `<item>` entries. If a digest uses new keys that the feed template doesn't recognize, the feed will appear valid but contain zero items. Always check `feed.xml` output after restructuring digest keys.

**Liquid HTML-in-string pitfall**: Never embed HTML tags with attributes inside Liquid `append` chains in the feed template. The Jekyll Liquid parser interprets `<a href="...">` as template syntax, causing "wrong number of arguments" and "Unexpected character /" errors that break the entire GitHub Pages build. The fix: use a separate `_includes/research_radar_item.xml` file with flat text-only Liquid assignments, and use `{% include %}` from the feed template. The item include uses simple `{{ field | xml_escape }}` calls without HTML markup.

The item include file is at `_includes/research_radar_item.xml`. It handles article rendering via `{% include research_radar_item.xml article=article digest=digest section="SectionName" %}`.

---

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

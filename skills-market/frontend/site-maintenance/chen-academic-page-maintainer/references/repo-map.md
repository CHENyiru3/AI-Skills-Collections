# Repo Map

## Stack

- Framework: Jekyll
- Theme/base architecture: `al-folio`
- Templating: Liquid

## Main routes

- `/`: `_pages/about.md`
- `/publications/`: `_pages/publications.md`
- `/projects/`: `_pages/projects.md`
- `/cv/`: `_pages/cv.md`
- `/news/`: `_pages/news.md`
- `/life/`: `_pages/life.md`
- `/tech-blog/`: `_pages/tech-blog.md`
- `/tech-blog/feed.xml`: `_pages/tech-blog-feed.xml`
- `/research-radar/`: `_pages/research-radar.md`
- `/research-radar/feed.xml`: `_pages/research-radar-feed.xml`
- Blog posts, if enabled by navigation or links: `_posts/*.md`

## Shared renderers and layouts

- Homepage layout: `_layouts/about.liquid`
- Generic page layout: `_layouts/page.liquid`
- CV layout: `_layouts/cv.liquid`
- Publications renderer: `_includes/publication_sections.liquid`
- Projects cards: `_includes/projects.liquid`
- News renderer: `_includes/news.liquid`
- Research Radar renderers:
  - `_layouts/research_radar.liquid`
  - `_includes/research_radar_sections.liquid`
  - `_includes/research_radar_article.liquid`
  - `_includes/research_radar_item.xml`
- Social links: `_includes/social.liquid`
- CV/resume layout support: `_layouts/cv.liquid`, `_includes/cv/*.liquid`, `_includes/resume/*.liquid`
- Publication badge/coauthor rendering: `_layouts/bib.liquid`

Inspect shared renderers before editing repeated content on visible pages.

## Sources of truth

- Site-wide config and CV filename: `_config.yml`
- Publication metadata: `_bibliography/papers.bib`
- CV structured content: `_data/cv.yml`
- Social links: `_data/socials.yml`
- Publication venue styling: `_data/venues.yml`
- Publication coauthor links: `_data/coauthors.yml`
- Timeline data: `_data/timeline.yml` (present in repo; verify current rendering before relying on it)
- JSONResume asset and config: `assets/json/resume.json`, `_config.yml` `jekyll_get_json` / `jsonresume`
- Projects: `_projects/*.md`
- Tech Blog posts: `_posts/*.md` with `categories: tech-blog`, `categories: tech`, or `tags: tech`
- Tech Blog RSS feed: `_pages/tech-blog-feed.xml`, using the same intentional-post filter as `_pages/tech-blog.md`
- News items: `_news/*.md`
- Research Radar digests: `_research_radar/*.md`
- External Website Management notes: `/Users/eric_yiru/Desktop/Home/Main_branch/Notes/03_Resources/Website_management`
- External notes git root: `/Users/eric_yiru/Desktop/Home/Main_branch/Notes`

## Derived-value rules already present

- The CV PDF shown on the homepage and CV page is driven by `_config.yml` `cv_pdf_filename`.
- The displayed CV date is derived from the filename pattern `CHEN_Yiru_CV_YYYY.MM.DD.pdf`.
- Research Radar collection output is configured in `_config.yml` as `research_radar` with permalink `/research-radar/:name/`.

## Drift hotspots

- Academic status appears in several places:
  - `_pages/about.md`
  - `_pages/cv.md`
  - `_data/cv.yml`
  - `_news/*.md`
- Publication and project status can drift across:
  - `_bibliography/papers.bib`
  - `_projects/*.md`
  - `_data/cv.yml`
  - `_data/timeline.yml`
- Publication styling is duplicated between:
  - `_pages/about.md`
  - `_pages/publications.md`
- Project narratives may restate publication or status information already represented in `papers.bib`.
- Tech Blog uses the general blog post collection but filters out default/sample posts unless they are intentionally tagged or categorized for Tech Blog.
- Tech Blog RSS must keep the same filter as the Tech Blog landing page so sample/general posts do not appear in the feed.
- Life page uses local gallery-ready markup and CSS in `_pages/life.md`; keep photo placeholders and responsive behavior in sync when editing sections.
- Website Management notes are an external editable mirror and drafting bridge. They can request changes across About, Life, Project, Publications, CV, News, and Tech Blog, but website files remain the rendered source of truth.
- `Website_management/TechBlog/Current Tech Blog.md` mirrors the landing page; new Markdown files directly under `Website_management/TechBlog/` are post candidates when the user asks to sync them.
- Research Radar is intentionally not mirrored into Website Management notes; use the website repo for `_research_radar/` and Research Radar page/feed edits.
- Research Radar is separate from `_news/`; do not mix recommendation digests with milestone announcements.
- Research Radar currently supports academic categories plus a Friday `biotech_articles` exception. Keep that exception clearly labeled if touched.

## Section risk summary

- High risk:
  - homepage identity and future-facing academic status
  - CV intro and CV data
  - publication metadata and authorship
- Moderate risk:
  - news entries tied to milestones, acceptances, or affiliation changes
  - project status statements
- Research Radar risk:
  - renderer UI wording is lower risk
  - generated article selections, rankings, summaries, recommendation labels, provider/scope metadata, and generator identity text are restricted
- Lower risk:
  - life page prose
  - non-sensitive readability polish
  - Research Radar renderer/UI polish that preserves the current schema and generated article facts

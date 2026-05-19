# Content Contracts

## Publications

- Data source: `_bibliography/papers.bib`
- Shared renderer: `_includes/publication_sections.liquid`
- Bib entry rendering also consults `_layouts/bib.liquid`, `_data/venues.yml`, and `_data/coauthors.yml`.
- Current top-level grouping:
  - Preprints
  - Publications
  - Manuscripts in Preparation, Under Review, or Forthcoming
  - Presentations and Posters at Conferences
- Manuscripts keep accepted/forthcoming above under-review or preparing items.
- Year grouping may be added if the list grows.
- Never shorten or hide long author lists unless the user explicitly requests it.
- Keep publication categories and statuses consistent with project pages, CV data, timeline data, and milestone news.

## CV

- `cv_pdf_filename` in `_config.yml` is the source of truth for the current downloadable CV.
- The visible CV date should be derived from the PDF filename, not manually duplicated.
- Keep the filename convention `CHEN_Yiru_CV_YYYY.MM.DD.pdf` unless the user changes it.
- Treat `_data/cv.yml` as the source of truth for structured CV entries.

## Homepage

- `_pages/about.md` mixes narrative text, profile metadata, and publication rendering.
- In `_pages/about.md` `profile.more_info`, the homepage version line should use the label `Yiru's Version`.
- Treat identity, degree, affiliation, advisor, scholarship, and future-plan statements as protected.
- Check for duplicated facts in `_pages/cv.md`, `_data/cv.yml`, and `_news/*.md` before finalizing changes.

## Projects

- Source: `_projects/*.md`
- Keep each project as its own long-form page unless the user requests structural change.
- Be careful when editing status lines or publication references because they may mirror publication metadata elsewhere.
- `_pages/projects.md` also embeds poster and coursework assets directly. Verify those asset paths if this page is touched.

## Tech Blog

- Source page: `_pages/tech-blog.md`
- RSS feed: `_pages/tech-blog-feed.xml`, rendered at `/tech-blog/feed.xml`
- Post source: `_posts/*.md`
- External mirror/draft source: `/Users/eric_yiru/Desktop/Home/Main_branch/Notes/03_Resources/Website_management/TechBlog/*.md`
- The Tech Blog page should list only posts with `categories: tech-blog`, `categories: tech`, or `tags: tech`.
- The Tech Blog RSS feed should use the same intentional-post filter as the Tech Blog page.
- Keep the route `/tech-blog/` and navigation title `Tech Blog`.
- Keep a visible RSS subscribe link on the Tech Blog landing page when the feed exists.
- Keep Tech Blog adjacent to Research Radar in the nav order unless the user requests a different menu order.
- Default al-folio sample posts should not appear there unless the user intentionally retags or recategorizes them.
- New Markdown files directly under the external `TechBlog/` folder are post candidates when the user asks to sync them. Ignore `README.md`, `Current Tech Blog.md`, and template files.
- Paired English/Chinese Tech Blog drafts should become one `_posts/YYYY-MM-DD-slug.md` entry with English title/description/default view and an in-page English/Chinese switcher. Avoid duplicate language-specific index entries.
- Tech Blog posts should disable the related-post recommendation block with `related_posts: false` unless the user explicitly requests recommendations.
- Tech Blog post images and screenshots should be responsive to the article/window size, keep their original aspect ratio, avoid horizontal overflow, and stay short enough that the whole image can be inspected in one viewport.

## Life

- Source: `_pages/life.md`
- External mirror/draft source: `/Users/eric_yiru/Desktop/Home/Main_branch/Notes/03_Resources/Website_management/Life/*.md`
- Keep each interest section as short prose, adding a responsive photo grid only when that section has confirmed real photos.
- Do not create fake photo frames for sections with no confirmed images.
- When replacing placeholders with photos, verify image paths and preserve alt text / accessible labels.
- Only add or retain Life photo assets when the user explicitly provides and confirms those images for website use. Ignore third-party, accidental, incomplete, or unconfirmed image URLs in notes.

## Website Management Notes

- Path: `/Users/eric_yiru/Desktop/Home/Main_branch/Notes/03_Resources/Website_management`
- Git root: `/Users/eric_yiru/Desktop/Home/Main_branch/Notes`
- The notes workspace contains editable mirrors, guides, and templates for About, Life, Project, TechBlog, Publications, CV, and News requests.
- `Website Source Map.md` is the first-read routing table for mapping notes to website source files.
- `Current ...` notes are editable mirrors of current website content; verify the actual website repo before applying edits.
- Treat notes as user-authored drafts or change requests. Translate them into website repo edits rather than publishing notes directly.
- Research Radar is deliberately excluded from this mirror system; do not create or sync a `ResearchRadar/` notes mirror.
- Do not initialize a nested git repository inside `Website_management`.
- When staging notes changes, scope git commands to `03_Resources/Website_management/` to avoid unrelated notes-vault changes.

## News

- Source: `_news/*.md`
- Items can be inline or full posts.
- Milestone announcements are fact-sensitive and may affect homepage or CV consistency.

## Research Radar

- Sources:
  - Daily digest files: `_research_radar/*.md`
  - Index page: `_pages/research-radar.md`
  - RSS feed: `_pages/research-radar-feed.xml`
  - Renderers: `_layouts/research_radar.liquid`, `_includes/research_radar_sections.liquid`, `_includes/research_radar_article.liquid`
  - RSS item renderer: `_includes/research_radar_item.xml`
- Research Radar is a recommendation channel and must remain separate from milestone News.
- Keep the route `/research-radar/` and feed `/research-radar/feed.xml`.
- Digest files should use `layout: research_radar`.
- Current digest front matter may include:
  - `generated_at`
  - `provider`
  - `scope`
  - optional `hot_topic`
  - `computational_articles`
  - `biomedicine_articles`
  - `field_articles`
  - optional Friday `biotech_articles`
- Legacy digest fields are still rendered if present:
  - `relevant_articles`
  - `breakthrough_articles`
- The current visible sections are:
  - Computational
  - Biomedicine
  - Other Fields
  - BioTech News Delivery, only when `biotech_articles` are present
  - Top N Relevant Reads, only for legacy `relevant_articles`
  - Top N Field Breakthroughs, only for legacy `breakthrough_articles`
- Digest files may include an optional `hot_topic` object with `title`, `summary`, and `signals` to highlight the day's strongest academic theme.
- Each article item should include rank, title, authors, source, published date, URL, DOI when available, article type, topics, recommendation, summary, `why_it_matters`, `why_for_me`, and optional Zotero-candidate flag.
- The website renders final Markdown produced by an external Clawdie/Hermes/DeepSeek workflow. It does not perform RSS reading, Zotero inspection, ranking, or automation.
- Exclude AI industry news, product announcements, blogs, newsletters, policy commentary, and Research Radar's own RSS feed from regular academic categories.
- Allow Friday `biotech_articles` as a clearly labeled BioTech News Delivery exception for industry-news context.
- Do not manually alter article rankings, summaries, or metadata unless the user requests a correction or regeneration.

## Assets

- Verify referenced PDF, image, and poster paths before finishing.
- Prefer config- or content-driven asset references over duplicated hardcoded paths when the repo already supports derivation.

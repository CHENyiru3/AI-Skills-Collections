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

## Shared renderers and layouts

- Homepage layout: `_layouts/about.liquid`
- Generic page layout: `_layouts/page.liquid`
- CV layout: `_layouts/cv.liquid`
- Publications renderer: `_includes/publication_sections.liquid`
- Projects cards: `_includes/projects.liquid`
- News renderer: `_includes/news.liquid`
- Social links: `_includes/social.liquid`

Inspect shared renderers before editing repeated content on visible pages.

## Sources of truth

- Site-wide config and CV filename: `_config.yml`
- Publication metadata: `_bibliography/papers.bib`
- CV structured content: `_data/cv.yml`
- Social links: `_data/socials.yml`
- Projects: `_projects/*.md`
- News items: `_news/*.md`

## Derived-value rules already present

- The CV PDF shown on the homepage and CV page is driven by `_config.yml` `cv_pdf_filename`.
- The displayed CV date is derived from the filename pattern `CHEN_Yiru_CV_YYYY.MM.DD.pdf`.

## Drift hotspots

- Academic status appears in several places:
  - `_pages/about.md`
  - `_pages/cv.md`
  - `_data/cv.yml`
  - `_news/*.md`
- Publication styling is duplicated between:
  - `_pages/about.md`
  - `_pages/publications.md`
- Project narratives may restate publication or status information already represented in `papers.bib`.

## Section risk summary

- High risk:
  - homepage identity and future-facing academic status
  - CV intro and CV data
  - publication metadata and authorship
- Moderate risk:
  - news entries tied to milestones, acceptances, or affiliation changes
  - project status statements
- Lower risk:
  - life page prose
  - non-sensitive readability polish

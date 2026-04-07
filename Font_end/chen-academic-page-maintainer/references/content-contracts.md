# Content Contracts

## Publications

- Data source: `_bibliography/papers.bib`
- Shared renderer: `_includes/publication_sections.liquid`
- Current top-level grouping:
  - Preprints
  - Publications
  - Manuscripts in Preparation, Under Review, or Forthcoming
  - Presentations and Posters at Conferences
- Manuscripts keep accepted/forthcoming above under-review or preparing items.
- Year grouping may be added if the list grows.
- Never shorten or hide long author lists unless the user explicitly requests it.

## CV

- `cv_pdf_filename` in `_config.yml` is the source of truth for the current downloadable CV.
- The visible CV date should be derived from the PDF filename, not manually duplicated.
- Keep the filename convention `CHEN_Yiru_CV_YYYY.MM.DD.pdf` unless the user changes it.
- Treat `_data/cv.yml` as the source of truth for structured CV entries.

## Homepage

- `_pages/about.md` mixes narrative text, profile metadata, and publication rendering.
- Treat identity, degree, affiliation, advisor, scholarship, and future-plan statements as protected.
- Check for duplicated facts in `_pages/cv.md`, `_data/cv.yml`, and `_news/*.md` before finalizing changes.

## Projects

- Source: `_projects/*.md`
- Keep each project as its own long-form page unless the user requests structural change.
- Be careful when editing status lines or publication references because they may mirror publication metadata elsewhere.

## News

- Source: `_news/*.md`
- Items can be inline or full posts.
- Milestone announcements are fact-sensitive and may affect homepage or CV consistency.

## Assets

- Verify referenced PDF, image, and poster paths before finishing.
- Prefer config- or content-driven asset references over duplicated hardcoded paths when the repo already supports derivation.

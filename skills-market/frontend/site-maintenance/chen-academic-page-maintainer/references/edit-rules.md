# Edit Rules

## Freely editable

Future agents may polish these without confirmation as long as meaning stays the same and structure is preserved:

- Project prose
- Life page prose
- Tech Blog index UI and non-sensitive page prose
- Low-risk UI wording
- Homepage version-line wording, while preserving the `Yiru's Version` label unless the user asks to rename it
- Research Radar page and renderer UI wording, as long as the current digest schema and generated article facts are preserved
- Readability and formatting in non-sensitive sections

## Restricted

Ask before changing:

- Homepage quick background
- Homepage profile metadata and status lines
- CV intro paragraph
- Publication status, category, venue, year, note, or authorship
- News posts about offers, acceptances, affiliations, or major milestones
- Research Radar article selections, rankings, summaries, metadata, recommendation labels, provider/scope metadata, generator identity text, and RSS item behavior
- User-supplied Tech Blog post wording, technical claims, or code snippets
- Ambiguous Website Management notes that do not identify a target page, request type, or exact protected wording
- Any content that mirrors academic status across multiple files
- Any content that mirrors publication or project status across BibTeX, project pages, CV data, timeline data, or news

## Exact wording only

Only change from direct user wording:

- Affiliation and institution names
- Degree and program labels
- Advisor or lab references
- Scholarship statements
- Future plans and timeline claims
- Identity statements
- User-provided article wording or article-level fact statements
- User-provided Research Radar correction text

## Refactoring policy

- Preserve the current site structure by default.
- If centralization or refactoring would help, identify it and ask before implementing it.
- Do not perform major layout, architecture, or template changes without explicit approval.
- Do not blindly sync the external Website Management folder into the website repo; translate only the requested note content.
- Do not treat every Markdown file in `Website_management/TechBlog/` as publish-ready automatically. Publish a Tech Blog post candidate only when the user asks to sync/apply it, and ignore `README.md`, `Current Tech Blog.md`, and templates.
- Do not publish paired English/Chinese Tech Blog drafts as duplicate posts unless the user explicitly asks; use one English-default bilingual post.
- Do not let the Tech Blog RSS feed include default/sample posts; it must use the same intentional-post filter as the Tech Blog page.
- Do not leave the default related-post recommendation block enabled on new Tech Blog posts unless the user explicitly asks for it.
- Do not import Life page photos from Website Management notes unless the user explicitly provides and confirms those images for the website.
- Do not mirror Research Radar into the external Website Management notes; Research Radar stays managed from the website repo.
- Do not initialize a nested git repository in `Website_management`; it is already inside the notes git repo.
- Do not move Research Radar generation, ranking, RSS ingestion, Zotero inspection, or provider automation into this repo unless the user explicitly requests that implementation.

## Uncovered-case policy

- If the skill does not explicitly define how to handle an issue, stop and ask the user.
- Do not infer new governance rules from a single ambiguous example.
- After the user answers, ask whether that rule should be added to the skill for future reuse.

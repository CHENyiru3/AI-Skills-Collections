---
name: duke-nus-marp
description: Create and edit academic Marp slide decks using the user's Duke-NUS theme and Harvard author–date citations. Use for Duke-NUS Marp presentations, lab meetings, research talks, and requests to apply this saved slide workflow. Not for unrelated PowerPoint editing or changing the user's citation library.
metadata:
  version: "1.0.1"
---

# Duke-NUS Marp slides

Produce editable Markdown with the bundled Duke-NUS CSS, source-grounded Harvard citations, and checked renders. User-specified content, slide count, location, and citation variants take precedence over defaults.

## Assets and scope

- `assets/duke-nus.css`: 1280 × 720 theme, Arial, blue #00539B, orange #F5821F, gray #4D4F53, online logo at https://i.imgur.com/hh3DOb2.png. Preserve this URL unless the user requests a change.
- `assets/starter.md`: minimal deck including Harvard references.
- `assets/example.md`: layout examples with explicitly fictional citation placeholders.
- `references/marp-guide.md`: read before authoring for syntax, class behavior, Harvard conventions, and export options.

The theme is a personal adaptation of the user's Duke-NUS PowerPoint, not an official template release. Use the bundled assets; no original machine-specific folder is required.

Work in the requested output directory. Read applicable local instructions, especially inside the Obsidian vault. Copy assets to the project before editing; do not modify the installed skill as part of making a deck. When an existing project has a customized theme or configuration, inspect and preserve it unless the user asks for replacement. Do not update vault indexes merely because slide sources live inside the vault.

## Authoring decisions

1. Inspect the supplied content and identify audience, purpose, and supported conclusions. Use reasonable assumptions for routine layout choices. Ask only for missing information that materially changes the talk.
2. Select the needed layouts from the example, then replace the examples with the actual content. Do not force every deck to include every layout. Honor the requested slide count, including references and cover unless the user specifies otherwise.
3. Keep one main point per slide. Preserve units, uncertainty, qualifiers, and attribution. Leave clear placeholders for missing data rather than inventing findings or sources.
4. Use `#` for the masthead title and an immediately following `##` for its optional subtitle. Both should fit one line on ordinary content slides. Use `###` for body headings.
5. Use local directives `<!-- _class: ... -->` to avoid leaking layout changes to later slides. Supported classes are `title`, `section`, `closing`, `figure`, `compact`, `references`, and `center`. Use `_paginate: skip` on covers/closing slides when excluding them from the count.
6. Use plain Markdown for routine content. The optional `columns` / `wide-left` divs need blank lines around their Markdown contents and HTML rendering enabled. In the `figure` layout, the last paragraph is the caption. Contain scientific figures without cropping evidence.

Keep the logo's original proportions and clear space. Do not recreate it with text or shapes. Do not add external font dependencies by default.

## Harvard citations

Default to the general Harvard convention documented in the guide: author–date in text; alphabetical, unnumbered references with hanging indents. A school/journal-specific Harvard variant overrides this default.

- Ground each real citation in supplied source material or verified bibliographic metadata. Check that the source supports the associated claim, not merely that its title sounds relevant.
- Match every in-text and figure citation to an entry, with consistent author names, years, and a/b suffixes. Include page locators for direct quotations.
- Use one plain paragraph per reference under `<!-- _class: references -->`; alphabetize across reference slides.
- Replace all illustrative names, years, and bracketed fields before delivering a finished research talk. Keep placeholders only when the user wants a template or required information is unavailable, and identify that limitation.
- CSS does not resolve citation keys, generate bibliographies, or sort references. Do not add `bibliography:`, `csl:`, or `[@key]` and imply the ordinary Marp CLI will process them. Use a separate citation processor only if that workflow is requested and verified.
- No Zotero installation, library indexing, or library writes are needed for formatting supplied references. Use relevant library tools only when the task actually needs library access.

## Export and verification

Use an available Marp CLI, or the tested baseline `@marp-team/marp-cli@4.5.1`. Discover local tools instead of embedding machine-specific npm cache paths. If using a different version, verify options against its help or official documentation.

From the output directory, with `duke-nus.css` beside `slides.md`:

```sh
npx @marp-team/marp-cli@4.5.1 slides.md --theme ./duke-nus.css --html -o slides.html
npx @marp-team/marp-cli@4.5.1 slides.md --theme ./duke-nus.css --html --pdf -o slides.pdf
```

Omit `--html` for decks without HTML layouts. Add `--allow-local-files` for trusted decks using local figures; the online logo does not need it. The logo requires internet access during preview and export; verify it loads before delivery. Exported PDFs retain the rendered logo for offline viewing. PDF requires a supported browser. Respect execution permissions if launching it is blocked.

- Render exports sequentially. Inspect each slide as an image at a consistent resolution, including the smallest text, captions, references, and page-number alignment. If a rendering artifact appears, rerender that deck alone before changing otherwise correct CSS.
- Check clipping, overlap, readable tables, image proportions, missing local assets, math, slide count, and citation/reference correspondence. Resolve layout issues by shortening or splitting content before using smaller text.
- Marpit's scaffold gives `section::after` inherited padding. Preserve the theme's explicit `padding: 0` on this pagination pseudo-element so page numbers align with the footer.
- Check the minimal starter separately after changing shared CSS. A layout-heavy example alone does not cover all uses.
- Deliver editable Markdown/CSS and needed assets, plus the requested exports. HTML/PDF are useful defaults for a finished talk, not prerequisites to a source-only edit. State any unverified export or missing source data honestly.
- Do not promise editable PowerPoint from ordinary Marp export: standard PPTX export uses rendered slide images. Keep Markdown as the editable source.

For VS Code, register the relative CSS path in the project's existing `markdown.marp.themes` array without replacing other entries. Current Marp for VS Code permits supported HTML elements in trusted workspaces; do not use the deprecated `markdown.marp.enableHtml` setting or change global editor settings.

## Official references

- [Theme CSS](https://marpit.marp.app/theme-css)
- [Marp CLI](https://github.com/marp-team/marp-cli#readme)
- [Marp for VS Code](https://github.com/marp-team/marp-vscode#readme)

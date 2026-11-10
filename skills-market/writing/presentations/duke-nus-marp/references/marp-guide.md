# Duke-NUS Marp theme

A clean 16:9 theme adapted from `../Duke-NUS-Beamer-Example-Editable.pptx`. It uses the reference's Arial typography, blue (#00539B), orange (#F5821F), gray (#4D4F53), logo at the upper left, and content titles beside the logo. The CSS loads the logo from https://i.imgur.com/hh3DOb2.png, preserving its proportions and clear space.

The logo requires internet access during preview and export. Exported PDFs retain the rendered logo for offline viewing. No online fonts or imported themes are used. Arial falls back to Helvetica or the system sans-serif font. This is a personal adaptation of the supplied reference, not an official institutional template release.

## Files

- `duke-nus.css`: reusable theme. Copy this single file to other projects.
- `starter.md`: short template to duplicate for a new presentation.
- `example.md`: examples of all main layouts.
- `example.html`: ready-to-open preview with slide navigation.
- `example.pdf`: rendered preview.
- `.marprc.yml`: local Marp CLI configuration.
- `.vscode/settings.json`: theme registration for Marp for VS Code when this folder is opened as the workspace.

## Start in VS Code

Open this **Marp folder** in VS Code with the Marp for VS Code extension installed. Duplicate `starter.md`, edit its text, and open Markdown Preview.

If you open a parent folder instead, add the CSS path relative to that workspace root to the existing `markdown.marp.themes` setting. Do not replace other registered themes. The example's two columns and figure placeholder use HTML divs, supported by current Marp for VS Code in a trusted workspace. If HTML has been disabled, restore the default `markdown.marp.html` setting. The starter uses ordinary Markdown only.

The required frontmatter is:

```yaml
---
marp: true
theme: duke-nus
paginate: true
footer: 'Duke-NUS Medical School'
---
```

## Export from this folder

With Node.js installed, run:

```sh
npx @marp-team/marp-cli@4.5.1 example.md -o example.html
npx @marp-team/marp-cli@4.5.1 example.md --pdf -o example.pdf
```

The local configuration loads the theme and enables HTML. PDF export requires a supported browser (Chrome, Edge, or Firefox).

For a deck outside this folder, specify the theme explicitly:

```sh
npx @marp-team/marp-cli@4.5.1 slides.md --theme /path/to/duke-nus.css -o slides.html
```

Add `--html` if the deck uses the optional HTML layouts. Add `--allow-local-files` when exporting a trusted deck that references local figures. The online theme logo does not require that flag.

## Layouts

Apply a class to one slide with a local directive:

```markdown
<!-- _class: title -->
<!-- _paginate: skip -->

# Presentation title
## Optional subtitle

Your name  
Duke-NUS Medical School  
Day Month Year
```

| Class | Use |
| --- | --- |
| (none) | Standard content with logo, title, orange rule, and footer |
| `title` | Cover with large title and author details |
| `section` | White section divider with a large blue heading |
| `closing` | Closing slide, with no visible footer or page number |
| `figure` | Figure slide with a smaller final caption paragraph |
| `compact` | Modestly smaller body and table text |
| `references` | Smaller text for bibliography entries |
| `center` | Vertically center the content below the masthead |

Combine modifiers when useful: `<!-- _class: compact center -->`. For covers and closing slides, `_paginate: skip` also excludes them from the total. CSS alone only hides their page number. Use `_footer: ''` or `_header: ''` to clear those fields on a particular slide.

Every content slide uses `#` for its masthead title. An immediately following `##` becomes the optional masthead subtitle. Use `###` for headings within the slide body. Keep masthead titles and subtitles to one line; a longer heading should be shortened or moved into the body.

Two-column slides use `<div class="columns">` with two child divs. Put blank lines around Markdown inside the divs, as shown in `example.md`. Add `wide-left` to give the first column more space.

Replace the figure placeholder with ordinary Markdown:

```markdown
<!-- _class: figure -->

# Main figure
## Brief result description

![width:1080 height:390](figures/result.png)

Figure 1. Caption and source.
```

The image is contained without cropping. The final paragraph on a `figure` slide is treated as its caption. Split dense material across slides rather than relying on clipping or automatic font shrinking.

## Harvard citations

Use author–date citations in slide text and an alphabetical, unnumbered reference list. The `references` class applies hanging indents to plain paragraphs (one paragraph per source). The names and years in the example deck are formatting placeholders, not real publications.

- Parenthetical: `(Brown, 2024)`.
- Narrative: `Brown (2024)`.
- Two authors: `(Smith and Lee, 2023)`.
- Three or more authors: `(Smith et al., 2023)`.
- Direct quotation: `(Brown, 2024, p. 12)`.
- Same author and year: `(Brown, 2024a)` and `(Brown, 2024b)`, matched in the reference list.
- Figure attribution: `Adapted from Brown (2024)`.

Journal article pattern:

```markdown
Author, A.A. and Author, B.B. (Year) ‘Article title’, *Journal title*, volume(issue), pp. first–last. Available at: https://doi.org/...
```

Use the article number instead of a page range where applicable. List all authors in the reference entries for this template. Include only sources actually cited; keep entries alphabetized across multiple reference slides.

Harvard has institutional variants. This template uses a consistent general Harvard convention; follow a required school or journal variant if supplied. See the [University of Leeds author–date guidance](https://library.leeds.ac.uk/info/1402/referencing/50/leeds_harvard_style) for the underlying citation and alphabetical-list principles.

Marp CSS styles the references but does not generate, alphabetize, or validate them. Enter formatted citations and references manually; bibliography keys alone will not resolve in the supplied workflow.

## Customization

Edit the named color variables and font family near the top of the CSS. Keep the `@theme duke-nus` metadata comment intact. If you rename the theme, update both that comment and the Markdown `theme:` field.

The supplied PPTX is the main visual reference. Section dividers use a white background and the full-color logo to keep this clean version consistent. Original slide content and embedded research screenshots are not included.

## Documentation

- [Marpit Theme CSS](https://marpit.marp.app/theme-css): theme metadata, slide dimensions, pagination, and scoped styles.
- [Marp CLI](https://github.com/marp-team/marp-cli#readme): export and browser options.
- [Marp for VS Code](https://github.com/marp-team/marp-vscode#readme): custom theme registration.

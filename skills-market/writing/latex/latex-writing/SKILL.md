---
name: latex-writing
domain: writing
description: Author or review LaTeX source for semantic structure, equations, references and class-compatible markup. Use for .tex work or LaTeX portions of noweb .nw files; not every academic writing task or a mandatory package/style migration.
metadata:
  version: "1.0.1"
---

# LaTeX Authoring

Inspect the document class, preamble, bibliography system and source conventions.
Preserve scientific meaning, labels and journal requirements. Add packages only
when needed and compatible; there is no mandatory external preamble to copy.

Use semantic markup for the intended structure. `description` suits labeled
term/definition entries, `itemize` unordered items and `enumerate` sequences.
A publisher's supported environment may override those defaults. Use headings,
figures/tables, captions and labels rather than visual approximations with repeated
line breaks or manual numbering.

For math, prefer `[...]` or `equation` and suitable amsmath environments such as
`align` over `$$` or `eqnarray`, when supported by the class. Align related steps and
number only references that need numbers. Equations remain part of sentences;
preserve punctuation, variable definitions, units and mathematical meaning.
Use text/operator commands for words and named operators rather than unintended
products of italic letters. Avoid changing mathematical notation as a style cleanup.

Use the project's existing cross-reference and citation commands. cleveref and
csquotes can help when compatible and already chosen; `cref` and `enquote` are
not universal prerequisites. Match citation punctuation and author/date style to
the target journal. Keep labels unique and attach them to the correct numbered
object, commonly after a float caption.

In noweb LaTeX documentation chunks, use `[[code]]` notation where the active noweb
processor expects it; do not apply that notation inside ordinary .tex or code chunks.
Check the actual weaving tool before changing quoting/escaping rules.

Review for changed structure, references and relevant compilation warnings. Preserve
author voice and evidence instead of enforcing stock transitions, universal passive
voice rules or one paragraph template. Compile/render when needed to establish the
changed source behavior. Stop after the requested LaTeX edit is valid; no global
preamble replacement or whole-paper rewrite is implied.

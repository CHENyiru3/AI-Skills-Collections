---
name: theme-factory
domain: documents
description: Apply a saved visual theme or create a requested color/font theme for an artifact. Use for explicit theming work; preserve a specified or existing theme rather than forcing a new selection flow.
license: Complete terms in LICENSE.txt
metadata:
  version: "1.0.1"
---

# Theme Factory

Use the theme already specified by the user or the artifact's documented design
system. If a choice is genuinely needed, offer a small relevant selection or use
an authorized design judgment; do not ask for the same decision again.

The `themes/` directory contains ten presets. Read only the selected/relevant file;
`theme-showcase.pdf` is an optional visual aid for choosing and should remain unchanged.
A custom theme should specify semantic color roles, font pairing and contrast,
using the user's brief rather than inventing unrelated brand requirements.

Apply colors/fonts consistently through the artifact's own backend/styles. Preserve
content, layout and useful hierarchy. Verify fonts are available or embedded and
choose a suitable fallback openly; theme prose does not install fonts automatically.
Check contrast and rendered output at the intended viewing size.

Report the applied theme and relevant checks, then stop. A showcase, explicit
selection confirmation and separate custom-theme review are unnecessary when the
user already chose the theme or delegated the design choice.

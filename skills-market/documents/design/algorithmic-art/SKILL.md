---
name: algorithmic-art
domain: documents
description: Create original code-based generative art with p5.js, seeded variation or interactive parameters. Use for algorithmic art requests; not ordinary charts, UI styling or static artwork that does not benefit from a generative system.
license: Complete terms in LICENSE.txt
metadata:
  version: "1.0.1"
---

# Algorithmic Art

Translate the user's subject, aesthetic and output constraints into a generative
system. Choose a computational idea that changes the visual result; do not require
a separate manifesto or override the brief in the name of creative freedom.

Use a seed for reproducible variations. Initialize both `randomSeed(seed)` and
`noiseSeed(seed)` before creating state, and avoid unseeded randomness/time-dependent
initialization where repeatability is intended. Reproduction also depends on
parameters, algorithm/library version, frame/state and external assets.

Expose only parameters useful for the artwork. Clamp/parse UI values, reset prior
state before regeneration, and bound particle counts/iterations so exploration
does not freeze the browser. For animation, define timestep/frame behavior and
provide pause or reduced-motion support when appropriate.

`templates/viewer.html` is an optional interactive starting point, not a required
brand/layout. If used, inspect it and adapt colors/fonts/controls to the brief;
verify every retained control, including reset and download. Read
`templates/generator_template.js` only for needed state/seed organization, not as
a fixed pattern to copy.

Deliver the requested code/artifact format. A single HTML can inline the algorithm
and controls, but CDN p5.js/fonts still require network access; bundle dependencies
when offline use is required. Separate JS and a short design explanation are
optional when useful, not contradictory mandatory outputs.

Run the artwork in an available browser, inspect its appearance and console, and
check seed/parameter/reset/export behavior that was included. Record actual seed
and settings for reproducible variants. Stop when the requested artwork works and
matches the brief; repeated craftsmanship claims and fixed polish cycles add no
acceptance value.

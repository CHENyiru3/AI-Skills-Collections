---
name: slack-gif-creator
domain: documents
description: Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for Slack like "make me a GIF of X doing Y for Slack."
license: Complete terms in LICENSE.txt
metadata:
  version: "1.0.1"
---

# Slack GIF Creation

Create the requested GIF for its intended use: custom emoji and a message attachment
have different size/readability needs. Verify current Slack/workspace limits for an
actual upload; local encoding presets are recommendations, not provider guarantees.
Creating a file does not authorize posting it or adding a workspace emoji.

Establish dimensions, duration, loop and transparency from the brief. A small square
canvas is a useful emoji starting point; choose frame rate/palette from motion and
file-size needs rather than universal 10–30 FPS or 480px rules. Keep subject/text
legible at the actual display size and avoid flashing when it is unnecessary.

Use supplied artwork as the requested source or reference. Do not replace it with
unrelated graphics. The bundled `core.gif_builder.GIFBuilder` can assemble equal-size
Pillow/array frames; inspect its signature for palette/transparency/duplicate options.
Use `core.easing` and `core.frame_composer` only when their helpers fit the animation.
Run from this skill directory or configure its import path explicitly.

Render a small, coherent motion with controlled state and a clean loop. Check
frame disposal and transparency so previous frames do not leave unwanted trails.
Optimize colors, dimensions, timing or duplicate frames when needed, preserving
recognizable motion and the user-requested content.

Inspect the saved GIF, not just the source frames: dimensions, frame sequence,
per-frame durations, palette, looping, bytes and representative visual playback.
`core.validators` offers local dimension heuristics and metadata, not a complete
Slack acceptance test; independently verify provider file limits and timing when
relevant. Do not claim a GIF was uploaded or validated by Slack unless that occurred.
Stop when the requested animation and export requirements are met.

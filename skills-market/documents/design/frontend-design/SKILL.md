---
name: frontend-design
domain: documents
description: Design and implement a frontend page or component with a coherent visual direction and working interactions. Use for an explicit web UI design task; not posters, unrelated code edits or a mandate to replace an existing design system.
license: Complete terms in LICENSE.txt
metadata:
  version: "1.0.1"
---

# Frontend Design

Establish the interface's purpose, audience, required actions and technical context.
Use the existing design system and framework unless the task includes a redesign.
Choose a visual direction from the brief; originality is useful when it supports
recognition and usability, not as a requirement to make every interface extreme.

Make typography, spacing, color and imagery coherent. Use reusable tokens where
helpful and ensure type coverage, contrast and readable density. Familiar fonts,
plain backgrounds and conventional layouts can be the right choice; blanket bans
on Arial/Inter/system fonts or blue palettes do not establish quality.

Implement real interactions and responsive states rather than a static visual
promise. Preserve semantic structure, keyboard access, focus/hover/disabled states
and error/loading behavior. Use motion purposefully and respect reduced-motion
preferences; avoid decorative effects that block content or input.

Match implementation complexity to the brief and existing stack. Inspect the
rendered result at relevant viewport sizes, exercise the main interaction and
check changed accessibility/console behavior. Fix actual problems and stop when
the requested interface works and its design is coherent; do not require novelty,
new dependencies or a global restyle for a scoped component change.

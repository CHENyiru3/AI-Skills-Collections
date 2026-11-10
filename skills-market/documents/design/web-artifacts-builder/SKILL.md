---
name: web-artifacts-builder
domain: documents
description: Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.
license: Complete terms in LICENSE.txt
metadata:
  version: "1.0.1"
---

# Web Artifact Builder

Build the requested multi-component HTML artifact using the existing project and
chosen stack. A simple single-file request does not need this scaffold. Preserve
existing configuration/dependencies rather than introducing React/Tailwind/shadcn
solely because they are bundled here.

For a genuinely new scratch project, inspect `scripts/init-artifact.sh` and its help
before selecting it. It installs dependencies and writes configuration, and its
bundled component versions may differ from current framework APIs. It refuses an
existing destination and does not install pnpm globally. Verify Node/package-manager
compatibility and the resulting build; do not advertise an untested stack as ready.

Develop the actual state, routing and interactions needed by the user. Use the
brief/design system rather than fixed font/color bans. Test the main interaction,
responsive layout and relevant console/build behavior before delivery; testing is
part of establishing that a working artifact works, not an optional afterthought.

Use `scripts/bundle-artifact.sh` only when a single HTML bundle is wanted. Inspect
it first: it installs bundling dependencies, may add Parcel configuration, and
cleans its output paths. Run in a disposable build copy if those files conflict
with existing project output. A successful bundle can still depend on remote
fonts, images or APIs; inspect those dependencies before claiming offline use.

Open the actual bundled artifact in the target environment when available and
check its critical behavior. Report the source/bundle paths, checks and runtime
limits. Stop after the requested artifact; hosting, publication and a new design
system are separate scope decisions.

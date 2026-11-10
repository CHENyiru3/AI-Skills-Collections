---
name: codebase-inspection
domain: platforms
description: Measure repository file/line/language composition with a defined scope, using pygount when available. Use for requested codebase statistics; not executing reviewed code or altering system Python to install a metric tool.
author: Hermes Agent
license: MIT
metadata:
  version: "1.0.1"
  hermes:
    tags:
    - LOC
    - Code Analysis
    - pygount
    - Codebase
    - Metrics
    - Repository
    related_skills:
    - github-repo-management
prerequisites:
  commands:
  - pygount
---

# Codebase Statistics

Identify the repository, revision/worktree state and metric: physical lines, language
classification, code/comment ratios, file counts or disk bytes are different measures.
Use available tools and document the scope. Do not run project code merely to count it.

If pygount is installed, inspect its help and request a targeted summary. Exclude
version-control metadata, virtual environments, dependencies and generated/build
outputs according to the question; include vendored/generated sources when the user
explicitly wants them. Report exclusions rather than hiding them in a catch-all.

Do not install with `--break-system-packages` or suppress installation errors. Use
an isolated tool environment only when installation is within scope, or provide a
clearly labeled simpler count. A suffix count or `wc` result is not semantic LOC.

Interpret classifier-specific categories (binary, generated, duplicate, unknown)
and Markdown/JSON behavior from the actual tool/version. Distinguish documentation
lines from comments and avoid treating LOC as a quality/productivity score.

Return a compact table with method, units, scope and limitations. Stop when the
requested statistics are established; this is not a code/security review. Preserve
the stable registry ID and existing invocation name rather than renaming consumers.

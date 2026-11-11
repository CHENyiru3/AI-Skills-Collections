---
name: computational-biology-project-manager
description: Initialize, resume, organize, or hand off a computational biology project using an index and current-state recap. Use for project continuity or explicitly requested local skill distillation; not method selection or result interpretation.
metadata:
  version: "1.0.0"
---

# Computational Biology Project Manager

Manage structure and continuity while leaving scientific intent with the
researcher. Reuse the chosen project root, existing conventions, and established
authorization. A resume request does not authorize reorganizing the project.

## Select the work

- **Initialize:** inspect first; create only missing agreed directories and
  management documents. Merge useful existing notes rather than replacing them.
- **Resume:** read the index, recap, and relevant artifacts. Distinguish current
  observations, unverified prior claims, unresolved decisions, and next work.
- **Maintain or hand off:** update stable navigation when facts change; record
  substantive outcomes, actual checks, limitations, and next authorized actions.
- **Distill a local skill:** only when requested or already authorized; capture
  a demonstrated reusable workflow using [local-skills.md](references/local-skills.md).

## Workspace and records

For a new project without another convention, use:

```text
data/               Inputs; preserve raw data
scripts/            Analysis and utility code
outputs/            Generated artifacts
log/                Execution records
project_index.md    Stable overview and navigation
last_recap.md       Latest current-state handoff
```

Do not move existing data or impose this layout over a conflicting convention.
Report a path/type collision before dependent writes. Do not populate empty
directories with speculative data, code, results, or dependency files.

Use [project-documents.md](references/project-documents.md) when creating or
merging the index or recap. Its default is English project documentation and a
Chinese `last_recap.md`; follow explicit user or established project language
choices instead when they differ. Use relative links and label unknowns `TBD`.
Keep the index for stable facts and long traces in the established log location.

For a temporary conversation transfer, use the separate `handoff` skill when
available and requested. Its full-session context need not enter the repository.
Do not install companions merely because project management was requested.

## Scientific boundary and completion

Carry out method-preserving administration and mechanical fixes within scope.
Resolve missing choices that affect scientific meaning before dependent work;
reuse decisions already authorized. Do not alter raw data or silently replace
meaningful results. For analysis code, use `scientific-coding-governance` when
available; otherwise preserve the same scientific boundary.

Verify touched paths, links, and recap claims against relevant artifacts. Report
what changed and what remains uncertain, then stop when continuity is restored.

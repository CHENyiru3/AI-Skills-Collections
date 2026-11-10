---
name: managing-python-releases
domain: programming
description: Prepare a Python package version/changelog or perform an explicitly requested release. Use for release planning, deprecations and publication workflows; local preparation alone does not authorize tagging, pushing or uploading.
metadata:
  version: "1.0.1"
---

# Python Release Management

Separate preparation from publication. Identify the project/version source, base
and target commit, intended artifacts and requested destination. Preserve unrelated
working-tree changes and existing release conventions.

Choose a version by observable compatibility: compatible correction → PATCH,
compatible added capability → MINOR, incompatible public contract → MAJOR, subject
to the project's documented scheme. Record deprecations and a practical migration
path; do not promise a removal date or support policy the maintainers did not choose.

Update the authoritative version source and derived metadata consistently. Use
`scripts/bump_version.py --help` and `--dry-run` only for a project with a static
three-component version. The helper supports this limited scheme, not all Python
version forms or dynamic backends; inspect its proposed files before applying it.
Read [MIGRATION.md](MIGRATION.md) for a needed migration guide and
[AUTOMATION.md](AUTOMATION.md) for requested release automation.

Build/inspect fresh artifacts and run checks relevant to changed behavior and
supported environments. A packaging task is complete when the requested artifacts
are reviewable; it need not publish them to establish correctness.

For an authorized release, stage only intended files, inspect the exact commit
and create/push only the intended tag/ref. Avoid `git commit -am`, `git add -A` and
`git push --tags` recipes that include unrelated work. Check tag-triggered workflows
before pushing; publication may start immediately. Confirm artifact/version/index
identity and report the observed result rather than treating a successful push as
proof that downstream publication completed.

Stop at the requested preparation or release outcome. Do not repeatedly republish
immutable versions or broaden a failed release into repository-wide changes.

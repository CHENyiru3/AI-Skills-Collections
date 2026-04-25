# Generated Skill Template

Use this template when drafting the repo-specific downstream maintenance skill.

```markdown
---
name: <site-specific-skill-name>
description: Maintain this specific website repo safely and consistently. Use this skill whenever the user asks to update, review, polish, reorganize, or extend this website, especially when the request touches governed sections, publication formatting, CV assets, shared templates, or duplicated content.
---

# <Site Specific Skill Name>

## What this skill does

Explain the purpose of the website and the maintenance scope.

## Repo map

Point to:
- `references/repo-map.md`
- `references/edit-rules.md`
- `references/content-contracts.md`
- `references/style-preferences.md`

## Default workflow

1. Inspect the relevant page, data source, and shared renderer first.
2. Check whether the requested section is freely editable, restricted, or exact-wording-only.
3. Prefer shared includes or single sources of truth over duplicated edits.
4. Preserve formatting contracts, ordering, labels, and derived values.
5. Ask before changing restricted or sensitive content.
6. Verify that all mirrored sections stay consistent.

## Edit permissions

Define:
- freely editable sections
- restricted sections
- exact-wording sections

## Formatting contracts

Define:
- publication rules
- CV/versioning rules
- date/path derivation rules
- section-specific conventions

## Approval-required changes

List the high-risk categories that require user confirmation.

## Verification checklist

List the repo-specific checks to run before finishing.
```

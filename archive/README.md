# Skill archive

Retired skills are preserved here for possible recovery. This directory is excluded from the active registry, catalogs, marketplace, deployment profiles, and taskpack discovery.

## Archived on 2026-11-10

The owner selected these skills for removal from the active market because they are no longer expected to be used or may be outdated. This is an owner preference, not an independent assessment of upstream maintenance.

| Skill | Preserved folder |
|-------|------------------|
| hermes-agent | [skills/agents/hermes-agent](skills/agents/hermes-agent/SKILL.md) |
| opencode | [skills/agents/opencode](skills/agents/opencode/SKILL.md) |
| zed | [skills/agents/zed](skills/agents/zed/SKILL.md) |
| cursor-usage-checker | [skills/ai-ml/llm/cursor-usage-checker](skills/ai-ml/llm/cursor-usage-checker/SKILL.md) |
| minimax-cli | [skills/ai-ml/llm/minimax-cli](skills/ai-ml/llm/minimax-cli/SKILL.md) |
| visium | [skills/compbio/spatial-omics/platforms/visium](skills/compbio/spatial-omics/platforms/visium/SKILL.md) |
| bitwarden | [skills/core/security/bitwarden](skills/core/security/bitwarden/SKILL.md) |
| skill-seekers | [skills/core/dev/skill-seekers](skills/core/dev/skill-seekers/SKILL.md) |
| codebti | [skills/projects/codebti](skills/projects/codebti/SKILL.md) |

Five already missing skills have metadata only: `beamer`, `clawd-animation`, `clawd-animation-lite`, `neat-freak`, and `the-pirate-bay`. No skill files existed for these entries.

The requested name `skill-seeker` refers to the existing `skill-seekers` skill.

## Recovery records

- [registry/skills.yaml](registry/skills.yaml) preserves all 14 original registry entries, archive dates, reasons, and file locations.
- [registry/aliases.yaml](registry/aliases.yaml) preserves removed legacy aliases.
- [registry/removed-references.yaml](registry/removed-references.yaml) preserves skill selections removed from deployment profiles and taskpacks.
- [taskpacks/codebti.yaml](taskpacks/codebti.yaml) preserves the retired project bundle.
- [marketplace/marketplace.json.bak](marketplace/marketplace.json.bak) preserves the previous historical marketplace backup. It is not the active marketplace.

For restoration and future archival steps, see the [architecture guide](../docs/guides/architecture.md#archiving-and-restoring-skills). Active discovery commands should scan `skills-market/`, rather than searching the entire repository for `SKILL.md`.

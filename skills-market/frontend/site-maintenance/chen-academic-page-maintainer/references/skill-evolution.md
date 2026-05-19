# Skill Evolution

Use this process whenever a future maintenance request exposes a case that is not explicitly covered by the current skill.

## Rule-gap workflow

1. Stop and identify the uncovered issue clearly.
2. Inspect the current repo structure enough to separate repo facts from user preference.
3. Ask the user how they want that case handled.
4. Resolve the immediate task using the user's answer.
5. Ask whether the answer should become a standing rule in this skill.
6. If the user says yes, update `SKILL.md` and the relevant reference file so future agents follow the same rule.

## Candidate rule types

- New protected sections
- New formatting contracts
- New publication or CV conventions
- New duplication hotspots
- New approval-required change classes
- New tone exceptions
- New Research Radar schema fields, source categories, or generator boundaries
- New Website Management note request types, templates, or sync rules

## Update target selection

- Update `SKILL.md` if the rule affects workflow, permissions, or approval behavior.
- Update `references/edit-rules.md` if the rule changes what can be edited freely or only with confirmation.
- Update `references/content-contracts.md` if the rule defines a source of truth or formatting contract.
- Update `references/style-preferences.md` if the rule changes tone or section-specific voice.
- Update `references/repo-map.md` if the rule depends on a new source location or newly discovered duplication hotspot.
- When changing Website Management note rules, check `/Users/eric_yiru/Desktop/Home/Main_branch/Notes/03_Resources/Website_management/Index Entry.md`, `Website Source Map.md`, and the relevant template files.
- When changing Research Radar rules, check `_research_radar/*.md`, `_includes/research_radar_sections.liquid`, `_includes/research_radar_article.liquid`, and `_pages/research-radar-feed.xml` before editing the skill.

# Skill Evolution

Use this process whenever a future maintenance request exposes a case that is not explicitly covered by the current skill.

## Rule-gap workflow

1. Stop and identify the uncovered issue clearly.
2. Ask the user how they want that case handled.
3. Resolve the immediate task using the user's answer.
4. Ask whether the answer should become a standing rule in this skill.
5. If the user says yes, update the skill and the relevant reference file so future agents follow the same rule.

## Candidate rule types

- New protected sections
- New formatting contracts
- New publication or CV conventions
- New duplication hotspots
- New approval-required change classes
- New tone exceptions

## Update target selection

- Update `SKILL.md` if the rule affects workflow, permissions, or approval behavior.
- Update `references/edit-rules.md` if the rule changes what can be edited freely or only with confirmation.
- Update `references/content-contracts.md` if the rule defines a source of truth or formatting contract.
- Update `references/style-preferences.md` if the rule changes tone or section-specific voice.
- Update `references/repo-map.md` if the rule depends on a new source location or newly discovered duplication hotspot.

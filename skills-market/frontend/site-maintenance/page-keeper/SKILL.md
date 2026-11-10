---
name: page-keeper
domain: frontend
description: Create a reusable maintenance skill for a specific website repository from its structure and established rules. Use when the user wants persistent site-maintenance instructions; not for a one-off website content edit alone.
metadata:
  version: "1.0.1"
---

# Website Maintenance Skill Builder

Inspect the target repository and relevant local instructions before asking questions.
Identify its framework, content sources, routes, shared renderers, assets and actual
build/check commands. Use [repo-discovery-checklist.md](references/repo-discovery-checklist.md)
for unfamiliar structure, not as a requirement to inventory unrelated subsystems.

Separate evidence-backed repo facts from user preferences or permissions. Reuse
known choices from the conversation and repository. Ask only about consequential
unknowns such as protected identity wording, publication-status changes or the
scope of future restructuring; do not reconfirm routine choices already authorized.
[question-catalog.md](references/question-catalog.md) is an optional aid.

Write a self-contained downstream skill that identifies the actual site/repository
in its discovery contract. Record canonical content/data sources, duplication risks,
formatting/date/path rules and validation that matters to that site. Preserve exact
user wording and evidence for identity/affiliation/publication facts; do not invent
permissions, affiliations or future dates from a generic personal-site pattern.

Use [generated-skill-template.md](references/generated-skill-template.md) only for
needed structure. A separate rulebook via [rulebook-schema.md](references/rulebook-schema.md)
can help a complex site, but should not duplicate the whole skill. Do not require
eight sequential reports or a placeholder outline when the user wants a final skill.

Validate target paths, trigger precision, usable references and a few relevant
maintenance scenarios. `evals/evals.json` contains optional starter cases, not
mandatory external model runs. Keep applicable version/registry/UI conventions.
Stop when the requested site-specific skill is usable and verified; installation,
publication and unrelated website changes are separate scope decisions.

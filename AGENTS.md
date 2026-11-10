# Repository Guidelines

## Project Structure & Module Organization

This repository is a catalog of AI agent skills. Each skill lives in a leaf directory and is discovered through `SKILL.md`.

- `agent/`: coding-agent and protocol skills.
- `document-skills/`: Office, PDF, design, frontend, and artifact skills.
- `Font_end/`: website maintenance skills. Preserve this existing directory name.
- `python-skills/`: Python library engineering skills and supporting references.
- `ai-ml-skills/`: deep learning, LLM, and training skills.
- `compbio-skills/`: computational biology, single-cell, spatial, workflow, and database skills.
- `writing/`: academic writing, LaTeX, and Obsidian skills.
- `docs/`: catalog pages and guides.
- `archive/`: retired skill files and recovery metadata; excluded from active discovery and installation.

Skill-local support files belong under `references/`, `scripts/`, `assets/`, or `evals/`.

## Build, Test, and Development Commands

There is no global build step. Use lightweight validation:

```bash
rg --files skills-market -g 'SKILL.md' # list active skills
find skills-market -name SKILL.md -print # verify active skill file placement
python path/to/script.py --help       # smoke-test changed helper scripts
```

For install checks, follow `README.md` and verify each installed leaf directory contains `SKILL.md`.

## Coding Style & Naming Conventions

Write skill directories in lowercase kebab-case, for example `python-skills/api-design/`. Keep skills self-contained; avoid external file references unless intentional and documented.

`SKILL.md` files must start on line 1 with YAML frontmatter. Include `name`, a specific `description` that explains trigger conditions, and a quoted `metadata.version` in `MAJOR.MINOR.PATCH` form. The version must match the skill's `version` in `registry/skills.yaml`. Use concise Markdown, actionable steps, and relative paths.

For later changes to a skill's instructions or bundled resources, update both version fields: PATCH for compatible corrections, MINOR for compatible added capabilities, and MAJOR for incompatible changes. Preserve an existing declared version on initial import; use `1.0.0` as the local baseline when none exists. Compare differing copies before resolving a conflict; version numbers alone do not justify overwriting user edits.

Python helper scripts should be readable, typed where practical, and executable from their skill directory. Prefer the standard library unless a requirements file declares dependencies.

## Testing Guidelines

No repository-wide test framework is configured. When changing a skill, manually validate the trigger description, referenced paths, and commands in examples. When changing scripts, run the smallest relevant smoke test, such as `--help` or a sample input. Add focused examples under `references/` when behavior is non-obvious.

## Commit & Pull Request Guidelines

Recent commits use short imperative summaries such as `update humanizer skill` and `update cursor check skill`. Start with a lowercase verb and name the changed skill or area.

Pull requests should include a brief summary, changed directories, validation performed, and any installation or marketplace impact. Link issues when available. Include screenshots only for visual/frontend skills.

## Agent-Specific Instructions

When adding or moving a skill, update related documentation in `README.md`, `docs/catalogs/`, and Claude marketplace configuration if the skill should be discoverable there. Do not bulk-copy local installed-skill output back into the repo.

When archiving skills, preserve their files and original metadata under `archive/`, remove their active registry entries, aliases, profile/taskpack selections, and index listings, and regenerate the marketplace. Follow `docs/guides/architecture.md` for archival and restoration details. Do not reintroduce archived skills into active listings unless the user requests restoration.

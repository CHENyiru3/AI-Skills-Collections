# CodeBTI

![CodeBTI Overview](https://i.imgur.com/RRNOh09.jpeg)

CodeBTI is a code-style version of MBTI for software projects. It helps a human and an AI agent choose a consistent Python coding style, design-pattern posture, testing policy, dependency policy, and collaboration workflow before implementation starts.

CodeBTI is not a personality test. It is a practical interview and documentation system for generating project-specific guidance such as `CodeStyle.md`, `SKILL.md`, or `SPEC.md`.

## Install as a Skill

This repository can be installed directly as a Codex skill. Copy or install this repo into your Codex skills directory as `codebti`. The root `SKILL.md` is the entry point.

## How It Works

1. The user describes the project.
2. The agent asks the 10 fixed Python questions in [python/questions/fixed-python.md](python/questions/fixed-python.md).
3. The agent asks exactly 5 adaptive follow-up questions using [python/questions/adaptive-question-guide.md](python/questions/adaptive-question-guide.md).
4. The agent records answers with [python/records/session-record.template.md](python/records/session-record.template.md).
5. The agent infers a Python style profile from [python/profiles/python-profile-taxonomy.md](python/profiles/python-profile-taxonomy.md).
6. The agent generates project guidance using the templates in [python/templates/](python/templates/).

## Repository Map

- [SKILL.md](SKILL.md): installable skill entry point for AI agents.
- [AGENT.md](AGENT.md): top-level agent guide and workflow reference.
- [python/questions/](python/questions/README.md): fixed and adaptive interview guidance.
- [python/patterns/](python/patterns/README.md): Python design-pattern database with RefactoringGuru citations.
- [python/profiles/](python/profiles/README.md): profile inference rules and Python profile taxonomy.
- [python/records/](python/records/README.md): session recording rules and record template.
- [python/templates/](python/templates/README.md): output templates for generated project guidance.

## Current Scope

The initial version is Python-first. Future languages should add parallel question sheets, pattern databases, and profile taxonomies without changing the core interview flow.

## Output

The main output is a project-specific `CodeStyle.md`. When useful, the same result can be distilled into:

- `SKILL.md` for reusable agent behavior,
- `SPEC.md` for project requirements,
- narrower specs such as `API_SPEC.md`, `TESTING_SPEC.md`, or `ARCHITECTURE_SPEC.md`.
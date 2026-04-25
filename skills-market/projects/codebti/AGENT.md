# CodeBTI Agent Guide

## Project Summary

CodeBTI is a code-style counterpart to MBTI. MBTI describes personality preferences; CodeBTI describes coding and design preferences for a project or a general engineering identity.

The goal is not to create a toy personality quiz. The goal is to help an AI agent and a human developer explicitly choose the coding style, architectural boundaries, design patterns, and review standards that should remain consistent throughout a project. The final result should be practical enough to become a `SKILL.md`, a project `SPEC.md`, or a reusable `CodeStyle.md`.

The current version focuses on Python. The repository is organized so that other languages can be added later without changing the core workflow.

## Audience

This repository is face-to-agent. AI coding agents should be able to read it directly and understand:

- what CodeBTI is,
- how to interview a user,
- how to record answers,
- how to infer a coding-style profile,
- how to generate a project-specific `CodeStyle.md`,
- and how to extend the system with new languages or design-pattern examples.

All primary content should be plain markdown. Avoid runtime dependencies, web apps, binary assets, and tool-specific formats in the initial version.

## Repository Shape

```
CodeBTI/
  SKILL.md          # installable skill entry point
  AGENT.md          # agent guide and workflow reference
  README.md         # human entry point
  python/
    questions/
      README.md
      fixed-python.md
      adaptive-question-guide.md
      editorial-guide.md
      question-format.md
    patterns/
      README.md
      python/
        README.md
        abstract-factory.md
        adapter.md
        bridge.md
        builder.md
        chain-of-responsibility.md
        command.md
        composite.md
        decorator.md
        facade.md
        factory-method.md
        flyweight.md
        iterator.md
        mediator.md
        memento.md
        observer.md
        prototype.md
        proxy.md
        singleton.md
        state.md
        strategy.md
        template-method.md
        visitor.md
    profiles/
      README.md
      python-profile-taxonomy.md
    records/
      README.md
      session-record.template.md
    templates/
      CodeStyle.template.md
      SKILL.template.md
      SPEC.template.md
```

The root `SKILL.md` is the installable skill entry point. `AGENT.md` and `README.md` provide additional context for humans and non-skill agents.

## Core Workflow

1. The user describes what they want to build.
2. The agent asks the 10 fixed Python questions in `python/questions/fixed-python.md`.
3. The agent asks exactly 5 adaptive follow-up questions using `python/questions/adaptive-question-guide.md`.
4. The agent records all answers with `python/records/session-record.template.md`.
5. The agent analyzes the answers using `python/profiles/python-profile-taxonomy.md` and the pattern database in `python/patterns/`.
6. The agent generates a detailed project `CodeStyle.md` from `python/templates/CodeStyle.template.md`.
7. If appropriate, the agent distills the style guidance into `SKILL.md` or `SPEC.md` using the templates in `python/templates/`.

## Current Status

The Python-first CodeBTI foundation is implemented:

- human entry point: `README.md`,
- agent guide: `AGENT.md`,
- installable skill entry point: `SKILL.md`,
- fixed question sheet: `python/questions/fixed-python.md`,
- adaptive question guide: `python/questions/adaptive-question-guide.md`,
- question editorial rules: `python/questions/editorial-guide.md`,
- 22-page Python design-pattern database: `python/patterns/python/`,
- Python profile taxonomy: `python/profiles/python-profile-taxonomy.md`,
- session recording template: `python/records/session-record.template.md`,
- output templates: `python/templates/CodeStyle.template.md`, `python/templates/SKILL.template.md`, and `python/templates/SPEC.template.md`.

No automation scripts, CLI, web app, or CI system are part of the current version.

## File Type Responsibilities

### Entry Files

Entry files give agents the minimum context needed to proceed. `SKILL.md` is the installable skill entry point. `AGENT.md` provides additional workflow guidance. `README.md` explains CodeBTI for humans and links to the main workflow.

Entry files should be concise, operational, and stable. Avoid burying important instructions in long essays.

### Design Pattern Examples

Pattern files describe real engineering preferences. They should not simply list abstract patterns. Each file should explain:

- the style choice,
- when it is useful,
- when it becomes harmful,
- what it looks like in Python,
- what signals in a user's answers suggest this preference,
- and how the preference should appear in generated code or review comments.

Pattern examples are general references. The generated `CodeStyle.md` should be project-specific. The current Python pattern database mirrors the classic GoF catalog structure and cites RefactoringGuru sources in each pattern page.

### QA Sheets

The fixed Python QA sheet contains 10 example-based questions covering:

- general purpose and paradigm,
- defensive coding and type boundaries,
- error handling and recovery,
- naming and readability,
- architecture and wiring style,
- folder structure,
- testing philosophy,
- comments and docstrings,
- Git history and collaboration,
- dependencies and environments.

The adaptive question guide instructs the agent to ask exactly 5 follow-up questions based on ambiguity, contradictions, project risk, strong signals, and likely pattern misuse.

### Records

Each session should be recorded in `python/records/` using a markdown file. The filename should include the date and a short project slug, for example:

```text
python/records/2026-04-22-my-python-cli.md
```

A session record should include:

- project summary,
- fixed questions and answers,
- adaptive questions and answers,
- agent observations,
- inferred CodeBTI profile,
- generated output files,
- and unresolved assumptions.

Do not record secrets, private credentials, or irrelevant personal information.

### Generated Output

The primary generated artifact is `CodeStyle.md`. It should be specific enough that an agent can use it during implementation and review.

A strong `CodeStyle.md` should define:

- project intent,
- preferred architecture,
- module boundaries,
- naming conventions,
- typing policy,
- error-handling policy,
- dependency policy,
- testing policy,
- documentation policy,
- examples of preferred code,
- examples of avoided code,
- review checklist,
- and instructions for future agent behavior.

When useful, the same guidance can be distilled into:

- `SKILL.md` for reusable agent behavior,
- `SPEC.md` for project-specific requirements,
- or narrower spec files such as `API_SPEC.md`, `TESTING_SPEC.md`, or `ARCHITECTURE_SPEC.md`.

## CodeBTI Profile Concept

CodeBTI should produce memorable profile names, but the profiles must remain engineering-grounded. A profile is a shorthand for a set of design preferences, not a substitute for detailed guidance.

For the initial Python version, define profiles across practical axes such as:

- Abstraction: local and concrete vs. layered and generalized.
- Type discipline: dynamic and pragmatic vs. strict and explicit.
- State model: mutable workflow vs. immutable transformations.
- Error model: exceptions, result objects, validation upfront, or fail-fast.
- Dependency posture: standard-library first vs. ecosystem-friendly.
- Testing style: behavior-first, unit-first, property-based, integration-heavy, or smoke-test oriented.

The current Python taxonomy defines practical profile families such as:

- `Object-Centered Boundary Keeper`
- `Function-First Pipeline Builder`
- `Data-First Validator`
- `Pragmatic Script Builder`
- `Test-First Integrator`
- `Framework-Aligned Builder`
- `Algorithm-First Minimalist`

Use `python/profiles/python-profile-taxonomy.md` as the initial Python taxonomy and refine it as new interview data appears.

## Initial Python Scope

The first version should focus on Python projects, including:

- packages,
- command-line tools,
- data processing scripts,
- APIs,
- notebooks converted into maintainable modules,
- and agent-written project scaffolds.

The Python guidance should cover at least:

- project layout,
- imports,
- typing,
- dataclasses and Pydantic-style models,
- exceptions,
- logging,
- configuration,
- dependency management,
- tests,
- scripts and CLIs,
- docstrings,
- and review expectations.

Do not overfit the system to one framework. Framework-specific guidance should be added as optional extensions.

## Expansion Model

Future languages should be added by creating parallel language folders rather than rewriting the core workflow.

Example:

```text
python/
  questions/
    fixed-python.md
    fixed-typescript.md
  patterns/
    python/
    typescript/
  profiles/
    python-profile-taxonomy.md
    typescript-profile-taxonomy.md
```

The general workflow should stay language-neutral. Language folders should hold language-specific examples, questions, and taxonomy details.

## Agent Behavior Rules

When an agent works in this repository:

- Prefer markdown files over code unless the user explicitly asks for tooling.
- Keep source files readable by both humans and agents.
- Make generated templates structured and easy to fill.
- Avoid vague style advice that cannot guide implementation.
- Include tradeoffs, not just rules.
- Preserve session records as evidence for generated recommendations.
- Treat CodeBTI results as project guidance, not personal judgment.
- Keep Python as the first implementation target while leaving room for other languages.

## Current Definition of Done

The Python-first markdown foundation is ready when it contains:

- root `SKILL.md` as the installable skill entry point,
- this `AGENT.md`,
- a human-facing `README.md`,
- the fixed Python question sheet in `python/questions/`,
- the adaptive question guide in `python/questions/`,
- a pattern index in `python/patterns/`,
- the 22 Python GoF pattern pages in `python/patterns/python/`,
- a profile taxonomy draft in `python/profiles/`,
- a session record template in `python/records/`,
- a `CodeStyle.md` template in `python/templates/`,
- output templates for `SKILL.md` and `SPEC.md` in `python/templates/`,
- a `python/records/` folder with recording guidance,
- and all local markdown links resolving.

With these files present, a user can ask an AI agent to run a CodeBTI interview and receive a useful project-specific `CodeStyle.md`.
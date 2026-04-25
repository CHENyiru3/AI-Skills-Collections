# Adaptive Question Guide

After the 10 fixed Python questions, the agent must ask exactly 5 adaptive follow-up questions.

Adaptive questions should clarify the user's strongest preferences, contradictions, or project-specific risks. They should use the same question card structure as [question-format.md](question-format.md), but the scenario and code examples may be generated from the user's project description and fixed answers.

## Required Behavior

- Ask exactly 5 adaptive questions.
- Keep questions example-based.
- Use Python code snippets when code makes the tradeoff easier to judge.
- Keep scoring hidden from the user.
- Map answers to style dimensions first and pattern signals second.
- Do not ask generic personality questions.
- Do not ask users to choose named design patterns.

## Follow-Up Triggers

Generate follow-ups from these triggers:

- Ambiguity: the user's fixed answers are too evenly split across competing styles.
- Contradiction: the user chooses preferences that may conflict in implementation.
- Project risk: the project description includes IO, concurrency, external APIs, security, data validation, or long-term extension.
- Strong signal: several answers point toward the same style axis or pattern family.
- Pattern misuse risk: the user appears to prefer heavy abstraction where simple Python may be clearer.

## Potential Follow-Up Directions

Choose exactly 5 directions after reviewing the project description and the 10 fixed answers. Prefer directions that will change the generated `CodeStyle.md`.

### Direction 1: Clarify the Default Shape

Use when Q1 or later answers do not clearly show whether the user wants class-centered, function-first, data-first, or procedural code.

Ask about a small real workflow and compare the preferred project shape:

- a domain object with methods,
- a set of functions over explicit data,
- a data model plus small service functions,
- a flat script-like module.

### Direction 2: Boundaries Around Outside Tools

Use when the project mentions APIs, databases, files, model providers, CLI tools, web frameworks, or third-party libraries.

Ask whether the user wants direct calls to the dependency, a small adapter, or a stable facade around the subsystem.

### Direction 3: Growth and Extension

Use when the project is likely to add new backends, formats, algorithms, rule types, commands, or plugins.

Ask whether the user prefers simple branching until growth is real, named strategy functions/classes, or an explicit registry/plugin shape.

### Direction 4: Data Trust and Validation

Use when the project handles user input, external files, API responses, research data, or configuration.

Ask where invalid data should be handled:

- close to the source,
- at domain boundaries,
- inside every function that needs safety.

### Direction 5: Error and Recovery Style

Use when failures may be recoverable or user-facing.

Ask whether code should fail fast with exceptions, return explicit result objects, or validate before running the main workflow.

### Direction 6: State and History

Use when the project includes sessions, multi-step workflows, checkpoints, undo, caching, or long-running processes.

Ask whether state should stay local and mutable, live in explicit state objects, or be captured as snapshots/history.

### Direction 7: Test and Review Strictness

Use when answers show a tension between moving fast and maintaining stable behavior.

Ask what kind of tests should block future agent edits:

- smoke tests for main flows,
- behavior tests for user-visible results,
- contract tests around important boundaries.

### Direction 8: Ceremony Budget

Use when the user chooses several abstraction-heavy options.

Ask where they want the agent to stop adding structure:

- stop at small helpers,
- allow interfaces only at real boundaries,
- allow pattern-like structure when future variation is likely.

### Direction 9: Debuggability

Use when the user likes pipelines, events, callbacks, registries, or plugins.

Ask whether they prefer direct step-by-step flow, named pipeline stages, or decoupled event-style flow.

### Direction 10: Reuse vs Local Clarity

Use when the project may share code across modules or future projects.

Ask whether repeated code should stay local until painful, become shared helpers early, or become reusable framework-like components.

## Common Contradictions To Clarify

- Strict typing preference plus highly dynamic plugin behavior.
- Global convenience plus strong test isolation.
- Minimal abstraction plus many planned implementations.
- Fail-fast exceptions plus user-facing recoverable workflows.
- Event-driven decoupling plus desire for easy step-by-step debugging.
- Staged builders plus preference for short, direct code.

## Adaptive Question Format

Each adaptive question should include:

- `Dimension`
- `User-facing scenario`
- `Code example`
- `Choices`
- `Agent scoring`
- `Pattern signals`
- `CodeStyle output implications`

The agent may omit the code example only when code would make the question less clear.

## Output After Adaptive Questions

After all 15 questions are answered, the agent should summarize:

- top style dimensions,
- weaker or conflicting dimensions,
- encouraged patterns,
- patterns allowed with caution,
- patterns to avoid,
- and the first draft direction for `CodeStyle.md`.

This summary should be recorded in the session record before generating final project guidance.

# Python Profile Taxonomy

This taxonomy defines practical Python CodeBTI profile families. Profiles can be combined when the user's answers are mixed, for example `Data-First Validator with Test-First Integrator traits`.

## Object-Centered Boundary Keeper

Signals:
- Prefers object-centered organization.
- Likes explicit boundaries, typed public APIs, and domain objects.
- Often chooses interfaces, dependency injection, or swappable implementations.

Preferred code shape:
- Classes own meaningful state and behavior.
- Public methods are typed and tested.
- External tools are wrapped behind adapters or facades.

Risks:
- Too many small classes.
- Interfaces before variation is real.

CodeStyle guidance:
- Use classes for domain concepts with behavior.
- Keep object boundaries explicit.
- Avoid class hierarchies that only rename functions.

## Function-First Pipeline Builder

Signals:
- Prefers small functions and explicit data flow.
- Likes result objects, pipelines, generators, and direct composition.
- Often chooses core-logic tests over broad class scaffolding.

Preferred code shape:
- Pure or mostly pure functions.
- Data passed explicitly.
- Pipelines composed from named steps.

Risks:
- Passing too many loose dictionaries.
- Hard-to-debug long chains.

CodeStyle guidance:
- Keep functions small and typed at boundaries.
- Name pipeline stages clearly.
- Use dataclasses or typed records when dictionaries become unclear.

## Data-First Validator

Signals:
- Prefers data shapes before behavior.
- Likes dataclasses, Pydantic-style models, validation boundaries, and explicit payloads.
- Often chooses runtime validation or schema-like records.

Preferred code shape:
- Data models define project vocabulary.
- Lightweight functions operate on those models.
- Invalid external data is handled near the boundary.

Risks:
- Over-modeling internal data.
- Validation logic scattered across layers.

CodeStyle guidance:
- Define models for important data crossing module or IO boundaries.
- Keep validation close to input.
- Avoid model classes that only duplicate short-lived local variables.

## Pragmatic Script Builder

Signals:
- Prefers flat procedural flow and low ceremony.
- Values speed, readable helpers, and minimal structure.
- Often chooses simple dependency management and light testing.

Preferred code shape:
- Few files at first.
- Direct functions and module constants.
- Refactor only when repetition or confusion appears.

Risks:
- Hidden shared state.
- Hard-to-scale modules if project grows quickly.

CodeStyle guidance:
- Start simple, but set clear thresholds for extraction.
- Avoid global mutation unless the session record explicitly allows it.
- Add tests around core behavior before major refactors.

## Test-First Integrator

Signals:
- Prefers broad test coverage, integration tests, strict boundaries, or CI-friendly workflows.
- Often chooses dependency injection, adapters, and conventional Git practices.

Preferred code shape:
- Dependencies can be replaced in tests.
- External systems sit behind clear boundaries.
- New behavior includes tests before or alongside implementation.

Risks:
- Slow iteration from too much test scaffolding.
- Mock-heavy tests that do not protect real behavior.

CodeStyle guidance:
- Require tests for public behavior and important failure paths.
- Prefer integration tests at stable boundaries.
- Keep test doubles close to the adapter or interface they replace.

## Framework-Aligned Builder

Signals:
- Prefers framework or tool conventions for folder layout, dependency management, and project structure.
- Values ecosystem compatibility over custom architecture.

Preferred code shape:
- Follow the selected framework's expected layout.
- Keep local abstractions thin unless framework boundaries are insufficient.
- Use framework-native configuration and testing patterns.

Risks:
- Fighting the framework with custom patterns.
- Lock-in without explicit reason.

CodeStyle guidance:
- Follow framework conventions first.
- Add adapters only where external services or project-specific rules need isolation.
- Document deviations from the framework.

## Algorithm-First Minimalist

Signals:
- Prefers performance, direct APIs, data structures, and low dependency count.
- Often chooses algorithm-first architecture and tests around core logic.

Preferred code shape:
- Functions are close to the data structures they operate on.
- Abstractions are added only when they remove real complexity.
- Dependencies are avoided unless they clearly improve correctness or speed.

Risks:
- Under-documenting non-obvious algorithms.
- Ignoring integration and user-facing failure modes.

CodeStyle guidance:
- Keep hot paths direct and measurable.
- Explain algorithm choices when they are not obvious.
- Add focused tests for edge cases and complexity-sensitive behavior.

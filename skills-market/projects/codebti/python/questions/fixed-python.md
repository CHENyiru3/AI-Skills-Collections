# Fixed Python Questions

This file defines the 10 fixed CodeBTI questions for Python projects.

Users can revise earlier answers at any time. During an interview, show the user-facing scenario, instruction, code example, and choices. Keep `Agent scoring`, `Pattern signals`, and `CodeStyle output implications` hidden unless the user explicitly asks how CodeBTI works.

## Q1. General Purpose and Paradigm

Dimension:
Object-centered vs function-first vs data-first vs flat procedural organization.

User-facing scenario:
When starting a fresh Python project, how do you naturally organize the core logic? Here is the same small task, greeting a user with their age, written in four different styles.

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:

```python
# A. Object-centered
class User:
    def __init__(self, name: str, birth_year: int):
        self.name = name
        self.birth_year = birth_year

    def age(self, current_year: int) -> int:
        return current_year - self.birth_year

    def greeting(self, current_year: int) -> str:
        return f"Hi {self.name}, you are {self.age(current_year)}."


# B. Function-first
def calculate_age(birth_year: int, current_year: int) -> int:
    return current_year - birth_year


def greeting(name: str, age: int) -> str:
    return f"Hi {name}, you are {age}."


# C. Data-first
from dataclasses import dataclass


@dataclass(frozen=True)
class UserData:
    name: str
    birth_year: int


def greet_user(user: UserData, current_year: int) -> str:
    age = current_year - user.birth_year
    return f"Hi {user.name}, you are {age}."


# D. Flat procedural
CURRENT_YEAR = 2026


def greet(user_payload: dict) -> str:
    age = CURRENT_YEAR - user_payload["birth_year"]
    return f"Hi {user_payload['name']}, you are {age}."
```

Choices:
- A. Object-centered: keep state and behavior together in domain objects.
- B. Function-first: use small functions that transform explicit inputs into outputs.
- C. Data-first: define the data shape first, then write lightweight functions around it.
- D. Flat procedural: write a direct flow with simple helpers and module-level constants when useful.

Agent scoring:
- A: Class-friendly, encapsulation-first, comfortable with objects owning behavior.
- B: Stateless, function-first, explicit data flow, prefers easy composition.
- C: Data-shape-first, clear model boundaries, likes immutable or validated records.
- D: Low ceremony, speed-first, comfortable with scripts and direct module flow.

Pattern signals:
- A: Possible [State](../patterns/python/state.md), [Template Method](../patterns/python/template-method.md), [Strategy](../patterns/python/strategy.md) as classes.
- B: Possible [Strategy](../patterns/python/strategy.md) as callables, [Iterator](../patterns/python/iterator.md)/generator pipelines.
- C: Possible [Builder](../patterns/python/builder.md) or [Factory Method](../patterns/python/factory-method.md) only when data construction grows.
- D: Avoid premature GoF patterns; prefer small helpers and clear modules.

CodeStyle output implications:
Use this answer to set the default project shape: class-centered, function-first, data-model-centered, or script/procedure-first. Future guidance should explain when the project may deviate from that default.

## Q2. Defensive Coding and Type Boundaries

Dimension:
Strict static typing vs boundary typing vs runtime validation vs dynamic duck typing.

User-facing scenario:
Python lets you choose how strongly the code checks its own assumptions. For a function that updates a user's age, how strict should the project be?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:

```python
# A. Strict checks
def update_user_age(user_id: int, new_age: int) -> bool:
    if not isinstance(new_age, int):
        raise TypeError("new_age must be an integer")
    if new_age <= 0:
        raise ValueError("new_age must be positive")

    user: dict[str, object] = db_get(user_id)
    user["age"] = new_age
    db_save(user)
    return True


# B. Boundary typing
def update_user_age(user_id: int, new_age: int) -> bool:
    user = db_get(user_id)
    if new_age <= 0:
        return False

    user["age"] = new_age
    db_save(user)
    return True


# C. Runtime validation
from pydantic import BaseModel, Field


class AgeUpdate(BaseModel):
    user_id: int
    new_age: int = Field(gt=0)


def update_user_age(raw_input: dict) -> bool:
    payload = AgeUpdate(**raw_input)
    user = db_get(payload.user_id)
    user["age"] = payload.new_age
    db_save(user)
    return True


# D. Dynamic Python
def update_user_age(user_id, new_age):
    user = db_get(user_id)
    user["age"] = int(new_age)
    db_save(user)
    return True
```

Choices:
- A. Strict checks: use strong type hints and explicit validation in important functions.
- B. Boundary typing: type public functions and module boundaries, but keep internal code flexible.
- C. Runtime validation: use validation models to clean and check incoming data.
- D. Dynamic Python: keep type hints light and trust callers unless a bug proves otherwise.

Agent scoring:
- A: High defensive coding, explicit invariants, stronger static-analysis posture.
- B: Boundary-first discipline, pragmatic internal flexibility.
- C: Validation-first, accepts runtime model libraries and coercion.
- D: Dynamic, low ceremony, duck-typing friendly.

Pattern signals:
- A: Supports explicit interfaces, protocols, strict adapters.
- B: Supports [Facade](../patterns/python/facade.md) and [Adapter](../patterns/python/adapter.md) at boundaries without overtyping internals.
- C: Supports data-first modeling, validation boundaries, [Builder](../patterns/python/builder.md) for complex payloads.
- D: Avoid heavy interface patterns unless project risk demands them.

CodeStyle output implications:
Set typing policy, validation policy, and where agents should add checks. This answer should prevent future code from mixing strict type-heavy style with casual untyped style without a clear boundary.

## Q3. Error Handling and Recovery

Dimension:
Fail-fast exceptions vs safe fallback vs explicit result objects vs batch quarantine.

User-facing scenario:
The project receives transaction payloads from a JSON API. Sometimes `amount` is missing or is a value like `"N/A"`. How should the code handle that kind of bad input?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:

```python
# A. Fail fast
class MalformedTransactionError(ValueError):
    pass


def calculate_total(tx: dict) -> float:
    if "amount" not in tx:
        raise MalformedTransactionError("Transaction is missing amount")
    if not isinstance(tx["amount"], (int, float)):
        raise MalformedTransactionError("Transaction amount must be numeric")
    return tx["amount"] * 1.2


# B. Safe fallback
def calculate_total(tx: dict) -> float:
    try:
        return float(tx.get("amount", 0)) * 1.2
    except (TypeError, ValueError):
        return 0.0


# C. Explicit result
def calculate_total(tx: dict) -> dict:
    amount = tx.get("amount")
    if not isinstance(amount, (int, float)):
        return {"ok": False, "value": None, "error": "Invalid amount"}
    return {"ok": True, "value": amount * 1.2, "error": None}


# D. Log and continue
import logging


def process_batch(transactions: list[dict]) -> list[float]:
    totals = []
    for tx in transactions:
        try:
            totals.append(float(tx["amount"]) * 1.2)
        except (KeyError, TypeError, ValueError) as exc:
            logging.warning("Skipped transaction %s: %s", tx.get("id"), exc)
    return totals
```

Choices:
- A. Fail fast: raise a clear error as soon as invalid data appears.
- B. Safe fallback: return a default value and keep the main flow moving.
- C. Explicit result: return a structured success or failure value instead of raising for expected problems.
- D. Log and continue: record the failure, skip the bad item, and keep processing the rest.

Agent scoring:
- A: Contract-first, correctness over continuity, exception-friendly.
- B: Continuity-first, tolerant fallback style, risk of hiding data quality issues.
- C: Explicit control flow, result-object style, good for recoverable business errors.
- D: Batch-resilient, observability-friendly, good for data pipelines.

Pattern signals:
- A: Supports boundary validation, strict Facades, custom exception hierarchy.
- B: Supports tolerant [Adapter](../patterns/python/adapter.md)/[Facade](../patterns/python/facade.md) behavior but needs clear fallback policy.
- C: Supports functional style, [Command](../patterns/python/command.md) outcomes, explicit workflow states.
- D: Supports pipeline style, [Chain of Responsibility](../patterns/python/chain-of-responsibility.md), quarantine/dead-letter workflows.

CodeStyle output implications:
Define the project-wide error policy so agents do not mix silent defaults, exceptions, result dictionaries, and quarantine behavior randomly.

## Q4. Naming and Readability

Dimension:
Explicit names vs concise idioms vs domain vocabulary vs comment-supported naming.

User-facing scenario:
Names shape how a codebase feels to read. How should variables, functions, and classes be named in this project?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:
None. The choice is about naming style and review expectations.

Choices:
- A. Explicit names: prefer names like `calculate_total_revenue_for_active_users`, even when they are longer.
- B. Concise idioms: allow short common names like `idx`, `req`, `df`, or `cfg` when context is clear.
- C. Domain language: use the terms from the product, business, math, or science domain instead of generic names like `manager` or `handler`.
- D. Short names with explanation: allow shorter names when docstrings or comments explain the reason and context.

Agent scoring:
- A: Readability through explicit naming; tolerates longer lines and less abbreviation.
- B: Context-heavy, idiomatic Python, comfortable with compact local names.
- C: Domain-driven naming, avoids generic service/object vocabulary.
- D: Documentation-supported naming, accepts comments as part of readability.

Pattern signals:
- A: Helps explicit [Facade](../patterns/python/facade.md) and boundary APIs.
- B: Supports function-first and script-like styles.
- C: Supports domain model, domain services, clear ubiquitous language.
- D: Supports comment-guided agent workflows and more verbose generated docs.

CodeStyle output implications:
Set naming rules for functions, classes, modules, variables, and review comments. The generated `CodeStyle.md` should include allowed abbreviations and discouraged generic names.

## Q5. Architecture and Wiring Style

Dimension:
Python language tools vs dependency injection vs swappable patterns vs central registry vs algorithm-first code.

User-facing scenario:
When a project has routing, setup/teardown, services, or multiple implementations, how do you prefer to wire the pieces together?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:
None. This question compares architecture preferences rather than one local code snippet.

Choices:
- A. Python tools: use decorators, context managers, and small wrappers for repeated setup or cleanup.
- B. Passed-in dependencies: pass services, clients, and repositories directly into functions or classes.
- C. Swappable implementations: define clear interfaces so different backends or algorithms can be exchanged.
- D. Central registry: keep shared services in one configured module or object that other code imports.
- E. Algorithm-first: keep abstractions thin and focus on data structures, performance, and direct APIs.

Agent scoring:
- A: Pythonic composition, accepts hidden setup when names and tests are clear.
- B: Testability-first, explicit dependencies, low hidden global state.
- C: Interface-first, extension-friendly, comfortable with pattern-like structure.
- D: Convenience-first, centralized configuration, risk of hidden coupling.
- E: Performance and directness first, avoids architecture ceremony.

Pattern signals:
- A: [Decorator](../patterns/python/decorator.md), context manager patterns, [Proxy](../patterns/python/proxy.md)-like wrappers.
- B: [Adapter](../patterns/python/adapter.md), [Facade](../patterns/python/facade.md), dependency injection, test doubles.
- C: [Strategy](../patterns/python/strategy.md), [Factory Method](../patterns/python/factory-method.md), [Abstract Factory](../patterns/python/abstract-factory.md), [Bridge](../patterns/python/bridge.md).
- D: [Singleton](../patterns/python/singleton.md)/Registry, service locator caution.
- E: Avoid unnecessary GoF structure; prefer clear functions and data structures.

CodeStyle output implications:
Set the default wiring rule: Python wrappers, dependency injection, explicit interfaces, central registry, or algorithm-first direct code. Include caution rules for hidden state and over-abstraction.

## Q6. Folder Structure

Dimension:
Feature folders vs technical layers vs flat source tree vs framework/tool-driven layout.

User-facing scenario:
As the codebase grows from one file to many files, what structure should agents use by default?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:

```text
# A. Feature folders
src/users/
src/billing/
src/reports/

# B. Technical layers
src/models/
src/services/
src/routes/

# C. Flat until needed
src/
  users.py
  billing.py
  reports.py

# D. Tool or framework layout
src/<framework-or-template-convention>/
tests/
docs/
```

Choices:
- A. Feature folders: group files by product area or domain, with each area owning its local models, services, and routes.
- B. Technical layers: group files by role, such as models, services, routes, data, and tests.
- C. Flat until needed: keep files in a simple `src/` layout until nesting clearly helps.
- D. Tool or framework layout: follow the structure expected by the chosen framework, package tool, or template.

Agent scoring:
- A: Domain/feature isolation, modular ownership, good for growing products.
- B: Layered architecture, conventional separation by technical role.
- C: Minimal structure, low import complexity, refactor when pain appears.
- D: Convention-first, values compatibility with tools and ecosystem expectations.

Pattern signals:
- A: Supports bounded contexts, [Facade](../patterns/python/facade.md) per feature, local adapters.
- B: Supports service-layer and MVC-like organization.
- C: Supports procedural/function-first code and low abstraction.
- D: Supports framework-aligned design and template-driven structure.

CodeStyle output implications:
Define where agents should create new modules and when they may introduce subfolders. Include source-vs-local-data separation when relevant.

## Q7. Testing Philosophy

Dimension:
Test-first coverage vs integration confidence vs core-logic focus vs manual/log-driven iteration.

User-facing scenario:
Tests take time to write and maintain. What level of testing should be the default for this project?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:
None. The choice is about testing scope and review expectations.

Choices:
- A. Test-first and broad coverage: write tests early and cover branches, edge cases, and important failure paths.
- B. Integration-heavy: focus on endpoints, database boundaries, CLI flows, or full workflows.
- C. Core logic only: test custom algorithms and business rules, but avoid testing framework boilerplate.
- D. Manual and logs first: move fast, test manually, and rely on logs or user feedback until the project stabilizes.

Agent scoring:
- A: High test discipline, regression prevention, slower but safer changes.
- B: Behavior and boundary confidence, less interest in unit-testing every helper.
- C: ROI-focused testing, protects custom logic while avoiding low-value tests.
- D: Prototype speed, low automated-test expectation, higher regression risk.

Pattern signals:
- A: Supports contract tests, adapters, strict interfaces.
- B: Supports [Facade](../patterns/python/facade.md)/API testing and integration boundaries.
- C: Supports algorithm-first and function-first testing.
- D: Avoid heavy abstractions that require extensive test scaffolding.

CodeStyle output implications:
Set minimum test requirements for generated code and future agent edits. Define whether new features need unit tests, integration tests, smoke tests, or manual verification notes.

## Q8. Comments and Docstrings

Dimension:
Self-documenting code vs why-focused comments vs strict docstrings vs AI-facing context comments.

User-facing scenario:
AI agents can over-explain code. What comment and docstring style should this project enforce?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:
None. The choice is about comment policy and documentation density.

Choices:
- A. Minimal comments: code should be clear enough that comments are rare; docstrings are mainly for public APIs.
- B. Explain why: avoid comments that repeat the code, but explain business rules, constraints, and non-obvious decisions.
- C. Full docstrings: use a consistent docstring style for most classes, methods, and functions.
- D. AI context comments: allow comments as planning markers or context for future agent edits when they reduce confusion.

Agent scoring:
- A: Self-documenting preference, low comment density.
- B: Context-first comments, moderate docstrings, strong review value.
- C: Documentation-heavy, API-reference friendly, higher maintenance cost.
- D: Agent-collaboration friendly, accepts comments as future-edit guidance.

Pattern signals:
- A: Works best with clear names and small functions.
- B: Supports domain-driven rules and boundary documentation.
- C: Supports public library/API style and strict interfaces.
- D: Supports agent workflows, planning/spec markers, and guided refactors.

CodeStyle output implications:
Define when agents should add comments, docstrings, planning notes, and context markers. Also define what kinds of comments should be removed during cleanup.

## Q9. Git History and Collaboration

Dimension:
Fast mainline commits vs conventional PR flow vs release branches vs linear history vs no Git preference.

User-facing scenario:
When humans and AI agents generate code together, what should the Git history and branching style look like?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:
None. The choice is about collaboration workflow, not Python code.

Choices:
- A. Fast mainline: commit directly to `main` or one shared `dev` branch with short descriptive messages.
- B. Conventional branches: use feature branches, pull requests, and messages like `feat:`, `fix:`, and `refactor:`.
- C. Release branches: keep `main` production-focused, use integration and release branches, and isolate hotfixes.
- D. Linear history: squash or rebase so history reads as a clean sequence without merge commits.
- E. No strong Git preference: keep Git requirements light and do not make workflow a major constraint.

Agent scoring:
- A: Speed-first collaboration, lower process overhead.
- B: Conventional, review-friendly, automation-friendly.
- C: Release-management discipline, stronger environment separation.
- D: History cleanliness, prefers curated commits.
- E: Git-light, likely needs minimal agent assumptions.

Pattern signals:
- A: Supports rapid prototyping and direct edits.
- B: Supports review checklists, CI, and structured agent commits.
- C: Supports release management specs and deployment gates.
- D: Supports polished patch sets and careful refactors.
- E: Avoid over-specifying Git behavior in generated style files.

CodeStyle output implications:
Set commit-message, branch, PR, and history expectations for future agent work. If E is chosen, keep Git guidance minimal.

## Q10. Dependencies and Environments

Dimension:
Standard pip/venv vs conda environments vs lockfile package managers vs newer Rust-based tooling.

User-facing scenario:
Python dependency management can shape the whole project. How should environments and third-party libraries be managed?

User-facing instruction:
Choose the style you would most naturally want to maintain. You can revise earlier answers at any time.

Code example:

```text
A. requirements.txt + venv
B. environment.yml + conda/miniconda
C. pyproject.toml + poetry.lock or Pipfile.lock
D. pyproject.toml / uv.lock / inline script metadata
```

Choices:
- A. Standard `pip` and `venv`: keep setup simple with `requirements.txt` and built-in virtual environments.
- B. Conda-style environment: use `conda` or `miniconda` when data science packages or native dependencies matter.
- C. Lockfile package manager: use Poetry or Pipenv for structured config and reproducible lock files.
- D. Newer fast tooling: use tools like `uv` or `rye` for fast resolution and modern Python project workflows.

Agent scoring:
- A: Minimal tooling, broad compatibility, simple setup.
- B: Data-science friendly, native dependency aware, environment-file centered.
- C: Reproducibility-first, structured project metadata, lockfile discipline.
- D: Modern tooling preference, speed-first dependency management.

Pattern signals:
- A: Supports lightweight scripts and simple packages.
- B: Supports research/data workflows and environment-heavy projects.
- C: Supports package/library style and CI reproducibility.
- D: Supports modern agent workflows and fast iteration.

CodeStyle output implications:
Set dependency policy, environment files, install commands, and whether agents may add new libraries. Include the preferred source of truth for dependencies.

# Design Pattern Database

This folder is the CodeBTI design pattern database. Agents should use it to translate a user's style preferences into concrete project guidance, not as a generic textbook.

The first database is Python-focused and mirrors the classic GoF pattern catalog used by RefactoringGuru. CodeBTI guidance is original and agent-facing: it explains when a pattern preference is useful, when it becomes overengineering, and what it implies for generated code.

## Source Attribution

The Python catalog structure and source references are based on:

- RefactoringGuru Design Patterns in Python: https://github.com/RefactoringGuru/design-patterns-python
- RefactoringGuru Python catalog: https://refactoring.guru/design-patterns/python
- License: Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International, https://github.com/RefactoringGuru/design-patterns-python/blob/main/LICENSE.txt
- Authors listed upstream: Alexey Pyltsyn and Alexander Shvets.

Do not copy large upstream examples into CodeBTI. Link to the original examples and write CodeBTI-specific guidance in our own words.

## Python Pattern Index

See [patterns/python/README.md](python/README.md) for the Python database.

## Agent Use

During a CodeBTI interview, use these pages to identify style signals:

- A user who prefers explicit families of related components may lean toward Abstract Factory.
- A user who wants flexible algorithm choice may lean toward Strategy.
- A user who dislikes hidden global state should usually avoid Singleton.
- A user who wants simple public entrypoints around complex internals may lean toward Facade.

Pattern fit is evidence, not identity. A generated `CodeStyle.md` should say which patterns are encouraged, which are allowed with caution, and which should be avoided for the project.

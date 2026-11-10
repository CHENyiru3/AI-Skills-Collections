---
name: setting-up-python-libraries
domain: programming
description: Scaffold a new Python library or modernize its package structure and selected tooling. Use for explicit setup work; preserve an existing project’s backend, Python support and conventions unless migration is requested.
metadata:
  version: "1.0.1"
---

# Python Library Setup

Establish the package purpose, distribution/import names, Python support, license
and destination from the request or existing repository. Select only the tooling
needed for the project; src layout, a Makefile, strict types and pre-commit are
choices rather than universal acceptance gates.

For a new library, keep package discovery and import names consistent with metadata.
Use a real license text selected for the project; an `MIT License` heading alone is
not a license. Declare the tools invoked by setup/CI and avoid embedding unescaped
author input into TOML. Include data/type markers only when the distribution uses them.

The bundled starter is optional:

```bash
python scripts/create_project.py my-library --author "Name" --directory /chosen/parent
```

It creates a new directory and refuses an existing target. Its MIT license, Python
floor and sample tool stack are starter defaults to adapt, not instructions to
replace an existing project. Review the generated diff before installing hooks or
running its remote CI. The helper does not install dependencies itself.

Read [PYPROJECT.md](PYPROJECT.md) for relevant packaging fields, [CI.md](CI.md)
for a requested CI/hook setup and [MAKEFILE.md](MAKEFILE.md) for command automation.
Verify version-sensitive examples against the chosen backend/actions.

For modernization, preserve user files and migrate only the requested pieces.
Validate generated metadata, package discovery and the relevant build/import or
check commands in an isolated environment. Stop when the selected scaffold/setup
works; global configuration, publication and every optional tool are not implied.

---
name: packaging-python-libraries
domain: programming
description: 'Build, inspect or repair an installable Python distribution: metadata, wheels, source archives and package data. Use for packaging work; publication to an index requires that requested scope, and an unrelated pyproject edit does not trigger this workflow.'
metadata:
  version: "1.0.1"
---

# Python Packaging

Inspect the existing backend, metadata/version source, supported Python versions
and intended distribution files. Preserve the backend unless a migration is part
of the task. Distribution names and import names can differ; test the installed
package rather than assuming the repository directory is the import contract.

Build in an appropriate isolated environment. If using the common PyPA tools,
`python -m build` needs `build`, and `python -m twine check` needs `twine` installed
there. Inspect only the artifacts from this build, not a wildcard over stale `dist/`.
A build executes backend hooks; treat unfamiliar projects accordingly.

Verify metadata and archive contents: importable modules, required data, license
files, optional extras and compiled-extension/platform tags where relevant. Test a
wheel in a clean environment outside the source tree. For an sdist, verify the
needed build inputs are included. An editable import alone does not prove either.

Keep declared requirements compatible with actual support: minimums, upper bounds
and exact pins need a concrete reason; lockfiles and library dependency ranges
serve different purposes. Declare optional capabilities without making ordinary
imports depend on an uninstalled extra.

Use [PYPROJECT_FULL.md](PYPROJECT_FULL.md) for a relevant metadata pattern and
[CONDA.md](CONDA.md) only for Conda packaging. Check evolving metadata/licensing
syntax against the chosen backend's version before reusing templates.

Preparing artifacts does not imply uploading to TestPyPI, PyPI or GitHub. For a
requested publication, confirm the index/project identity, exact artifacts and
existing authorization; prefer configured protected credentials or supported
trusted publishing without putting secrets in commands/output. Inspect current
provider documentation for action inputs and token scopes.

Report artifacts and verification, then stop at the requested packaging or
publication outcome. Reference: [PyPA packaging guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

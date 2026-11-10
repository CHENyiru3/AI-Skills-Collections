---
name: documenting-python-libraries
domain: programming
description: Write or repair Python package docstrings, usage guides, API references or documentation builds. Use for an explicit package documentation task; a product mention alone does not require Sphinx or deployment setup.
metadata:
  version: "1.0.1"
---

# Python Package Documentation

Use the project's existing documentation system and docstring convention. Start
with the user's audience and the specific missing or incorrect contract; one
function's docstring does not require rebuilding the whole documentation stack.

Document accepted inputs, shapes/units, return ownership, side effects and meaningful
errors. Keep examples aligned with real exports and installed versions. Label
illustrative values; do not invent benchmark outputs or suggest placeholders were
executed. Distinguish optional extras from ordinary install requirements.

For a tutorial, choose a runnable path through the intended task and explain its
important assumptions. For a reference, document actual behavior rather than an
aspirational interface. Public API completeness is relevant to a full reference
request, not a prerequisite to correcting one page.

Read [SPHINX_CONFIG.md](SPHINX_CONFIG.md) only for Sphinx configuration and
[TUTORIALS.md](TUTORIALS.md) for a substantial tutorial. Check current extension and
hosting inputs before changing a build; importing modules for autodoc can execute
package code. Use the existing isolated development environment where appropriate.

Validate affected links, example calls and the relevant doc build when available.
Report unavailable dependencies and existing warnings accurately. Publishing to
Read the Docs or another host is separate from preparing a local documentation
change. Stop when the requested documentation is correct and reviewable.

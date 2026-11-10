---
name: jupyter
domain: programming
description: Inspect, edit, execute or convert a Jupyter .ipynb artifact when notebook-specific cell, output or metadata handling is needed. Reading/editing does not imply executing cells or overwriting the source notebook.
metadata:
  version: "1.0.1"
---

# Jupyter Notebook Work

Identify the requested notebook, operation and output path. Separate inspection,
structural editing, conversion and execution; a notebook can execute arbitrary code
and access the selected kernel's files/network.

Prefer notebook-aware libraries such as nbformat for edits. Preserve the notebook
format/minor version, cell IDs, metadata and cell order. Use the format's cell
constructors and validate the result rather than inserting incomplete raw JSON.
When code changes, clear only its stale outputs/execution counts as appropriate;
do not erase unrelated results merely for a cosmetic edit.

Execution requires that scope in the request and an appropriate kernel/environment.
Inspect code and dependencies before running an unfamiliar notebook. Use a separate
output path or a working copy by default; in-place execution can destroy useful
outputs. Bound execution time and report the actual failing cell/status. Do not
turn an execution error into a successful run by silently allowing errors.

For conversion, confirm whether outputs/assets, interactive widgets or raw cells
survive the target format. Verify the changed artifact with notebook validation
and inspect representative rendered output when layout matters. Report unexecuted
cells and unavailable dependencies. Stop at the requested notebook operation.

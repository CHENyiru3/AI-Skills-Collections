---
name: latex
domain: writing
description: Compile or troubleshoot an existing LaTeX project and verify its PDF, logs and references. Use for an explicit TeX build task; not creating a new paper template, renaming bibliographies or changing global editor settings.
allowed-tools: Bash(latexmk*), Bash(xelatex*), Bash(pdflatex*), Bash(biber*), Bash(bibtex*), Bash(mkdir*), Bash(ls*), Read, Write, Edit
argument-hint:
- tex-file-path
metadata:
  version: "1.0.1"
---

# LaTeX Compilation

Identify the main document, working directory, engine and bibliography workflow
from project files/configuration. Respect the journal/class and existing latexmk
or editor settings; a package already loaded by the class may conflict with a new
load. Inspect an unfamiliar latexmkrc before execution because it contains Perl.
Do not enable shell escape merely to bypass a build failure.

Prefer the project's existing build command. If choosing an engine, inspect actual
requirements such as fontspec/Unicode, class directives and existing configuration;
fontspec may work with XeLaTeX or LuaLaTeX, so do not infer one engine universally.
Use latexmk when available for dependency-aware reruns; otherwise run the necessary
engine/bibliography passes and inspect the logs.

Distinguish biblatex/Biber from BibTeX/natbib and use the real bibliography filename,
style and output directory. Preserve supplied records and verify any new citation
metadata against a primary bibliographic source rather than fabricating it from
memory. Formatting existing references does not require installing a library tool.

Use the project's build directory or a requested destination. Do not force `out/`,
copy every PDF into the source directory, install missing template skills, or modify
global VS Code settings. For Overleaf, its documented project configuration is named
`latexmkrc` without a leading dot; verify the relevant hosted/local behavior before
assuming files are ignored or synchronized.

## Establish a fresh result

Check the actual process status, current build log and expected PDF. A pre-existing
PDF is not evidence that a failed run succeeded. Copy a deliverable only after a
successful build and bind it to that main document, not `out/*.pdf` in a Perl END
hook that also executes after failures.

Inspect undefined citations/references, duplicate labels, missing glyphs/assets and
consequential overfull boxes. Re-run only when dependencies/auxiliary state require
it. Render affected pages when layout matters, and report unresolved warnings or
missing dependencies with their effects.

Stop when the requested PDF/build repair has current evidence. Do not redesign
the paper, replace its bibliography conventions or install an entire TeX distribution
as an automatic prerequisite.

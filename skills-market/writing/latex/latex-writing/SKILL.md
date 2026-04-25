---
name: latex-writing
description: |
  Guide LaTeX document authoring following best practices, proper semantic 
  markup, academic writing standards, and rigorous mathematical typesetting. 
  Use proactively when: (1) writing or editing .tex files, (2) writing 
  or editing .nw literate programming files, (3) literate-programming skill is 
  active and working with .nw files, (4) user mentions LaTeX, BibTeX, math 
  formatting, or academic writing, (5) reviewing LaTeX code quality. Ensures 
  proper use of semantic environments (description vs itemize), csquotes 
  (\enquote{} not ``...''), cleveref (\cref{} not \S\ref{}), amsmath 
  environments, and formal academic tone.
---

# LaTeX Writing Best Practices

This skill guides the creation of well-structured, semantically correct LaTeX documents following established best practices for academic and technical writing.

## Core Principle: Semantic Markup

Use LaTeX environments that match the semantic meaning of the content, not just the visual appearance. Let LaTeX handle the typography; you handle the structure.

## Academic Writing Standards

When drafting academic papers, reports, or documentation, the prose must be clear, objective, and precise.

### Tone and Style
- **Avoid colloquialisms and contractions**: Use "do not" instead of "don't", and "establish" instead of "set up".
- **Objective voice**: Minimize first-person pronouns ("I", "we") unless describing specific novel actions taken by the authors (e.g., "We propose a new algorithm...").
- **Tense consistency**: 
  - Use **present tense** for general truths, describing what the paper does, and referencing figures/tables (e.g., "Section 2 describes...", "Figure 3 illustrates...").
  - Use **past tense** for describing the specific experiments you ran or past related work (e.g., "Smith et al. demonstrated...", "The system processed 500 requests...").

### Paragraph Structure
- **One idea per paragraph**: Begin with a clear topic sentence.
- **Signposting**: Use transition words (e.g., *Furthermore*, *Consequently*, *However*) to guide the reader through logical arguments.

## Mathematics and Equations

Mathematical typesetting requires strict adherence to `amsmath` best practices to ensure readability and correct spacing. 

### Display Math: Numbered vs. Unnumbered
- **Never** use `$$...$$` for display equations in LaTeX. It is a plain TeX primitive that breaks vertical spacing.
- Use `\[ ... \]` for unnumbered display equations.
- Use the `equation` environment for numbered, single-line equations.

**Anti-pattern**: Plain TeX display math
```latex
% INCORRECT
The formula is:
$$ E = mc^2 $$

```

**Correct**: LaTeX display math

```latex
% CORRECT
The formula is
\[
  E = mc^2
\]

```

### Multi-line Equations (`align` vs `eqnarray`)

* **Always** use the `align` (or `align*`) environment from the `amsmath` package for multi-line equations.
* **Never** use `eqnarray`, as it is obsolete and produces inconsistent spacing around the equals sign.

**Anti-pattern**: Using eqnarray

```latex
% INCORRECT
\begin{eqnarray}
  y &=& mx + c \\
  f(x) &=& x^2 + 2x + 1
\end{eqnarray}

```

**Correct**: Using align

```latex
% CORRECT
\begin{align}
  y &= mx + c \\
  f(x) &= x^2 + 2x + 1
\end{align}

```

### Punctuating Equations

Equations are part of the sentence structure. They must be punctuated appropriately (with commas or periods) just like regular text.

```latex
% CORRECT
We define the objective function as
\begin{equation}
  J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)})^2, \label{eq:cost}
\end{equation}
where $m$ is the number of training examples, and $\theta$ represents the parameters.

```

### Text Inside Math

Always use `\text{...}` (from `amsmath`) or `\mathrm{...}` for words or roman text inside math mode. Variables are italicized; plain text and multi-letter function names (like sin, cos, variance) should not be.

```latex
% INCORRECT
$variance = \sum (x - \mu)^2$
$Rate_{initial} = 5$

% CORRECT
$\mathrm{Var}(X) = \sum (x - \mu)^2$
$R_{\text{initial}} = 5$

```

## List Environments: When to Use What

### Use `description` for Term-Definition Pairs

When you have labels followed by explanations, definitions, or descriptions, use the `description` environment:

```latex
\begin{description}
\item[Term] Definition or explanation of the term
\item[Label] Content associated with the label
\item[Property] Description of the property
\end{description}

```

**NEVER do this:**

```latex
\begin{itemize}
\item \textbf{Term:} Definition or explanation
\item \textbf{Label:} Content associated with label
\end{itemize}

```

### Common Use Cases for `description`

* **API parameters**: `\item[username] The user's login name`
* **Configuration options**: `\item[timeout] Maximum wait time in seconds`
* **Glossary entries**: `\item[LaTeX] A document preparation system`
* **Passes/Fails examples**: `\item[Passes] Correct implementation...`
* **Variable definitions**: Explaining terms immediately following an equation.

### Use `itemize` for Simple Lists

Use `itemize` when items are uniform list elements without labels.

### Use `enumerate` for Numbered Steps or Rankings

Use `enumerate` when chronological order or rank matters.

## Fixing Common Anti-Patterns

### Anti-Pattern: Manual Formatting Instead of Semantic Structure

```latex
% INCORRECT
\noindent\textbf{Configuration:} Set timeout to 30 seconds.\\
\textbf{Performance:} Optimized for large datasets.

```

### Correct: Semantic Description

```latex
% CORRECT
\begin{description}
\item[Configuration] Set timeout to 30 seconds
\item[Performance] Optimized for large datasets
\end{description}

```

## Literate Programming (.nw files)

**CRITICAL**: When writing LaTeX in literate programming files (.nw), use noweb's `[[code]]` notation for quoting code, not `\texttt` with manual escaping.

### Use `[[code]]` Notation, Not `\texttt{...\_...}`

**Anti-pattern**: Manual underscore escaping with `\texttt`

```latex
% INCORRECT - in .nw files
The \texttt{get\_submission()} method calls \texttt{\_\_getattribute\_\_}.

```

**Correct**: Use `[[code]]` notation

```latex
% CORRECT - in .nw files
The [[get_submission()]] method calls [[__getattribute__]].

```

## Additional Best Practices

### Cross-References

* **Always** use `\cref{...}` (cleveref package) for all cross-references.
* **Never** use `\S\ref{...}` or manually type section/figure/equation prefixes.
* Examples:
* Sections: `\cref{sec:background}` → "Section 2.1"
* Figures: `\cref{fig:diagram}` → "Figure 3"
* Equations: `\cref{eq:cost}` → "Equation 1"
* Multiple: `\cref{sec:intro,sec:conclusion}` → "Sections 1 and 4"



### Citations

* Use proper citation commands (`\cite`, `\citep`, `\citet`) not manual references.
* In academic writing, citations should generally be placed *before* punctuation: `...end of the sentence \citep{smith2020}.`

### Quotations (csquotes package)

* **Always** use `\enquote{...}` for quotes, never manual quote marks.
* Handles nested quotes automatically: `\enquote{outer \enquote{inner} quote}`.

### Emphasis

* **Never** use ALL CAPITALS for emphasis in running text.
* Use `\emph{...}` to emphasize words or phrases. Let LaTeX handle the typographic styling (usually italics).

### Floats: Figures and Tables

**Core principle**: An image is not a figure, but a figure can contain an image. Use proper figure and table environments with captions and labels.

#### Using sidecaption (memoir class)

When using the memoir document class, prefer `sidecaption` over traditional `\caption` for better layout and accessibility:

```latex
\begin{figure}
  \begin{sidecaption}{Clear description of image content}[fig:label]
    \includegraphics[width=0.7\textwidth]{path/to/image}
  \end{sidecaption}
\end{figure}

```

## Workflow for Writing LaTeX

When writing or editing LaTeX content:

1. **Check file type**: Are you in a .nw literate programming file? If yes, use `[[code]]`.
2. **Review Academic Tone**: Is the language objective, precise, and using consistent tenses?
3. **Identify content structure**: Is this a list of uniform items or term-definition pairs?
4. **Choose semantic environment**: Match the environment to the content meaning.
5. **Format Math Rigorously**: Ensure all equations are punctuated and use `amsmath` environments (`align`, `\[ \]`).
6. **Verify cross-references**: Ensure labels and references are descriptive and use `\cref`.

## When Reviewing LaTeX Code

Check for these common issues:

* [ ] Colloquial language or inconsistent tense usage.
* [ ] Use of `$$...$$` instead of `\[ ... \]`.
* [ ] Use of `eqnarray` instead of `align`.
* [ ] Equations missing terminal punctuation (periods/commas).
* [ ] Lists using `\textbf{Label:}` instead of `description` environment.
* [ ] Hard-coded prefixes (`Section~\ref`, `Eq~\ref`) instead of `\cref`.
* [ ] Manual quotes (`"..."`) instead of `\enquote{...}`.
* [ ] `\texttt{..._...}` in `.nw` files instead of `[[...]]`.

## Standard Preamble

For new LaTeX documents, use the standard preamble from `references/preamble.tex`. Copy it verbatim to your project's `doc/preamble.tex` and include it with `\input{preamble}` after `\documentclass`.


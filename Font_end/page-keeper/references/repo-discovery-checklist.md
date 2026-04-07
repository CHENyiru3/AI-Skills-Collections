# Repo Discovery Checklist

Use this checklist before asking the user any questions.

## 1. Detect the stack

Look for:
- `package.json`
- `pyproject.toml`
- `_config.yml`
- `config.toml`
- `hugo.toml`
- `astro.config.*`
- `next.config.*`
- plain `index.html`

Classify the site as one of:
- Jekyll
- Hugo
- Astro
- Next.js static site
- plain static site
- custom setup

## 2. Map routes and content sources

Identify:
- homepage/about page
- projects listing and project detail pages
- publications page
- CV/resume page
- blog/news pages
- personal/life pages
- 404 and utility pages

Find where the content actually lives:
- route pages
- collections
- markdown folders
- data files

## 3. Map shared renderers

Find:
- layouts
- includes or partials
- reusable components
- shared publication renderers
- shared card renderers
- shared profile or metadata blocks

Always check whether content shown in multiple places is driven by one shared file.

## 4. Map configuration

Look for site-wide settings such as:
- title and identity
- social links
- CV/resume filename
- asset paths
- feature flags
- collection definitions
- bibliography configuration

## 5. Inspect data-driven sections

Check whether structured content comes from:
- YAML
- JSON
- TOML
- BibTeX
- markdown front matter

Examples:
- publications
- CV entries
- social links
- timeline data
- repositories

## 6. Identify formatting contracts

Look for rules such as:
- publication grouping by year/category/status
- accepted manuscript ordering
- author notation
- conference poster labeling
- exact section names
- degree or affiliation formatting
- date extraction from filenames
- asset naming conventions

## 7. Detect duplication and drift risks

Find:
- content duplicated across homepage and dedicated pages
- repeated inline styles that could drift
- hardcoded values duplicated across files
- derived values that should come from config or filenames

## 8. Classify sections by risk

For each visible section, determine whether it appears to be:
- safe to polish
- sensitive
- fact-heavy
- highly styled
- likely exact-wording
- likely shared across multiple pages

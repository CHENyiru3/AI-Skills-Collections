# Sphinx Configuration

Use this starter when building Python library docs with autodoc and Markdown support.

```python
project = "my-package"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "myst_parser",
    "sphinx_copybutton",
]
templates_path = ["_templates"]
exclude_patterns = ["_build"]
html_theme = "furo"
autodoc_typehints = "description"
napoleon_google_docstring = True
napoleon_numpy_docstring = False
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}
```

## Recommended Layout

- `index.md` for the landing page
- `api.md` for generated API docs
- `guides/` for tutorials and recipes

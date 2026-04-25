# Full pyproject.toml Example

```toml
[build-system]
requires = ["setuptools>=69", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "my-package"
version = "0.1.0"
description = "Short description"
readme = "README.md"
requires-python = ">=3.10"
license = {text = "MIT"}
authors = [{name = "Your Name"}]
dependencies = []

[project.optional-dependencies]
dev = ["pytest>=8", "ruff>=0.4", "mypy>=1.8"]
docs = ["sphinx>=7", "furo>=2024.0", "myst-parser>=2.0"]

[project.urls]
Homepage = "https://github.com/user/my-package"
Documentation = "https://my-package.readthedocs.io"
Issues = "https://github.com/user/my-package/issues"

[tool.pytest.ini_options]
testpaths = ["tests"]

[tool.ruff]
line-length = 88

[tool.mypy]
python_version = "3.10"
```

# Typer Guide

Typer is a good fit when the codebase already leans on type hints and the CLI is not deeply custom.

## When to Choose Typer

- You want signatures to map directly to CLI options.
- You prefer automatic help text from annotations.
- You want lower ceremony for medium-sized tools.

## Minimal Example

```python
import typer

app = typer.Typer()


@app.command()
def process(input_file: str, verbose: bool = False) -> None:
    if verbose:
        typer.echo(f"Processing {input_file}")


if __name__ == "__main__":
    app()
```

## Decision Rule

- Choose Click when the CLI already uses it or needs advanced customization.
- Choose Typer when you want a modern typed wrapper and faster implementation.
- Use `argparse` only when avoiding dependencies matters more than ergonomics.

# Click Patterns

## Recommended Structure

- Keep the root command light.
- Use subcommands for verbs such as `build`, `validate`, `publish`, or `sync`.
- Put shared options on the group only when they genuinely apply everywhere.

## Context Object

Use `@click.pass_context` or `@click.pass_obj` for shared configuration rather than globals.

## Input and Output

- Accept `-` for stdin and stdout where streaming makes sense.
- Send normal output to stdout and diagnostics to stderr.
- Return non-zero exit codes for invalid input or operational failures.

## UX Defaults

- Support `--help` and `--version`.
- Prefer explicit option names over single-letter aliases unless they are common.
- Keep command names consistent in tense and style.

## Testing

- Use `CliRunner` for command behavior.
- Test both success and failure paths.
- Check exit codes, stderr, and output files.

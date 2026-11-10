---
name: building-python-clis
domain: programming
description: Create, change or test a Python command-line interface, including arguments, streams and exit behavior. Use for Python CLI development with the chosen framework; not merely running a command-line tool.
metadata:
  version: "1.0.1"
---

# Python CLI Development

Use the existing argparse, Click or Typer stack when practical. Select a new
framework from dependency constraints and required interaction, not a universal
preference. Match the command's install/entry-point contract to package metadata.

Define the command as a process interface:

- Keep machine-readable results on stdout and diagnostics/progress on stderr.
  Use nonzero status for failures and avoid contaminating piped data with banners.
- Define whether `-` means stdin/stdout; a path type requiring an existing file
  does not automatically implement stream support.
- Make overwrite and destructive behavior explicit. Parse/validate arguments
  before opening an output file that could truncate user data.
- Preserve documented flags, defaults and exit codes when changing an interface.
  Obtain the version from package metadata rather than duplicating release values.
- Declare a CLI framework as a runtime dependency if the ordinary console entry
  point imports it; optional extras need a deliberate missing-extra experience.

For Click-specific patterns read [CLICK_PATTERNS.md](CLICK_PATTERNS.md); for Typer
read [TYPER_GUIDE.md](TYPER_GUIDE.md). Verify version-sensitive completion and test
runner APIs against the installed version before copying examples.

Test the changed command through its public entry point: `--help`, a representative
success and an important failure. Use a temporary filesystem and create real input
fixtures before invoking an existing-path argument. Test stdin only when the command
supports it. Check stream separation and exit status, not just a substring in output.
Do not write shell startup files or install completion unless requested.

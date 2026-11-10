# Optional ZotPilot setup

Use only for a requested ZotPilot installation/configuration. First discover existing
Zotero connectors and CLI versions; library search does not automatically need a new
index or another client registration. Reuse configured access where sufficient.

1. Check the package's current Python/dependency requirements and selected environment.
   Inspect the bundled `pyproject.toml`; do not install global prerequisites silently.
2. For the explicit CLI installation, the wrapper supports:

   ```bash
   python scripts/run.py --install status --json
   ```

   Ordinary `status`/help never installs or upgrades. The installation uses uv's
   isolated tool environment and does not fall back to installing into system Python.
   Compare versions/content before replacing an existing installation.
3. For setup, inspect the installed `zotpilot setup --help`. Establish the actual
   Zotero data directory/library and choose the requested provider. Local embeddings
   may need an initial model download; cloud embeddings send library-derived content
   to that provider. Agree on provider and item scope before indexing private material.
4. Keep API keys in the host's configured protected credential/environment mechanism,
   rather than chat, command arguments or shell history. Library writes need suitable
   Zotero API access and the real numeric user/library identity where that API requires it.
5. Register only the intended client, preserving other MCP entries:

   ```bash
   python scripts/run.py register --platform codex
   ```

   Check `register --help` for the supported platform spelling before running it.
   Reload/restart the affected connection if required; tool availability is the evidence
   that registration worked, not a blanket demand to restart every agent.
6. Index only if the requested search needs it and within the agreed item/provider
   scope. Check status/partial failures; do not force a whole-library rebuild merely
   because one item is absent. Verify the original requested library operation.

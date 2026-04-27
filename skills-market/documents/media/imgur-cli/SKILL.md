---
name: imgur-cli
domain: documents
description: Upload or delete images through the locally installed `imgur` command from `@rasch/imgur-cli`. Use when the user wants to send a local image file or remote image URL to Imgur, retrieve the public link plus `deletehash`, remove a prior upload by `deletehash`, or verify/troubleshoot the local Imgur CLI installation.
---

# imgur-cli

Use the local binary at `~/.local/bin/imgur`.

## First Check

Before using the tool:

```bash
command -v imgur
imgur --help
```

If `imgur` is missing from `PATH`, use the absolute path:

```bash
$HOME/.local/bin/imgur --help
```

## Core Commands

```bash
imgur <url|path>
imgur del <deletehash>
```

The CLI prints plain text, not JSON. Successful uploads print the public Imgur link and then `deletehash: <value>`.

## Workflow

Prefer this sequence:

1. Check that the input is either a reachable image URL or an existing local file.
2. Run `imgur <url|path>`.
3. Return both the Imgur link and the `deletehash` to the user.
4. Tell the user to keep the `deletehash` if they may want to remove the upload later.
5. For deletion requests, run `imgur del <deletehash>` and confirm the success message.

## Authentication

The upstream CLI ships with a default anonymous Imgur client ID. Override it when needed:

```bash
IMGUR_CLIENTID=<client-id> imgur path/to/image.png
```

If uploads fail with authorization or rate-limit issues, retry with an explicit `IMGUR_CLIENTID`.

## Behavior From Source

- Local files are base64-encoded before upload.
- Remote URLs are sent directly to Imgur as the `image` field.
- Deletes call Imgur using the `deletehash`, not the public URL.
- Missing files fail fast with `Error: File "<path>" does not exist.`

Read [repo-summary.md](./references/repo-summary.md) only when you need implementation details or want to debug behavior against the upstream repository.

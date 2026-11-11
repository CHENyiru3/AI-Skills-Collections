---
name: yiru-google-drive
description: Transfer local files or folder trees to or from Google Drive using an already configured gws CLI, including native-document export and retry accounting. Use for requested transfers; not account provisioning, sharing changes, or deletion synchronization.
metadata:
  version: "1.0.0"
---

# Configured Google Drive Transfers

The historical skill ID is retained; account, OAuth project, credentials, and
storage locations belong in the operator's private configuration, not this skill.
Reuse configured access. Use [gws-shared](../gws-shared/SKILL.md) for CLI mechanics
and [gws-drive](../gws-drive/SKILL.md) for API operations. Diagnose authentication
only when it fails; a transfer does not authorize changing credentials or sharing.

## Files and destinations

Use supplied Drive IDs/resource keys and the requested local destination.
Resolve ambiguous destinations before writing. Inspect an unfamiliar method's
schema and the installed CLI version before relying on its flags.

```bash
gws drive +upload ./report.pdf --parent FOLDER_ID
gws drive files get --params '{"fileId":"FILE_ID","alt":"media"}' -o ./report.pdf
gws drive files export --params '{"fileId":"DOC_ID","mimeType":"application/pdf"}' -o ./document.pdf
```

Choose native-document export formats for the user's purpose. Do not treat a
folder, shortcut, or Google-native document as an ordinary binary download.
Where path validation requires it, use the actual source/destination directory
as the working directory and paths beneath it; do not weaken path checks.

New uploads create items and may duplicate them on retry. Inspect an uncertain
remote result before repeating it. Updating an existing item requires its ID
and the requested overwrite scope.

## Folder trees

Check whether the installed CLI provides the requested recursion. Otherwise
use a task-scoped traversal with subprocess argument lists and JSON serialization.

- **Upload:** enumerate the requested tree, create folders including empty ones,
  and retain relative-path-to-Drive-ID mappings plus completed file IDs. Do not
  follow symlinks outside the requested tree implicitly.
- **Download:** list each folder with `'<ID>' in parents and trashed = false`;
  request `nextPageToken` and follow it until absent. Recreate folders, download
  binaries, export native documents, and resolve shortcuts deliberately without
  cycles. Report unsupported or skipped entries.
- Treat remote names as untrusted path components: reject absolute/traversal
  paths, resolve duplicate names with stable ID suffixes, and preserve existing
  local files unless replacement is requested.
- Check method-specific shared-drive options and local capacity. For a configured
  external storage mount, verify the intended mount is present and writable
  before creating destination directories.

Check successful exit statuses and returned IDs; compare binary sizes and
available checksums where useful. Report counts, destinations, failures, skipped
items, and whether traversal completed. Do not infer resumability or deletion
synchronization from a small successful transfer.

---
name: gws-drive
description: List, retrieve, create, update, or manage Google Drive files, folders, and shared-drive resources through the gws CLI. Use for a requested Drive API operation; use gws-drive-upload for a simple new-file upload.
metadata:
  version: "0.22.6"
  source-cli-version: "0.22.5"
---

# Google Drive with gws

Read [gws-shared](../gws-shared/SKILL.md) when authentication, CLI syntax,
pagination, or output handling needs attention. Reuse existing access and the
user's authorized operation; do not regenerate or install skills automatically.

## Select the operation

Use Drive IDs from supplied URLs or resolved listings. Preserve resource keys
when required; resolve ambiguous names or destinations before dependent writes.
Inspect the relevant method rather than relying on a copied API catalog:

```bash
gws drive --help
gws schema drive.files.list
gws drive files list --params '{"q":"trashed = false","fields":"nextPageToken,files(id,name,mimeType)"}'
```

- List/search with `files list`; follow every `nextPageToken` needed for the
  requested scope. Include explicit fields and `trashed = false` when appropriate.
- Inspect metadata or retrieve binary content with `files get`; `alt=media`
  applies to binary files. Export native Docs/Sheets/Slides to a supported format.
- Create folders/files with `files create`; upload a new binary file with
  [gws-drive-upload](../gws-drive-upload/SKILL.md).
- Update an existing item by its ID with `files update`; a repeated create call
  can produce duplicates. Inspect the destination after an uncertain write
  before retrying.
- Change permissions or remove content only within that explicitly authorized
  scope. A transfer request does not imply either operation.

For shared drives, inspect `supportsAllDrives`, `includeItemsFromAllDrives`,
`corpora`, and `driveId` for the selected method. For complete folder-tree
transfers, use [the configured transfer workflow](../yiru-google-drive/SKILL.md).

Check exit status, returned IDs, destination, and listing completeness. Report
failures without claiming that dry-run success or a partial page proves the
remote operation completed. Consult the [Drive API guides](https://developers.google.com/workspace/drive/api/guides/about-sdk)
for version-sensitive behavior outside these common operations.

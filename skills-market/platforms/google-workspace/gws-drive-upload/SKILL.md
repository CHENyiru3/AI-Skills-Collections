---
name: gws-drive-upload
description: Upload a local file as a new Google Drive item with gws drive +upload, optionally choosing its parent and name. Use for an authorized new-file upload; not replacement of an existing item or recursive synchronization.
metadata:
  version: "0.22.6"
  source-cli-version: "0.22.5"
---

# New-file Upload

Use [gws-shared](../gws-shared/SKILL.md) for shared CLI mechanics and
[gws-drive](../gws-drive/SKILL.md) to resolve an uncertain destination.
The user's upload request supplies authorization for that transfer.

```bash
gws drive +upload ./report.pdf --parent FOLDER_ID
gws drive +upload ./data.csv --parent FOLDER_ID --name 'Results.csv'
```

`--parent` and `--name` are optional; MIME type and default name come from the
local file. Inspect current help when behavior matters. Run from the actual
source directory with a file path beneath it if CLI path validation rejects a
path escaping the working directory.

This creates a new item. Do not retry an uncertain result blindly or use it to
overwrite an existing file. For requested replacement, use `files update` with
the verified file ID and inspect its upload schema. Check exit status, returned
ID, and parent/name metadata; report the actual destination and any failure.

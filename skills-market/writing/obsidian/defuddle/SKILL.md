---
name: defuddle
domain: writing
description: Extract a clutter-reduced Markdown representation of a standard HTML page using Defuddle when that extraction is requested or useful. Not a universal replacement for connected/browser access, authenticated pages or raw Markdown URLs.
metadata:
  version: "1.0.1"
---

# Defuddle Extraction

Use an available Defuddle CLI when the task benefits from removing article-page
navigation and clutter. Check `defuddle --help`/`defuddle parse --help` for the
installed version. Do not install it globally simply because a URL was provided.
Prefer existing connected/browser access for authenticated or dynamically rendered
content and read raw Markdown directly when appropriate.

A typical extraction is:

```bash
defuddle parse https://example.com/article --md -o content.md
```

Choose the actual URL/output destination and inspect extraction quality. Confirm
that relevant tables, captions, references and code survived, and preserve source
URL/title/date provenance needed by the task. Empty or partial extraction is not
evidence that the original page lacks the content. Fall back to the source/browser
when needed rather than treating cleaned output as authoritative completeness.

Save only when the user requested an artifact or the task convention requires it.
Stop when the requested content is available in a usable form; no new reader stack
or global npm configuration is implied.

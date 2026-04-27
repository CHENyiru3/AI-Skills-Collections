---
name: cursor-usage-checker
domain: ai-ml
description: Check Cursor usage, billing, and quota through the shared provider usage checker. Reuse local browser session cookies and call Cursor's authenticated usage APIs before considering any browser automation.
category: ai-ml-skills/llm
---

# Cursor Usage Checker

This skill delegates to the shared provider usage checker.

## Default source order

1. Cached cookie header
2. Imported Firefox session cookies
3. Manual cookie header
4. Cursor web APIs

## Usage

```bash
python3 check_usage.py
python3 ../../utility/provider-usage-checker/scripts/check_usage.py --provider cursor --json
```

## What it extracts

- Billing cycle dates
- Included plan utilization
- On-demand spend and limit data
- Identity from `auth/me`
- Legacy request usage when Cursor still exposes it

## Privacy Note

The checker copies Firefox `cookies.sqlite` to a temporary location before reading and does not print raw cookie values.

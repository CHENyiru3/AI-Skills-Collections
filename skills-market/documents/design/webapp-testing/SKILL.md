---
name: webapp-testing
domain: documents
description: Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs.
license: Complete terms in LICENSE.txt
metadata:
  version: "1.0.1"
---

# Local Web Application Testing

Use the application's existing browser/test stack when available. Playwright is
one option; Python, headless Chromium and a new automation script are not universal
requirements. Inspect source/helper code when it matters to selection or repair.

Establish the target URL, running server and requested behavior. Reuse an existing
server without stopping it. For task-owned servers, `scripts/with_server.py --help`
explains its lifecycle wrapper; inspect it before use when side effects matter:

```bash
python scripts/with_server.py --server "npm run dev" --port 5173 -- python your_automation.py
```

The helper checks port availability and starts/stops its own process groups on
POSIX systems. A listening port is only a server readiness hint, not application
readiness. It must not kill a server that was already running.

Navigate and wait for the state needed by the assertion: a visible/enabled control,
loaded data, a relevant response or route change. Prefer semantic roles/labels and
observable state over guessed selectors, arbitrary sleeps or universal networkidle;
background polling can prevent network quiescence indefinitely.

Exercise the requested success/failure path with controlled test data and avoid
submitting real external transactions for a local UI check. Capture useful DOM,
screenshots and console errors when they help diagnose or establish the result.
Close task-owned pages/processes without disrupting the user's sessions.

The `examples/` files are optional starting points; adapt their browser/readiness
choices to the actual app. Stop when the requested behavior has relevant evidence;
report unavailable checks and actual failures without expanding into a full suite.

Reference: [Playwright Page API](https://playwright.dev/docs/api/class-page).

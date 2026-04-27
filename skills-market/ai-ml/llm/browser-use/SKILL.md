---
name: browser-use
domain: ai-ml
description: AI agent that autonomously interacts with the web via Chromium/CDP. Makes websites accessible for LLMs.
version: 1.1.0
category: automation
---

# browser-use Skill

AI agent that autonomously interacts with the web via Chromium/CDP. Makes websites accessible for LLMs.

## ⚠️ CRITICAL: Google API Key Required

browser-use's Agent runs an AI agent that makes decisions about web interactions. **It requires a Google API key** — without it, you get `Missing required environment variable: GOOGLE_API_KEY` or the agent fails to initialize.

If no Google API key is available, use the built-in Hermes browser tools instead (`browser_navigate`, `browser_click`, `browser_type`, `browser_snapshot`). These are separate from browser-use and work out of the box.

## browser-use vs Built-in Browser Tools

| Feature | browser-use Agent | Built-in Hermes browser tools |
|---------|------------------|------------------------------|
| AI-driven | ✅ Yes (autonomous agent) | ❌ No (scripted, deterministic) |
| API key needed | ✅ Google API key required | ❌ None |
| Browser engine | Chromium (CDP protocol) | **WebKit** |
| Firefox support | ❌ Chromium only | ✅ WebKit (cross-platform) |
| Cloudflare behavior | Blocked by Cloudflare (Chromium fingerprint) | Sometimes allowed (different fingerprint) |
| Best for | Complex multi-step tasks needing AI reasoning | Simple navigation, form fills, scraping |
| Headless/silent | ⚠️ Requires Google key + cloud for best stealth | ✅ Fully headless by default |

## Installation

```bash
cd /Users/eric_yiru/Desktop/Github/browser-use
uv venv --python 3.11
source .venv/bin/activate
uv pip install -e .
uv pip install playwright
python -m playwright install chromium
```

## macOS arm64 Chromium Fix (IMPORTANT — playwright installs to wrong path on Apple Silicon)

Playwright on macOS arm64 installs Chromium to `chrome-mac-arm64/` but browser-use looks for `chrome-mac/`. Fix with symlinks:

```bash
ls ~/Library/Caches/ms-playwright/
PLAYWRIGHT_CHROMIUM=~/Library/Caches/ms-playwright/chromium-1217  # or whichever version exists

ln -sfn chrome-mac-arm64 "$PLAYWRIGHT_CHROMIUM/chrome-mac"
ln -sfn "Google Chrome for Testing.app" "$PLAYWRIGHT_CHROMIUM/chrome-mac/Chromium.app"

# Verify
ls "$PLAYWRIGHT_CHROMIUM/chrome-mac/"
# Should show: Chromium.app -> Google Chrome for Testing.app, etc.
```

Without this fix: `RuntimeError: Error getting browser path: No local browser path found after: uvx playwright install chromium`

## Environment Setup

```bash
# Required — browser-use Agent needs a Google API key (or one of the alternatives)
GOOGLE_API_KEY=your_google_api_key
# Or: BROWSER_USE_API_KEY, ANTHROPIC_API_KEY, OPENAI_API_KEY
```

## Basic Usage Pattern

```python
from browser_use import Agent, Browser, ChatBrowserUse
import asyncio
from dotenv import load_dotenv

load_dotenv()

async def main():
    browser = Browser()  # or Browser(use_cloud=True) for stealth cloud browser
    agent = Agent(
        task="Find the number of stars of the browser-use repo",
        llm=ChatBrowserUse(),
        browser=browser,
    )
    await agent.run()

asyncio.run(main())
```

## Key Imports (from `browser_use/__init__.py`)

- `Agent`, `Browser`, `BrowserSession`, `BrowserProfile`
- `ChatBrowserUse`, `ChatGoogle`, `ChatAnthropic`, `ChatOpenAI`, `ChatGroq`, `ChatLiteLLM`, `ChatMistral`, `ChatOllama`, `ChatAzureOpenAI`, `ChatVercel`
- `Tools`, `Controller`
- `DomService`, `SystemPrompt`
- `ActionModel`, `ActionResult`, `AgentHistoryList`

## Cloud/Sandbox Production Pattern

```python
from browser_use import Browser, sandbox, ChatBrowserUse
from browser_use.agent.service import Agent

@sandbox(cloud_profile_id='your-profile-id')
async def production_task(browser: Browser):
    agent = Agent(task="Your authenticated task", browser=browser, llm=ChatBrowserUse())
    await agent.run()
```

## Key Files

- Main package: `/Users/eric_yiru/Desktop/Github/browser-use/browser_use/`
- Agent service: `browser_use/agent/service.py`
- Agent views/models: `browser_use/agent/views.py`
- LLM adapters: `browser_use/llm/` (browser_use/, anthropic/, google/, openai/, etc.)
- Examples: `examples/models/` directory

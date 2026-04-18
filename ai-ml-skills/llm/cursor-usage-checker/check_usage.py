#!/usr/bin/env python3
"""
Cursor Usage Checker
Uses Firefox cookies + Playwright WebKit to bypass Cloudflare on cursor.com/billing
"""
import asyncio
import sqlite3
import os
import shutil
from playwright.async_api import async_playwright

FIREFOX_PROFILE = '/Users/eric_yiru/Library/Application Support/Firefox/Profiles/ftyiboxw.default-release'
UV_PYTHON = '/Users/eric_yiru/.local/share/uv/python/cpython-3.11.14-macos-aarch64-none/bin/python3.11'

def get_firefox_cursor_cookies():
    """Extract Cursor session cookies from Firefox profile (works even with Firefox running)."""
    src_db = os.path.join(FIREFOX_PROFILE, 'cookies.sqlite')
    tmp_db = '/tmp/firefox_cookies_copy.sqlite'

    shutil.copy2(src_db, tmp_db)
    wal_path = src_db + '-wal'
    if os.path.exists(wal_path):
        shutil.copy2(wal_path, tmp_db + '-wal')

    conn = sqlite3.connect(tmp_db)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT host, name, value, path, isSecure, isHttpOnly
        FROM moz_cookies
        WHERE host IN ('cursor.com', '.cursor.com', 'authenticator.cursor.sh', '.authenticator.cursor.sh')
    """)
    raw_cookies = cursor.fetchall()
    conn.close()

    return [{
        'name': name,
        'value': value,
        'domain': host,
        'path': path,
        'secure': bool(isSecure),
        'httpOnly': bool(isHttpOnly)
    } for host, name, value, path, isSecure, isHttpOnly in raw_cookies]

async def main():
    cookies = get_firefox_cursor_cookies()
    print(f"Loaded {len(cookies)} cursor cookies from Firefox")

    async with async_playwright() as p:
        print("Launching WebKit...")
        browser = await p.webkit.launch(headless=True)
        context = await browser.new_context()
        await context.add_cookies(cookies)
        page = await context.new_page()

        print("Navigating to cursor.com/dashboard/billing...")
        await page.goto("https://cursor.com/dashboard/billing")
        await asyncio.sleep(12)

        print(f"URL: {page.url}")
        print(f"Title: {await page.title()}")

        content = await page.evaluate("document.body.innerText")
        print(f"\n=== BILLING PAGE CONTENT ===\n{content[:8000]}")

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())

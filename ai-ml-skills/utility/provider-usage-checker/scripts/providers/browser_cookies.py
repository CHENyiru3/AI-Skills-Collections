from __future__ import annotations

import os
import shutil
import sqlite3
import tempfile
from dataclasses import dataclass
from pathlib import Path


class BrowserCookieError(RuntimeError):
    pass


@dataclass
class ImportedCookieHeader:
    cookie_header: str
    source: str


def _copy_sqlite_with_wal(src_db: Path) -> Path:
    if not src_db.exists():
        raise BrowserCookieError(f"Cookie database not found: {src_db}")
    temp_dir = Path(tempfile.mkdtemp(prefix="provider-usage-checker-"))
    dst_db = temp_dir / src_db.name
    shutil.copy2(src_db, dst_db)
    wal_path = src_db.with_name(src_db.name + "-wal")
    if wal_path.exists():
        shutil.copy2(wal_path, temp_dir / wal_path.name)
    shm_path = src_db.with_name(src_db.name + "-shm")
    if shm_path.exists():
        shutil.copy2(shm_path, temp_dir / shm_path.name)
    return dst_db


def _find_firefox_profiles() -> list[Path]:
    root = Path.home() / "Library" / "Application Support" / "Firefox" / "Profiles"
    if not root.exists():
        return []
    return sorted(path for path in root.iterdir() if path.is_dir() and (path / "cookies.sqlite").exists())


def import_firefox_cookie_header(domains: list[str], cookie_names: set[str] | None = None) -> ImportedCookieHeader:
    profiles = _find_firefox_profiles()
    if not profiles:
        raise BrowserCookieError("No Firefox profiles with cookies.sqlite were found.")

    for profile in profiles:
        copy_path = _copy_sqlite_with_wal(profile / "cookies.sqlite")
        conn = sqlite3.connect(copy_path)
        try:
            cursor = conn.cursor()
            placeholders = ",".join("?" for _ in domains)
            query = f"""
                SELECT host, name, value
                FROM moz_cookies
                WHERE host IN ({placeholders})
            """
            cursor.execute(query, domains)
            rows = cursor.fetchall()
        finally:
            conn.close()

        cookies: list[tuple[str, str]] = []
        for _host, name, value in rows:
            if cookie_names and name not in cookie_names:
                continue
            cookies.append((name, value))
        if not cookies and cookie_names:
            for _host, name, value in rows:
                cookies.append((name, value))
        if cookies:
            deduped: dict[str, str] = {}
            for name, value in cookies:
                deduped[name] = value
            header = "; ".join(f"{name}={value}" for name, value in sorted(deduped.items()))
            return ImportedCookieHeader(cookie_header=header, source=f"firefox:{profile.name}")
    raise BrowserCookieError("No matching Firefox cookies were found.")


def import_cookie_header(
    browser: str,
    domains: list[str],
    cookie_names: set[str] | None = None,
) -> ImportedCookieHeader:
    if browser not in {"auto", "firefox"}:
        raise BrowserCookieError(f"Browser import is not implemented for {browser}. Use Firefox or a manual cookie header.")
    return import_firefox_cookie_header(domains=domains, cookie_names=cookie_names)

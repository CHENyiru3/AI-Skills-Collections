"""Zotero Web API write client (read is handled by ZoteroClient via SQLite)."""
from __future__ import annotations
from pyzotero import zotero


class ZoteroWriter:
    """
    Write access to Zotero library via official Web API v3 (Pyzotero).

    Reads are NOT done here — use ZoteroClient for reads.
    This class only handles mutations: tags, collections, etc.
    """

    def __init__(self, api_key: str, user_id: str, library_type: str = "user"):
        self._zot = zotero.Zotero(user_id, library_type, api_key)

    # =========================================================
    # Tag operations
    # =========================================================

    def set_item_tags(self, item_key: str, tags: list[str]) -> dict:
        """Replace all tags on an item with the given list."""
        item = self._zot.item(item_key)
        item["data"]["tags"] = [{"tag": t} for t in tags]
        return self._zot.update_item(item)

    def add_item_tags(self, item_key: str, tags: list[str]) -> dict:
        """Add tags to an item without removing existing ones."""
        item = self._zot.item(item_key)
        existing = {t["tag"] for t in item["data"].get("tags", [])}
        new_tags = existing | set(tags)
        item["data"]["tags"] = [{"tag": t} for t in sorted(new_tags)]
        return self._zot.update_item(item)

    def remove_item_tags(self, item_key: str, tags: list[str]) -> dict:
        """Remove specific tags from an item."""
        item = self._zot.item(item_key)
        remove_set = set(tags)
        item["data"]["tags"] = [
            t for t in item["data"].get("tags", [])
            if t["tag"] not in remove_set
        ]
        return self._zot.update_item(item)

    # =========================================================
    # Collection operations
    # =========================================================

    def add_to_collection(self, item_key: str, collection_key: str) -> bool:
        """Add an item to a collection (non-destructive, keeps existing collections)."""
        item = self._zot.item(item_key)
        existing = set(item["data"].get("collections", []))
        existing.add(collection_key)
        item["data"]["collections"] = list(existing)
        self._zot.update_item(item)
        return True

    def remove_from_collection(self, item_key: str, collection_key: str) -> bool:
        """Remove an item from a collection."""
        item = self._zot.item(item_key)
        existing = set(item["data"].get("collections", []))
        existing.discard(collection_key)
        item["data"]["collections"] = list(existing)
        self._zot.update_item(item)
        return True

    def create_collection(self, name: str, parent_key: str | None = None) -> dict:
        """Create a new collection. Returns the created collection's data."""
        payload = [{"name": name, "parentCollection": parent_key or False}]
        result = self._zot.create_collections(payload)
        # Pyzotero returns {"success": {"0": key}, "unchanged": {}, "failed": {}}
        if result.get("success"):
            created_key = list(result["success"].values())[0]
            return {"key": created_key, "name": name, "parent_key": parent_key}
        raise RuntimeError(f"Failed to create collection: {result}")

    def create_note(self, item_key: str, content: str, title: str | None = None, tags: list[str] | None = None) -> dict:
        """Create a child note on a Zotero item.

        Args:
            item_key: Parent item key
            content: Note content (plain text or HTML)
            title: Optional title (prepended as heading)
            tags: Optional tags for the note

        Returns:
            Dict with key of created note
        """
        import html as html_mod

        # Convert plain text to HTML if it doesn't look like HTML
        if not content.strip().startswith("<"):
            # Plain text → HTML: paragraphs and line breaks
            paragraphs = content.split("\n\n")
            html_parts = []
            for p in paragraphs:
                escaped = html_mod.escape(p).replace("\n", "<br/>")
                html_parts.append(f"<p>{escaped}</p>")
            html_content = "".join(html_parts)
        else:
            html_content = content

        # Prepend title as heading
        if title:
            html_content = f"<h1>{html_mod.escape(title)}</h1>{html_content}"

        # Build note template
        template = self._zot.item_template("note")
        template["parentItem"] = item_key
        template["note"] = html_content
        template["tags"] = [{"tag": t} for t in (tags or [])]

        result = self._zot.create_items([template])
        if result.get("success"):
            created_key = list(result["success"].values())[0]
            return {"key": created_key, "parent_key": item_key}
        raise RuntimeError(f"Failed to create note: {result}")

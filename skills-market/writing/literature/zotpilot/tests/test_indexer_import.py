"""Smoke test: indexer module imports cleanly."""

def test_indexer_imports():
    """Verify zotpilot.indexer can be imported without errors."""
    from zotpilot import indexer
    assert hasattr(indexer, "Indexer") or hasattr(indexer, "IndexResult")

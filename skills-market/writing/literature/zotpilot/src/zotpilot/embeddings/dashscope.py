"""Alibaba Cloud Bailian (DashScope) embedding provider."""
import logging
import time

import httpx

logger = logging.getLogger(__name__)

# China mainland endpoint (default)
DEFAULT_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
# International endpoint (Singapore)
INTL_BASE_URL = "https://dashscope-intl.aliyuncs.com/compatible-mode/v1"


class DashScopeEmbedder:
    """
    Alibaba Cloud Bailian embedding wrapper using OpenAI-compatible API.

    Supports text-embedding-v3 and text-embedding-v4 (Qwen3-Embedding).
    Uses asymmetric embeddings via DashScope native text_type parameter.

    Default model: text-embedding-v4
    Output dimensions: configurable (v3: 64–1024, v4: 64–2048)
    Max input: 8192 tokens per text
    Batch size: up to 10 texts (v3/v4)
    Pricing: ¥0.0005 / 1k tokens (~$0.07 / million tokens)
    """

    def __init__(
        self,
        model: str = "text-embedding-v4",
        dimensions: int = 1024,
        api_key: str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = 120.0,
        max_retries: int = 3,
    ):
        import os
        self.api_key = api_key or os.environ.get("DASHSCOPE_API_KEY")
        if not self.api_key:
            raise ValueError(
                "DASHSCOPE_API_KEY not set. Get one at https://bailian.console.aliyun.com/"
            )
        self.model = model
        self.dimensions = dimensions
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries

    def _embed_batch(
        self, batch: list[str], batch_num: int, total_batches: int
    ) -> list[list[float]]:
        """Embed a single batch with retry."""
        total_chars = sum(len(t) for t in batch)
        logger.debug(
            f"Embedding batch {batch_num}/{total_batches}: "
            f"{len(batch)} texts, {total_chars} chars total"
        )

        url = f"{self.base_url}/embeddings"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": self.model,
            "input": batch,
            "dimensions": self.dimensions,
            "encoding_format": "float",
        }

        for attempt in range(1, self.max_retries + 1):
            try:
                with httpx.Client(timeout=self.timeout) as client:
                    response = client.post(url, headers=headers, json=payload)
                    response.raise_for_status()
                    data = response.json()

                embeddings = sorted(data["data"], key=lambda x: x["index"])
                result = [e["embedding"] for e in embeddings]
                logger.debug(
                    f"Batch {batch_num}/{total_batches} succeeded "
                    f"(attempt {attempt}), got {len(result)} embeddings"
                )
                return result

            except httpx.TimeoutException:
                logger.warning(
                    f"Batch {batch_num}/{total_batches} timed out after "
                    f"{self.timeout}s (attempt {attempt}/{self.max_retries})"
                )
            except httpx.HTTPStatusError as e:
                logger.warning(
                    f"Batch {batch_num}/{total_batches} HTTP {e.response.status_code} "
                    f"(attempt {attempt}/{self.max_retries}): {e.response.text[:200]}"
                )
            except Exception as e:
                logger.warning(
                    f"Batch {batch_num}/{total_batches} failed "
                    f"(attempt {attempt}/{self.max_retries}): {type(e).__name__}: {e}"
                )

            if attempt < self.max_retries:
                backoff = 2 ** attempt
                logger.info(f"Retrying in {backoff}s...")
                time.sleep(backoff)

        from .gemini import EmbeddingError
        raise EmbeddingError(
            f"Batch {batch_num}/{total_batches} failed after "
            f"{self.max_retries} attempts ({len(batch)} texts, {total_chars} chars)"
        )

    def embed(
        self,
        texts: list[str],
        task_type: str = "RETRIEVAL_DOCUMENT",
    ) -> list[list[float]]:
        """
        Embed a batch of texts.

        Args:
            texts: List of texts to embed
            task_type: Ignored (DashScope OpenAI-compatible endpoint
                       uses symmetric embeddings)

        Returns:
            List of embedding vectors
        """
        if not texts:
            return []

        results = []
        batch_size = 10  # DashScope v3/v4 limit
        total_batches = (len(texts) + batch_size - 1) // batch_size

        logger.debug(
            f"Embedding {len(texts)} texts in {total_batches} batch(es), "
            f"model={self.model}"
        )

        for i in range(0, len(texts), batch_size):
            batch = texts[i:i + batch_size]
            batch_num = i // batch_size + 1
            batch_results = self._embed_batch(batch, batch_num, total_batches)
            results.extend(batch_results)
            if batch_num < total_batches:
                time.sleep(0.5)

        return results

    def embed_query(self, query: str) -> list[float]:
        """Embed a search query."""
        return self.embed([query], task_type="RETRIEVAL_QUERY")[0]

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        """Embed documents for indexing."""
        return self.embed(texts, task_type="RETRIEVAL_DOCUMENT")

Smart Defaults: Agno provides sensible defaults to get you started quickly:
Embedder: If no embedder is specified, Agno automatically uses OpenAIEmbedder with default settings
Chunking: If no chunking strategy is provided to readers, Agno defaults to FixedSizeChunking(chunk_size=5000)
Search Type: Vector databases default to SearchType.vector for semantic search
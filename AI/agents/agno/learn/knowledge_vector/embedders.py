from agno.knowledge.embedder.cohere import CohereEmbedder
import asyncio
# Add embedding to database
embedder = CohereEmbedder(id="embed-v4.0", dimensions=1536)

embeddings = embedder.get_embedding("The quick brown fox jumps over the lazy dog.")
# Print the embeddings and their dimensions
print(f"Embeddings: {embeddings[:5]}")
print(f"Dimensions: {len(embeddings)}")


embed_list = [
    "Large language models are trained using autoregressive objectives.",
    "World models learn latent state transitions and reward dynamics.",
    "SLR(1) parsing uses FOLLOW sets to resolve shift-reduce conflicts.",
    "Embeddings map discrete tokens into continuous vector spaces.",
    "Model-based reinforcement learning explicitly learns environment dynamics.",
    "Decoder-only transformers rely on masked self-attention.",
    "A Markov decision process satisfies the Markov property.",
    "Vector databases enable efficient similarity search.",
    "PDF documents can be chunked before embedding.",
    "Sampling drift can be mitigated with scheduled sampling."
]


embeddings, usage = asyncio.run(embedder.async_get_embeddings_batch_and_usage(embed_list))

print(f"Num embeddings: {len(embeddings)}")
print(f"Embedding dimension: {len(embeddings[0])}")
print(f"First embedding (first 5 dims): {embeddings[0][:5]}")
print(f"Usage: {usage}")
import asyncio

from agno.agent import Agent
from agno.db.sqlite.sqlite import SqliteDb
from agno.knowledge.embedder.google import GeminiEmbedder
from agno.knowledge.knowledge import Knowledge
from agno.vectordb.chroma.chromadb import ChromaDb
from agno.models.cerebras import Cerebras
db = SqliteDb(
    db_file="temp/contents.db",
    knowledge_table="knowledge_contents",
)

# Create Knowledge Instance
knowledge = Knowledge(
    name="Basic SDK Knowledge Base",
    description="Agno 2.0 Knowledge Implementation",
    contents_db=db,
    vector_db=ChromaDb(
        # table_name="vectors",
        # db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
        # embedder=OpenAIEmbedder(),
        collection="vectors",
        path="tmp/chromadb_rag",
        persistent_client=True,
        embedder=GeminiEmbedder(id="gemini-embedding-001")
    ),
)
# Add from URL to the knowledge base
asyncio.run(
    knowledge.add_content_async(
        name="Recipes",
        url="https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf",
        metadata={"user_tag": "Recipes from website"},
    )
)

agent = Agent(
    # model=Cerebras(id="gpt-oss-120b"),
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    # model=Cerebras(id="zai-glm-4.6"),
    name="My Agent",
    description="Agno 2.0 Agent Implementation",
    knowledge=knowledge,
    search_knowledge=True,
    
)

agent.print_response(
    "How do I make chicken and galangal in coconut milk soup?",
    # metadata={"user_tag": "Recipes from website"},
    markdown=True,
)
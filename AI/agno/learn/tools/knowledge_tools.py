from agno.agent import Agent
from agno.models.google import Gemini
from agno.knowledge.embedder.google import GeminiEmbedder
from agno.knowledge.knowledge import Knowledge

from agno.tools.knowledge import KnowledgeTools
from agno.vectordb.lancedb import LanceDb, SearchType

# integrates with Knowledge
# add_knowledge_to_context + search_knowledge is essentailly KnowledgeTools but just with search
#Knowledge Tools comes with default sys prompt + few shot

#Ex:

# Create a knowledge base containing information from a URL
agno_docs = Knowledge(
    # Use LanceDB as the vector database and store embeddings in the `agno_docs` table
    vector_db=LanceDb(
        uri="tmp/lancedb",
        table_name="agno_docs",
        search_type=SearchType.hybrid,
        embedder=GeminiEmbedder(id="gemini-embedding-001")
        # embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    ),
)
agno_docs.add_content(
    url="https://docs.agno.com/llms-full.txt"
)

knowledge_tools = KnowledgeTools(
    knowledge=agno_docs,
    think=True,# session_state["thoughts"]
    search=True, # knowledge search, same as search_knowledge = True
    analyze=True, # session_state["analysis"]
    add_few_shot=True,
)

agent = Agent(
    model=Gemini(id="gemini-2.5-flash"),
    tools=[knowledge_tools],
    markdown=True,
)

if __name__ == "__main__":
    agent.print_response("How do I build multi-agent teams with Agno?", stream=True)
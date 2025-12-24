from agno.agent import Agent
from agno.knowledge.knowledge import Knowledge


### MANUAL FILTERS
agent = Agent(
    name="KnowledgeFilterAgent",
    search_knowledge=False,  # Do not use agentic search
    add_knowledge_to_context=True,     # Add knowledge base references to the system prompt
    knowledge_filters={"user_id": "jordan_mitchell"}, # Pass filters like this
)

# Attach Metadata
knowledge_base = Knowledge(
    vector_db=vector_db,
)
knowledge_base.add_contents(
    [
        {
            "path": "path/to/cv1.pdf",
            "metadata": {
                "user_id": "jordan_mitchell",
                "document_type": "cv",
                "year": 2025,
            },
        },
        # ... more documents ...
    ]
)

knowledge_base = Knowledge(
    vector_db=vector_db,
    max_results=5,
)

# Load first document with user_1 metadata
knowledge_base.add_content(
    path=path/to/cv1.pdf,
    metadata={"user_id": "jordan_mitchell", "document_type": "cv", "year": 2025},
)

# Load second document with user_2 metadata
knowledge_base.add_content(
    path=path/to/cv2.pdf,
    metadata={"user_id": "taylor_brooks", "document_type": "cv", "year": 2025},
)

# Query with filters
agent = Agent(
    knowledge=knowledge_base,
    search_knowledge=True,
    # knowledge_filters={"user_id": "jordan_mitchell"},
    knowledge_filters={
        "user_id": "jordan_mitchell",
        "document_type": "cv",
        "year": 2025,
    }
)
agent.print_response(
    "Tell me about Jordan Mitchell's experience and skills",
    markdown=True,
)

# response specific queries
agent.print_response(
    "Tell me about Jordan Mitchell's experience and skills",
    knowledge_filters={"user_id": "jordan_mitchell"},
    markdown=True,
)


### AGENTIC FILTERS

# 1. Attach Metadata first

# ...


agent = Agent(
    knowledge=knowledge_base,
    search_knowledge=True,
    enable_agentic_knowledge_filters=True,
)
agent.print_response(
    "Tell me about Jordan Mitchell's experience and skills with jordan_mitchell as user id and document type cv",
    markdown=True,
)

# In this example, the Agent will automatically use:
user_id = "jordan_mitchell"
document_type = "cv"




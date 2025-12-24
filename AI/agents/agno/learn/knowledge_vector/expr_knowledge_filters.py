from agno.filters import EQ

# Find only HR policy documents
EQ("department", "hr")

# Find content from a specific year
EQ("year", 2024)

from agno.filters import IN

# Find content from multiple regions
IN("region", ["north_america", "europe", "asia"])

# Find multiple document types
IN("document_type", ["policy", "guideline", "procedure"])

from agno.filters import GT, LT

# Find recent documents
GT("year", 2020)

# Find documents with high priority scores
GT("priority_score", 8.0)

# Find documents within a date range
LT("year", 2025)

from agno.filters import AND

# Find sales documents from North America in 2024
AND(
    EQ("data_type", "sales"),
    EQ("region", "north_america"),
    EQ("year", 2024)
)

from agno.filters import OR


# Find either engineering or product documents
OR(
    EQ("department", "engineering"),
    EQ("department", "product")
)

from agno.filters import NOT

# Find everything except draft documents
NOT(EQ("status", "draft"))

# NEED CONTENTS DATABASE FOR AGENTIC FILTERING

from agno.agent import Agent
from agno.filters import EQ, IN, AND
from agno.knowledge.knowledge import Knowledge
from agno.vectordb.pgvector import PgVector
from agno.db.postgres import PostgresDb

# Setup knowledge with metadata
knowledge = Knowledge(
    contents_db=PostgresDb(
        db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
        knowledge_table="knowledge_contents",
    ),
    vector_db=PgVector(
        table_name="filtered_knowledge",
        db_url="postgresql+psycopg://ai:ai@localhost:5532/ai"
    )
)

# Add content with rich metadata
knowledge.add_content(
    path="sales_report_q1.csv",
    metadata={
        "data_type": "sales",
        "quarter": "Q1",
        "year": 2024,
        "region": "north_america",
        "currency": "USD"
    }
)

# Create agent with knowledge
agent = Agent(
    knowledge=knowledge,
    search_knowledge=True,
    instructions="Always search knowledge before answering questions"
)

# Use filters in agent responses - NOTE: filters must be in a list!
agent.print_response(
    "What were our Q1 sales results?",
    knowledge_filters=[  # ← Must be a list!
        AND(EQ("data_type", "sales"), EQ("quarter", "Q1"))
    ]
)

# Find recent sales data from specific regions, but exclude drafts
complex_filter = AND(
    EQ("data_type", "sales"),
    IN("region", ["north_america", "europe"]),
    GT("year", 2022),
    NOT(EQ("status", "draft"))
)

# Search for either customer feedback or survey data from the last two years
feedback_filter = AND(
    OR(
        EQ("data_type", "feedback"),
        EQ("data_type", "survey")
    ),
    GT("year", 2022)
)


agent.print_response(
    "What do our customers think about our new features?",
    knowledge_filters=[feedback_filter]  # ← List wrapper required
)


def get_user_filter(user_id: str, user_department: str):
    """Create filters based on user context."""
    return OR(
        EQ("visibility", "public"),
        EQ("owner", user_id),
        EQ("department", user_department)
    )

# Apply user-specific filtering
user_filter = get_user_filter("john_doe", "engineering")
agent.print_response(
    "Show me the latest project updates",
    knowledge_filters=[user_filter]  # ← List wrapper required
)


#TIME BASED
from datetime import datetime

current_year = datetime.now().year

# Only search recent content
recent_filter = GT("year", current_year - 2)

# Exclude archived content
active_filter = NOT(EQ("status", "archived"))

# Combine for active, recent content
current_content = AND(recent_filter, active_filter)

# Use in agent - wrap in list
agent.print_response(
    "What's new?",
    knowledge_filters=[current_content]
)


async def progressive_search(agent: Agent, query, base_filters=None):
    """Try broad search first, then narrow if too many results."""

    # First attempt: broad search
    broad_results = await agent.aget_relevant_docs_from_knowledge(
        query=query,
        filters=base_filters,  # Already a list
        num_documents=10
    )

    if len(broad_results) > 8:
        # Too many results, add more specific filters
        specific_filter = AND(
            base_filters[0] if base_filters else EQ("status", "active"),
            GT("relevance_score", 0.8)
        )

        return await agent.aget_relevant_docs_from_knowledge(
            query=query,
            filters=[specific_filter],  # ← Wrapped in list
            num_documents=5
        )

    return broad_results

# Advanced filter expressions (using FilterExpr like EQ(), AND(), etc.) is currently only supported in PGVector.

# Not compatible with agnetic filtering

# Works with agentic filtering (agent decides filters dynamically)
knowledge_filters = [{"department": "hr", "document_type": "policy"}]

# Does not work with agentic filtering (static, predefined logic)
knowledge_filters = [AND(EQ("department", "hr"), EQ("document_type", "policy"))]


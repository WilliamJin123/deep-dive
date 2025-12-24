import asyncio
from agno.agent import Agent
from agno.knowledge.knowledge import Knowledge
from agno.vectordb.pgvector import PgVector

# Create Knowledge Instance
knowledge = Knowledge(
    name="Basic SDK Knowledge Base",
    description="Agno 2.0 Knowledge Implementation",
    vector_db=PgVector(
        table_name="vectors", db_url="postgresql+psycopg://ai:ai@localhost:5532/ai"
    ),
)

# Add from local file to the knowledge base

#INCLUDE OR EXCLUDE FILES USING REGEX
asyncio.run(
    knowledge.add_content_async(
        name="CV",
        path="cookbook/08_knowledge/testing_resources",
        metadata={"user_tag": "Engineering Candidates"},
        # Only include PDF files
        include=["*.pdf"],
        # Don't include files that match this pattern
        exclude=["*cv_5*"],
    )
)

# ADD CONTENT
asyncio.run(
    knowledge.add_content_async(
        name="CV",
        path="cookbook/08_knowledge/testing_resources/cv_1.pdf",
        metadata={"user_tag": "Engineering Candidates"},
    )
)

#REMOVE CONTENT BY ID AND ITERATING THROUGH KNOWLEDGE CONTENT


# Remove content and vectors by id
contents, _ = knowledge.get_content() #second variable is count of knowledge "rows"
for content in contents:
    print(content.id)
    print(" ")
    knowledge.remove_content_by_id(content.id)

# Remove all content
knowledge.remove_all_content()

# Remove vectors
knowledge.remove_vectors_by_metadata({"user_tag": "Engineering Candidates"})
knowledge.remove_vectors_by_name("CV")
knowledge.remove_vector_by_id("random_id")


# Add from local file to the knowledge base, but don't skip if it already exists
asyncio.run(
    knowledge.add_content_async(
        name="CV",
        path="cookbook/08_knowledge/testing_resources/cv_1.pdf",
        metadata={"user_tag": "Engineering Candidates"},
        skip_if_exists=False,
        # True by default
    )
)

#Synchronous add
knowledge.add_content(
    name="CV",
    path="cookbook/08_knowledge/testing_resources/cv_1.pdf",
    metadata={"user_tag": "Engineering Candidates"},
)

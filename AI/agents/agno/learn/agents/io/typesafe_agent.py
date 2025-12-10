from typing import List

from agno.agent import Agent
from agno.models.cohere import Cohere
from agno.models.cerebras import Cerebras
from agno.tools.hackernews import HackerNewsTools
from pydantic import BaseModel, Field
from rich.pretty import pprint


# Define your input schema
class ResearchTopic(BaseModel):
    topic: str
    sources_required: int = Field(description="Number of sources", default=5)


# Define your output schema
class ResearchOutput(BaseModel):
    summary: str = Field(..., description="Executive summary of the research")
    insights: List[str] = Field(..., description="Key insights from posts")
    top_stories: List[str] = Field(
        ..., description="Most relevant and popular stories found"
    )
    technologies: List[str] = Field(
        ..., description="Technologies mentioned"
    )
    sources: List[str] = Field(..., description="Links to the most relevant posts")


# Define your agent
hn_researcher_agent = Agent(
    # Model to use
    # model=Claude(id="claude-sonnet-4-0"),
    model=Cohere("command-a-03-2025"), # id="command-r-plus" default
    # Tools to use
    tools=[HackerNewsTools()],
    instructions="Research hackernews posts for a given topic",
    # Add your input schema
    input_schema=ResearchTopic,
    # Add your output schema
    output_schema=ResearchOutput,
    parser_model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    markdown=True,
)

# Run the Agent
response = hn_researcher_agent.run(
    input=ResearchTopic(topic="AI", sources_required=5)
)

# Print the response
pprint(response.content)

# =============================================================================
# | Feature                        | output_model                                | parser_model                                |
# |-------------------------------|---------------------------------------------|---------------------------------------------|
# | Who generates the initial     | Main model generates natural language or    | Main model tries to generate raw structured |
# | structure?                    | draft response                              | output (e.g. JSON)                            |
# |-------------------------------|---------------------------------------------|---------------------------------------------|
# | When is the secondary model   | Always — at the end to produce the final    | Only if the main model’s output fails       |
# | used?                         | structured response                         | validation (on parse error)                 |
# |-------------------------------|---------------------------------------------|---------------------------------------------|
# | Role of secondary model       | Full generation of structured output        | Repair / fix malformed or invalid output    |
# |-------------------------------|---------------------------------------------|---------------------------------------------|
# | Best use case                 | Main model isn't good at JSON (e.g. image   | Main model outputs JSON but occasionally    |
# |                               | analysis models, some open-source models)   | makes formatting mistakes                   |
# |-------------------------------|---------------------------------------------|---------------------------------------------|
# | Performance                   | One extra LLM call always                   | Extra call only on failure (more efficient) |
# =============================================================================

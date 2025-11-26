from typing import List

from agno.agent import Agent
from agno.models.cerebras import Cerebras

from agno.team.team import Team
from agno.tools.hackernews import HackerNewsTools
from pydantic import BaseModel, Field


class ResearchTopic(BaseModel):
    """Structured research topic with specific requirements."""

    topic: str = Field(description="The main research topic")
    focus_areas: List[str] = Field(description="Specific areas to focus on")
    target_audience: str = Field(description="Who this research is for")
    sources_required: int = Field(description="Number of sources needed", default=5)


# Create specialized Hacker News research agent
hackernews_agent = Agent(
    name="Hackernews Agent",
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),

    tools=[HackerNewsTools()],
    role="Extract key insights and content from Hackernews posts",
    instructions=[
        "Search Hacker News for relevant articles and discussions",
        "Extract key insights and summarize findings",
        "Focus on high-quality, well-discussed posts",
    ],
)

# Create collaborative research team
team = Team(
    name="Hackernews Research Team",
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    
    members=[hackernews_agent],
    determine_input_for_members=False,  # The member gets the input directly, without the team leader synthesizing it
    instructions=[
        "Conduct thorough research based on the structured input",
        "Address all focus areas mentioned in the research topic",
        "Tailor the research to the specified target audience",
        "Provide the requested number of sources",
    ],
    show_members_responses=True,
)

# Use Pydantic model as structured input
research_request = ResearchTopic(
    topic="AI Agent Frameworks",
    focus_areas=["AI Agents", "Framework Design", "Developer Tools", "Open Source"],
    target_audience="Software Developers and AI Engineers",
    sources_required=7,
)
# Execute research with structured input
team.print_response(input=research_request)
from typing import List

from agno.agent import Agent
from agno.models.cerebras import Cerebras
from agno.tools.hackernews import HackerNewsTools
from pydantic import BaseModel, Field


class ResearchTopic(BaseModel):
    """Structured research topic with specific requirements"""

    topic: str
    focus_areas: List[str] = Field(description="Specific areas to focus on")
    target_audience: str = Field(description="Who this research is for")
    sources_required: int = Field(description="Number of sources needed", default=5)

hackernews_agent = Agent(
    name="Hackernews Agent",
    # model=OpenAIChat(id="gpt-5-mini"),
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    tools=[HackerNewsTools()],
    role="Extract key insights and content from Hackernews posts",
)

# hackernews_agent.print_response(
#     input=ResearchTopic(
#         topic="AI",
#         focus_areas=["AI", "Machine Learning"],
#         target_audience="Developers",
#         #default sources_required  = 5
#     )
# )


# a validated dictionary with all the right attributes works as well (since pydantic is a wrapper for JSON schema)
hackernews_agent.print_response(
    input={
        "topic": "Food",
        "focus_areas": ["Bananas", "Baking"],
        "target_audience": "Chefs",
        "sources_required": "5",
    }
)
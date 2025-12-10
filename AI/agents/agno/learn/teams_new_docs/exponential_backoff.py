from agno.agent import Agent
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.models.cerebras import Cerebras


# Create a research team
team = Team(
    members=[
        Agent(
            name="Sarah",
            role="Data Researcher",
            tools=[DuckDuckGoTools()],
            instructions="Focus on gathering and analyzing data",
        ),
        Agent(
            name="Mike",
            role="Technical Writer",
            instructions="Create clear, concise summaries",
        ),
    ],
    retries=3,
    exponential_backoff=True,
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
)

team.print_response(
    "Search for latest news about the latest AI models",
    stream=True,
)
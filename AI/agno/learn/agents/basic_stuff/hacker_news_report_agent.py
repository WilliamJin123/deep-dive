from agno.agent import Agent
from agno.models.cerebras import Cerebras
from agno.tools.hackernews import HackerNewsTools
import os

agent = Agent(
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507", ),
    tools=[HackerNewsTools()],
    markdown=True,
)
agent.print_response("Write a report on trending startups and products.", stream=True)
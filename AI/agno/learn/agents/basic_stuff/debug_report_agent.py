from agno.agent import Agent
from agno.models.cerebras import Cerebras
from agno.tools.hackernews import HackerNewsTools

agent = Agent(
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    tools=[HackerNewsTools()],
    markdown=True,
    instructions="Write a report on the topic. Output only the report.",
    debug_level=1,
    debug_mode=True,
)

agent.print_response("Write a report on trending startups and products.", stream=True)

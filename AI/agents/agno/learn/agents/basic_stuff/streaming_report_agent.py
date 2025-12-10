from typing import Iterator
from agno.agent import Agent, RunOutput, RunOutputEvent, RunEvent
from agno.models.cerebras import Cerebras
from agno.tools.hackernews import HackerNewsTools
from agno.utils.pprint import pprint_run_response

agent = Agent(
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    tools=[HackerNewsTools()],
    instructions="Write a report on the topic. Output only the report.",
    markdown=True,
)

# Run agent and return the response as a variable
response: RunOutput = agent.run("Trending startups and products.")
# Print the response
print(response.content)

################ STREAM RESPONSE #################
stream: Iterator[RunOutputEvent] = agent.run("Trending products", stream=True)
for chunk in stream:
    if chunk.event == RunEvent.run_content:
        print(chunk.content)

# ################ STREAM AND PRETTY PRINT #################
stream: Iterator[RunOutputEvent] = agent.run("Trending products", stream=True)
pprint_run_response(stream, markdown=True)
from typing import Iterator
from agno.team import Team
from agno.agent import Agent
from agno.models.cerebras import Cerebras
from agno.run.team import TeamRunOutputEvent
from agno.utils.pprint import pprint_run_response


# for prod, don't run with print_response, run with Team.run() or Team.arun()

news_agent = Agent(name="News Agent", role="Get the latest news")
weather_agent = Agent(name="Weather Agent", role="Get the weather for the next 7 days")

team = Team(
    name="News and Weather Team", 
    members=[news_agent, weather_agent],
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    # model=OpenAIChat(id="gpt-4o")
)

# Run team and return the response as a variable
response = team.run("What is the weather in Tokyo?")
# Print the response
print(response.content)

################ STREAM RESPONSE #################
stream: Iterator[TeamRunOutputEvent] = team.run("What is the weather in Tokyo?", stream=True)
for chunk in stream:
    if chunk.event == "TeamRunContent":
        print(chunk.content)

# ################ STREAM AND PRETTY PRINT #################
stream: Iterator[TeamRunOutputEvent] = team.run("What is the weather in Tokyo?", stream=True)
pprint_run_response(stream, markdown=True)


# Team.arun() runs concurrent member delegation tasks (very powerful!)
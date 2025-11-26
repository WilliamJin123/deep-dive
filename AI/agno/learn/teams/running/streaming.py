from typing import Iterator
from agno.team import Team, TeamRunOutputEvent
from agno.agent import Agent
from agno.models.openai import OpenAIChat

news_agent = Agent(name="News Agent", role="Get the latest news")
weather_agent = Agent(name="Weather Agent", role="Get the weather for the next 7 days")

team = Team(
    name="News and Weather Team",
    members=[news_agent, weather_agent],
    model=OpenAIChat(id="gpt-4o")
)

# Run team and return the response as a stream
stream: Iterator[TeamRunOutputEvent] = team.run("What is the weather in Tokyo?", stream=True)
for chunk in stream:
    if chunk.event == "TeamRunContent":
        print(chunk.content)
        
        
#When your team is running asynchronously (using arun), the members will run concurrently if the team leader delegates to multiple members in one request.
# This means you will receive member events concurrently and the order of the events is not guaranteed.

#Learn thread management and vaoiding race conditions is a MUST

# Stream all events
response_stream = team.run(
    "What is the weather in Tokyo?",
    stream=True,
    stream_events=True
)

#Iterating over different types of events

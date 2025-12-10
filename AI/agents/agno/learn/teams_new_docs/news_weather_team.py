from agno.team import Team
from agno.agent import Agent
from agno.models.cerebras import Cerebras
from agno.tools.duckduckgo import DuckDuckGoTools

# Create specialized agents
news_agent = Agent(
    id="news-agent",
    name="News Agent",
    role="Get the latest news and provide summaries",
    tools=[DuckDuckGoTools()]
)

weather_agent = Agent(
    id="weather-agent",
    name="Weather Agent",
    role="Get weather information and forecasts",
    tools=[DuckDuckGoTools()]
)

reasoning_agent= Agent(model=Cerebras(id="zai-glm-4.6"),
    name="Reasoning Agent",
    id="reasoning_agent",
    role="Do reasoning and analysis tasks for the team leader"
)

# Create the team
team = Team(
    name="News and Weather Team",
    members=[news_agent, weather_agent],
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    # model=OpenAIChat(id="gpt-4o"),
    instructions="Coordinate with team members to provide comprehensive information. Delegate tasks based on the user's request.",
    # reasoning=True, # reasoning gives a system prompt to split up the task
    # useful for non-reasoning models, but might be redundant for thinking models

    # #USE reasoning_agent instead, otherwise the model context rots and it forgets to think AND toolcall
    # reasoning=True,
    # reasoning_agent=reasoning_agent,
    #agent doesn't work very well

    reasoning=True,
    reasoning_model=Cerebras(id="zai-glm-4.6")
    # debug_level=1,
    # debug_mode=True

    show_members_responses= True #intuitive, default only team leader toolcalls are shown
)

team.print_response("What's the latest news and weather in Tokyo?", stream=True)

## Conclusion: I don't like the reasoning "capability" agno provides
# Better to use thinking models or code custom logic
# NOTE: I think i am using reasoning capability wrong, ther eis. dedicated section to investigate, moving on 
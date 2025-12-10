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

# Create the team
team = Team(
    name="News and Weather Team",
    members=[news_agent, weather_agent],
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    # model=OpenAIChat(id="gpt-4o"),
    instructions="Coordinate with team members to provide comprehensive information. Delegate tasks based on the user's request.",
    # show_members_responses=False
)

team.print_response("What's the latest news and weather in Tokyo?", stream=True, )
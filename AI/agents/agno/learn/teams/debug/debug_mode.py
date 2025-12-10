# imports
from agno.team import Team
from agno.agent import Agent
from agno.models.cerebras import Cerebras

# Define a single Cerebras model instance (or create per agent)
cerebras_model = Cerebras(id="qwen-3-235b-a22b-instruct-2507")

# Create agents with Cerebras model
news_agent = Agent(
    name="News Agent",
    role="Fetch and summarize the latest global news",
    model=cerebras_model,           # ← Agent uses Cerebras
)

weather_agent = Agent(
    name="Weather Agent",
    role="Provide detailed 7-day weather forecasts for any city",
    model=cerebras_model,           # ← Agent uses Cerebras
)

# Create team with Cerebras as orchestrator model
team = Team(
    name="News and Weather Team",
    members=[news_agent, weather_agent],
    model=cerebras_model,           # ← Team uses Cerebras to route and respond
    debug_mode=True,                # Enable debug logs
    # debug_level=2,                # Optional: Enable for more verbose output
)

# Run query
team.print_response("What is the weather in Tokyo? Also, what are today's top 3 global headlines?")
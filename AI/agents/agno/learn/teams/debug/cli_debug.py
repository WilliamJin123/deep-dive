from agno.team import Team
from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.cerebras import Cerebras  # ← Switched to Cerebras

# Define the Cerebras model
model=Cerebras(id="qwen-3-235b-a22b-instruct-2507")

# Create agents using Cerebras
news_agent = Agent(
    name="News Agent",
    role="Get the latest news",
    model=model
)

weather_agent = Agent(
    name="Weather Agent",
    role="Get the weather for the next 7 days",
    model=model
)

# Create team with Cerebras as orchestrator and memory
team = Team(
    name="News and Weather Team",
    members=[news_agent, weather_agent],
    model=model,                            # ← Team uses Cerebras
    db=SqliteDb(db_file="tmp/data.db"),     # Persistent storage
    add_history_to_context=True,            # Include past runs
    num_history_runs=3,                     # Last 3 interaction pairs
    debug_mode=True                         # Optional: enable for visibility
)

# Run as interactive CLI app with streaming
team.cli_app(stream=True)
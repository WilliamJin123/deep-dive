from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.cerebras import Cerebras
from agno.tools.hackernews import HackerNewsTools

agent = Agent(
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    tools=[HackerNewsTools()],
    db=SqliteDb(db_file="tmp/data.db"),
    add_history_to_context=True,
    num_history_runs=3,
    markdown=True,
)

# Run agent as an interactive CLI app
agent.cli_app(stream=True)
from agno.agent import Agent
from agno.models.cerebras import Cerebras
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.db.sqlite import SqliteDb

agent = Agent(
    # model=OpenAIChat(id="gpt-4o"),
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    
    tools=[DuckDuckGoTools()],
    db=SqliteDb(db_file="tmp/agents.db"),
    add_history_to_context=True,
    num_history_runs=5,
    store_media=False,              # Don't store images/videos/audio/files
    store_tool_messages=False,       # Don't store tool execution details
    store_history_messages=False,   # Don't store history messages
)

agent.print_response("Search for the latest AI news and summarize it")
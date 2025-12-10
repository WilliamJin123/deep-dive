from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.cerebras import Cerebras
from agno.os import AgentOS
from agno.tools.mcp import MCPTools
import os

agent = Agent(
    name="Agno Agent",
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    # Add a database to the Agent
    db=SqliteDb(db_file="agno.db"),
    # Add the Agno MCP server to the Agent
    tools=[MCPTools(transport="streamable-http", url="https://docs.agno.com/mcp")],
    # Add the previous session history to the context
    add_history_to_context=True,
    markdown=True,
)

# Create the AgentOS
agent_os = AgentOS(agents=[agent])
# Get the FastAPI app for the AgentOS
app = agent_os.get_app()

if __name__ == "__main__":
    print("ran agno_os")
    agent_os.serve(app="agno_os:app", reload=True, port=8000) # host="0.0.0.0", port=8000) # filename:app
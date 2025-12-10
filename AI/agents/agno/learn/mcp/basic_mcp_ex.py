from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.mcp import MCPTools

# Create the Agent
agno_agent = Agent(
    name="Agno Agent",
    model=Claude(id="claude-sonnet-4-0"),
    # Add the Agno MCP server to the Agent
    tools=[MCPTools(transport="streamable-http", url="https://docs.agno.com/mcp")],
)

#automatically conencts() and closes() on every run, but less lifecycle control, explicitly use connect and close for maximum control
async with MCPTools(command="uvx mcp-server-git") as mcp_tools:
    agent = Agent(model=OpenAIChat(id="gpt-5-mini"), tools=[mcp_tools])
    await agent.aprint_response("What is the license for this project?", stream=True)

# Automatic Connection Management in AgentOS
# When using MCPTools within AgentOS, the lifecycle is automatically managed. No need to manually 
# connect or disconnect the MCPTools instance. This does not automatically refresh connections, 
# you can use refresh_connection to do so

# refreshes on each run if set refresh_connection = True
# the connection to the MCP server is checked and re-established IF NEEDED, and the list of available tools is then refreshed.

#probably set it to True

mcp_tools = MCPTools(command="uvx mcp-server-git", refresh_connection=True)
await mcp_tools.connect()

agent = Agent(model=OpenAIChat(id="gpt-5-mini"), tools=[mcp_tools])
await agent.aprint_response("What is the license for this project?", stream=True)  # The connection will be refreshed on each run.

await mcp_tools.close()


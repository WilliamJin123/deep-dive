#Doesn't work, will figure out later

from agno.agent import Agent
from agno.tools.mcp import MCPTools
from agno.models.cerebras import Cerebras
import asyncio
async def run_mcp_agent():

    # Initialize the MCP tools
    mcp_tools = MCPTools(command=f"uvx mcp-server-git")

    # Connect to the MCP server
    await mcp_tools.connect()

    agent = Agent(
        model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
        tools=[mcp_tools], markdown=True)
    await agent.aprint_response("What is the license for this project?", stream=True)
    ...
    
if __name__=="__main__":
    asyncio.run(run_mcp_agent())
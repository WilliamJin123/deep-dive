import asyncio
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.mcp_toolbox import MCPToolbox

#Toolbox loads a lot of tools, but filters to avoid tool overload (fancy term for context bloat)

async def main():
    # Connect to the running MCP Toolbox server and filter to hotel tools only
    async with MCPToolbox(
        url="http://127.0.0.1:5001",
        toolsets=["hotel-management"]  # Only load hotel search tools
    ) as toolbox:
        agent = Agent(
            model=OpenAIChat(),
            tools=[toolbox],
            instructions="You help users find hotels. Always mention hotel ID, name, location, and price tier."
        )
        
        # Ask the agent to find hotels
        await agent.aprint_response("Find luxury hotels in Zurich")

# Run the example
asyncio.run(main())
import asyncio
import os

from agno.agent import Agent
from agno.tools.mcp import MCPTools


async def run_agent(message: str) -> None:
    """Run the Airbnb and Google Maps agent with the given message."""

    env = {
        **os.environ,
        "GOOGLE_MAPS_API_KEY": os.getenv("GOOGLE_MAPS_API_KEY"),
    }

    # Initialize and connect to multiple MCP servers
    airbnb_tools = MCPTools(command="npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt")
    google_maps_tools = MCPTools(command="npx -y @modelcontextprotocol/server-google-maps", env=env
        # By providing this tool_name_prefix, all the tool names will be prefixed with "dev_" (avoid name collisions)
        tool_name_prefix="dev",                             
    )
    await airbnb_tools.connect()
    await google_maps_tools.connect()

    try:
        agent = Agent(
            tools=[airbnb_tools, google_maps_tools],
            markdown=True,
        )

        await agent.aprint_response(message, stream=True)
    finally:
        await airbnb_tools.close()
        await google_maps_tools.close()


# Example usage
if __name__ == "__main__":
    # Pull request example
    asyncio.run(
        run_agent(
            "What listings are available in Cape Town for 2 people for 3 nights from 1 to 4 August 2025?"
        )
    )

# Or use one MultiMCPTools instance

import asyncio
import os

from agno.agent import Agent
from agno.tools.mcp import MultiMCPTools


async def run_agent(message: str) -> None:
    """Run the Airbnb and Google Maps agent with the given message."""

    env = {
        **os.environ,
        "GOOGLE_MAPS_API_KEY": os.getenv("GOOGLE_MAPS_API_KEY"),
    }

    # Initialize and connect to multiple MCP servers
    mcp_tools = MultiMCPTools(
        commands=[
            "npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt",
            "npx -y @modelcontextprotocol/server-google-maps",
        ],
        env=env,

        # Set the allow_partial_failure to True to allow for partial failure connecting to the MCP servers
        # Otherwise one failure throws for all
        allow_partial_failure=True,

        
    )
    await mcp_tools.connect()

    try:
        agent = Agent(
            tools=[mcp_tools],
            markdown=True,
        )

        await agent.aprint_response(message, stream=True)
    finally:
        # Always close the connection when done
        await mcp_tools.close()


# Example usage
if __name__ == "__main__":
    # Pull request example
    asyncio.run(
        run_agent(
            "What listings are available in Cape Town for 2 people for 3 nights from 1 to 4 August 2025?"
        )
    )




import asyncio
from pathlib import Path
from textwrap import dedent

from agno.agent import Agent
from agno.models.cerebras import Cerebras
from agno.models.openai import OpenAIChat
from agno.tools.mcp import MCPTools


async def run_agent(message: str) -> None:
    """Run the filesystem agent with the given message."""

    file_path = "<path to the directory you want to explore>"

    # Initialize and connect to the MCP server to access the filesystem
    mcp_tools = MCPTools(command=f"npx -y @modelcontextprotocol/server-filesystem {file_path}")
    await mcp_tools.connect()

    try:
        agent = Agent(
            model=Cerebras(id="zai-glm-4.6"),
            # model=OpenAIChat(id="gpt-5-mini"),
            tools=[mcp_tools],
            instructions=dedent("""\
                You are a filesystem assistant. Help users explore files and directories.

                - Navigate the filesystem to answer questions
                - Use the list_allowed_directories tool to find directories that you can access
                - Provide clear context about files you examine
                - Use headings to organize your responses
                - Be concise and focus on relevant information\
            """),
            markdown=True,
        )

        # Run the agent
        await agent.aprint_response(message, stream=True)
    finally:
        # Always close the connection when done
        await mcp_tools.close()


# Example usage
if __name__ == "__main__":
    # Basic example - exploring project license
    asyncio.run(run_agent("What is the license for this project?"))
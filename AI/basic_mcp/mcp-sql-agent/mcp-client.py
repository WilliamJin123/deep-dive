import asyncio
import os
from dataclasses import dataclass, field
from typing import Union, cast
# import anthropic
# from anthropic.types import MessageParam, TextBlock, ToolUnionParam, ToolUseBlock
from cerebras.cloud.sdk import Cerebras
from cerebras.cloud.sdk.types import 
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# --- Load environment variables (for Anthropic API key) ---
load_dotenv()

cerebras_client = Cerebras(api_key=os.getenv("CEREBRAS_API_KEY"))
server_params = StdioServerParameters(command="python", args=["./mcp_server.py"], env=None)

@dataclass
class Chat:
    messages: list[MessageParam] = field(default_factory=list)
    system_prompt: str = """You are a master SQLite assistant. Use your tools to execute SQL queries and return clean results."""
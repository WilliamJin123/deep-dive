from agno.agent import Agent
from agno.models.cerebras import Cerebras
from agno.models.openai import OpenAIChat

# Importing our GoogleSearchTools ToolKit, containing multiple web search tools
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    # model=OpenAIChat(id="gpt-5-mini"),
    tools=[
        DuckDuckGoTools()
    ],
)

agent.print_response("What's the latest about OpenAIs GPT-5?", markdown=True)

from agno.tools.function import ToolResult
from agno.media import Image

@tool
def generate_image(prompt: str) -> ToolResult:
    """Generate an image from a prompt."""

    # Create your image (example)
    image_artifact = Image(
        id="img_123",
        url="https://example.com/generated-image.jpg",
        original_prompt=prompt
    )

    return ToolResult(
        content=f"Generated image for: {prompt}",
        images=[image]
    )
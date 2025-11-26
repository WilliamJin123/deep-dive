from agno.agent import Agent
from agno.media import Image
from agno.models.mistral import MistralChat
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=MistralChat("pixtral-large-2411"),
    tools=[DuckDuckGoTools()],
    markdown=True,
)

agent.print_response(
    "Tell me about this image and give me the latest news about it.",
    images=[
        Image(
            url="https://upload.wikimedia.org/wikipedia/commons/0/0c/GoldenGateBridge-001.jpg"
        )
    ],
    stream=True,
)
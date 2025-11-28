import random

from agno.models.cerebras import Cerebras
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools import tool

def get_weather(city: str) -> str:
    """Get the weather for the given city.
    
    Args:
        city (str): The city to get the weather for.
    """

    # In a real implementation, this would call a weather API
    weather_conditions = ["sunny", "cloudy", "rainy", "snowy", "windy"]
    random_weather = random.choice(weather_conditions)

    return f"The weather in {city} is {random_weather}."

# To equipt our Agent with our tool, we simply pass it with the tools parameter
agent = Agent(
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    # model=OpenAIChat(id="gpt-5-nano"),
    tools=[get_weather],
    markdown=True,
)

# Our Agent will now be able to use our tool, when it deems it relevant
agent.print_response("What is the weather in San Francisco?", stream=True)

def get_weather(city: str) -> str:
    """
    Get the weather for a given city.

    Args:
        city (str): The city to get the weather for.
    """
    return f"The weather in {city} is sunny."

# returned as
{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the weather for a given city.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The city to get the weather for."
                }
            },
            "required": ["city"]
        }
    }
}


from pydantic import BaseModel, Field

class GetWeatherRequest(BaseModel):
    city: str = Field(description="The city to get the weather for")

def get_weather(request: GetWeatherRequest) -> str:
    """
    Get the weather for a given city.

    Args:
        request (GetWeatherRequest): The request object containing the city to get the weather for.

    """
    return f"The weather in {request.city} is sunny."

# automatic pydantic conversion

#execute tools concurrently with arun, model must support parallel tool calls
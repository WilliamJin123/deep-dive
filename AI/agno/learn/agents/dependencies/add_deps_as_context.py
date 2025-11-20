import json
from textwrap import dedent

import httpx
from agno.agent import Agent
from agno.models.cerebras import Cerebras


def get_user_profile() -> str:
    """Fetch and return the user profile for a given user ID.

    Args:
        user_id: The ID of the user to retrieve the profile for
    """

    # Get the user profile from the database (this is a placeholder)
    user_profile = {
      "name": "John Doe",
      "experience_level": "senior",
    }

    return json.dumps(user_profile, indent=4)

agent = Agent(
    # model=OpenAIChat(id="gpt-5-mini"),
    model=Cerebras(id="llama-3.3-70b"),
    
    dependencies={"user_profile": get_user_profile},
    # We can add the entire dependencies dictionary to the user message
    add_dependencies_to_context=True,
    markdown=True,
)

agent.print_response(
    "Get the user profile for the user with ID 123 and tell me about their experience level.",
    stream=True,
)
# Optionally pass the dependencies to the print_response method
# agent.print_response(
#     "Get the user profile for the user with ID 123 and tell me about their experience level.",
#     dependencies={"user_profile": get_user_profile},
#     stream=True,
# )

# Get the user profile for the user with ID 123 and tell me about their experience level.                                                       
                                                                                                                                               
# <additional context>                                                                                                                     
# {                                                                                                                                        
# "user_profile": "{\n    \"name\": \"John Doe\",\n    \"experience_level\": \"senior\"\n}"                                              
# }                                                                                                                                        
# </additional context>
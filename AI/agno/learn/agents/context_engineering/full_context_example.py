from agno.agent import Agent
from agno.models.cerebras import Cerebras


agent = Agent(
    name="Helpful Assistant",
    model=Cerebras(id="llama-3.3-70b"),
    role="Assistant",
    description="You are a helpful assistant",
    instructions=["Help the user with their question"],
    additional_context="""
    Here is an example of how to answer the user's question: 
        Request: What is the capital of France?
        Response: The capital of France is Paris.
    """,
    expected_output="You should format your response with `Response: <response>`",
    markdown=True,
    add_datetime_to_context=True,
    add_location_to_context=True,
    add_name_to_context=True,
    add_session_summary_to_context=True,
    add_memories_to_context=True,
    add_session_state_to_context=True,
)

# You are a helpful assistant
# <your_role>
# Assistant
# </your_role>

# <instructions>
#   Help the user with their question
# </instructions>

# <additional_information>
# Use markdown to format your answers.
# The current time is 2025-09-30 12:00:00.
# Your approximate location is: New York, NY, USA.
# Your name is: Helpful Assistant.
# </additional_information>

# <expected_output>
#   You should format your response with `Response: <response>`
# </expected_output>

# Here is an example of how to answer the user's question: 
#     Request: What is the capital of France?
#     Response: The capital of France is Paris.

# You have access to memories from previous interactions with the user that you can use:

# <memories_from_previous_interactions>
# - User really likes Digimon and Japan.
# - User really likes Japan.
# - User likes coffee.
# </memories_from_previous_interactions>

# Note: this information is from previous interactions and may be updated in this conversation. You should always prefer information from this conversation over the past memories.

# Here is a brief summary of your previous interactions:

# <summary_of_previous_interactions>
# The user asked about information about Digimon and Japan.
# </summary_of_previous_interactions>

# Note: this information is from previous interactions and may be outdated. You should ALWAYS prefer information from this conversation over the past summary.

# <session_state> ... </session_state>
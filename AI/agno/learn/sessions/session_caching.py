from agno.agent import Agent
from agno.models.cerebras import Cerebras
# from agno.models.openai import OpenAIChat

agent = Agent(
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    # model=OpenAIChat(id="gpt-4o"),
    session_id="my_session",
    cache_session=True,  # Enable in-memory caching
)

# First run loads from database and caches
agent.run("First message")

# Subsequent runs use cached session (faster)
agent.run("Second message")

#This is only for development and testing purposes. It is not recommended for production use.
from agno.agent import Agent
from agno.models.cerebras import Cerebras

agent = Agent(
    # model=OpenAIChat(id="gpt-5-mini"),
    model=Cerebras(id="llama-3.3-70b"),
    
    dependencies={"name": "John Doe"},
    instructions="You are a story writer. The current user is {name}."
)

agent.print_response("Write a 5 second short story about {name}")
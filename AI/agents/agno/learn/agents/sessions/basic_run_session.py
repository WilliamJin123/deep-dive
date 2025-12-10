from agno.agent import Agent
from agno.models.cerebras import Cerebras

agent = Agent(model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"))

# Run agent and return the response as a variable
response = agent.run("Tell me a 5 second short story about a robot")
print(response.content)
print(response.run_id)
print(response.session_id)
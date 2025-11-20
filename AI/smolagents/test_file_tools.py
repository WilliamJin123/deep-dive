from smolagents import CodeAgent
from cerebras_agent import makeCerebrasAgent
from file_tools import TOOLS

# Example: give the list of tools to your smolagent
agent = CodeAgent(
    model=makeCerebrasAgent(),
    tools=TOOLS,
    verbosity_level=2,
    
)
response = agent.run("Create a folder named 'project' and write a README inside it. Make the README about pineapples.")
print(response)

response = agent.run(
    "Go into the 'project' directory, list all the files and directories you see, "
    "and then delete everything except for the README file."
)
print(response)

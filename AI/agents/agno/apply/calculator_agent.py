from pathlib import Path
from agno.agent import Agent
from agno.models.cerebras import Cerebras
from agno.skills import Skills, LocalSkills

# Get the path to the skills directory
# Assuming we are running from the root of the repo, or relative to this file
# This file is in apply/
# Skills are in apply/skills
skills_dir = Path(__file__).parent / "skills"

# Initialize the Agent
agent = Agent(
    model=Cerebras(id="gpt-oss-120b"),
    name="Calculator Agent",
    instructions=[
        "You are a helpful assistant with a calculator skill.",
        "When asked to calculate a math expression, use the `calculator` skill.",
        "To use the skill, use the available function `get_skill_script` to run 'calculate.bat' with the expression as an argument.",
        "Example: get_skill_script(skill_name='calculator', script_path='calculate.bat', args=['2 + 2'])",
        "Always output the result clearly."
    ],
    skills=Skills(loaders=[LocalSkills(str(skills_dir))]),
    markdown=True,
    debug_mode=True, # Enable debug to see tool calls
)

if __name__ == "__main__":
    # Test the agent
    agent.print_response("Calculate the square root of 144 multiplied by 12", stream=True)

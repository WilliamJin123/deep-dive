from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.skills import Skills, LocalSkills

# Load skills from a directory
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    skills=Skills(loaders=[LocalSkills("/path/to/skills")])
)

from agno.skills import Skills, LocalSkills

# Load all skills from the directory
skills = Skills(loaders=[LocalSkills("/path/to/skills")])

from agno.skills import Skills, LocalSkills

# Load a single skill directory
skills = Skills(loaders=[LocalSkills("/path/to/skills/code-review")])

from agno.skills import Skills, LocalSkills

skills = Skills(loaders=[
    LocalSkills("/path/to/shared-skills"),
    LocalSkills("/path/to/project-skills"),
])


# Agent Tools
# When you add skills to an agent, it automatically gets access to these tools:
# Tool	Description
# get_skill_instructions(skill_name)	Load full instructions for a skill
# get_skill_reference(skill_name, reference_path)	Load a reference document
# get_skill_script(skill_name, script_path, execute, args, timeout)	Read or execute a script

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    skills=Skills(loaders=[LocalSkills("/path/to/skills")]),
    instructions=[
        "You have access to specialized skills.",
        "Use get_skill_instructions to load full guidance when needed.",
    ],
)

# The agent will automatically use skills when relevant
agent.print_response("Review this code for best practices: def foo(): pass")

# ... skills are modified on disk ...

# Reload to pick up changes
skills.reload()


from agno.skills import Skills, LocalSkills, SkillValidationError
# Error handling
try:
    skills = Skills(loaders=[LocalSkills("/path/to/skills")])
except SkillValidationError as e:
    print(f"Skill validation failed: {e}")
    print(f"Errors: {e.errors}")


    from pathlib import Path
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.skills import Skills, LocalSkills

# Get skills directory relative to this file
skills_dir = Path(__file__).parent / "skills"

# Create agent with skills
agent = Agent(
    name="Code Assistant",
    model=OpenAIChat(id="gpt-4o"),
    skills=Skills(loaders=[LocalSkills(str(skills_dir))]),
    instructions=[
        "You are a helpful coding assistant with access to specialized skills."
    ],
    markdown=True,
)

if __name__ == "__main__":
    agent.print_response(
        "Review this Python function:\n\n"
        "def calc(x,y): return x+y"
    )
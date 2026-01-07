from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.skills import Skills, LocalSkills

# Load skills from a directory
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    skills=Skills(loaders=[LocalSkills("/path/to/skills")])
)

# Load all skills at once
from agno.skills import Skills, LocalSkills

skills = Skills(loaders=[LocalSkills("/path/to/skills")])

# The agent now has access to skill tools:
# - get_skill_instructions(skill_name)
# - get_skill_reference(skill_name, reference_path)
# - get_skill_script(skill_name, script_path)

# ---
# name: my-skill
# description: Short description of what this skill does
# ---


# skills/
# ├── code-review/
# │   ├── SKILL.md
# │   ├── scripts/
# │   └── references/
# ├── git-workflow/
# │   ├── SKILL.md
# │   ├── scripts/
# │   └── references/
# └── testing/
#     ├── SKILL.md
#     └── references/
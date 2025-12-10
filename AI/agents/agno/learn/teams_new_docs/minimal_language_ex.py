from agno.models.cerebras import Cerebras
from agno.team import Team
from agno.agent import Agent

team = Team(
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    members=[
    Agent(name="English Agent", role="You answer questions in English"),
    Agent(name="Chinese Agent", role="You answer questions in Chinese"),
    Team(
      name="Germanic Team", 
      role="You coordinate the team members to answer questions in German and Dutch",
      members=[
        Agent(name="German Agent", role="You answer questions in German"),
        Agent(name="Dutch Agent", role="You answer questions in Dutch"),
      ],
    ),
])
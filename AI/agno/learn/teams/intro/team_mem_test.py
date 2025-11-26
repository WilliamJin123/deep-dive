from agno.agent import Agent
from agno.team import Team
from agno.db.sqlite import SqliteDb
from agno.models.cerebras import Cerebras


# Shared database
db = SqliteDb(db_file="agno.db")

# Agents and team using the same database and user context
agent1 = Agent(
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    db=db, enable_user_memories=True, user_id="user1")

agent2 = Agent(
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    db=db, enable_user_memories=True, user_id="user1")

team = Team(
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    members=[agent1, agent2], db=db, enable_user_memories=True, user_id="user1")

# Any memory created by one agent is accessible by others
agent1.print_response("My name is John.")
team.print_response("What is my name?")  # Will respond: "Your name is John."
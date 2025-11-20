from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.cerebras import Cerebras
from agno.run import RunContext

def get_user_profile(run_context: RunContext) -> str:
    """Get the user profile."""
    return run_context.dependencies["user_profiles"][run_context.user_id]

agent = Agent(
    # model=OpenAIChat(id="gpt-5-mini"),
    model=Cerebras(id="llama-3.3-70b"),
    db=SqliteDb(db_file="tmp/agents.db"),
    tools=[get_user_profile],
    dependencies={"user_profiles": {"user_1001": {"name": "John Doe", "experience_level": "senior"}, "user_1002": {"name": "Jane Doe", "experience_level": "junior"}}},
)

agent.print_response("Get the user profile for the current user and tell me about their experience level.", user_id="user_1002", stream=True)
from agno.agent import Agent
from agno.models.cerebras import Cerebras
from agno.db.sqlite import SqliteDb

agent = Agent(
    db=SqliteDb(db_file="tmp/agentic_session.db"),
    # model=OpenAIChat(id="gpt-5-mini"),
    model=Cerebras(id="llama-3.3-70b"),  # qwen-3-235b-a22b-instruct-2507 is really bad at modifying agentic state automatically for some reason.
    # in general for prod I think it's good to define how session state is edited explicitly
    session_state={"shopping_list": []},
    add_session_state_to_context=True,  # Required so the agent is aware of the session state
    enable_agentic_state=True,  # Adds a tool to manage the session state
)

agent.print_response("Add milk, eggs, and bread to the shopping list", stream=True)
print(f"Session state: {agent.get_session_state()}")
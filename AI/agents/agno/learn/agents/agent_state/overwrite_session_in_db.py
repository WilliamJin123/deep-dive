from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.cerebras import Cerebras

# Create an Agent that maintains state
agent = Agent(
    # model=OpenAIChat(id="gpt-4o-mini"),
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    db=SqliteDb(db_file="tmp/agents.db"),
    markdown=True,
    # Set the default session_state. The values set here won't be overwritten - they are the initial state for all sessions.
    session_state={},
    # Adding the session_state to context for the agent to easily access it
    add_session_state_to_context=True,
    # Allow overwriting the stored session state with the session state provided in the run
    overwrite_db_session_state=True, #defualt False, will append to session_state 
)

# Let's run the agent providing a session_state. This session_state will be stored in the database.
agent.print_response(
    "Can you tell me what's in your session_state?",
    session_state={"shopping_list": ["Potatoes"]},
    stream=True,
)
print(f"Stored session state: {agent.get_session_state()}")

# Now if we pass a new session_state, it will overwrite the stored session_state.
agent.print_response(
    "Can you tell me what is in your session_state?",
    session_state={"secret_number": 43},
    stream=True,
)
print(f"Stored session state: {agent.get_session_state()}")
#only secret number if overwrite
#Stored session state: {'shopping_list': ['Potatoes'], 'secret_number': 43}   if no overwrite
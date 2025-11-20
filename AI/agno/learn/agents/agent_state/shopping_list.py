from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.cerebras import Cerebras
from agno.run import RunContext

# Define a tool that adds an item to the shopping list
def add_item(run_context: RunContext, item: str) -> str:
    """Add an item to the shopping list."""

    # We access the session state via run_context.session_state
    run_context.session_state["shopping_list"].append(item)

    return f"The shopping list is now {run_context.session_state['shopping_list']}"


# Create an Agent that maintains state
agent = Agent(
    # model=OpenAIChat(id="gpt-5-mini"),
    # model=Cerebras(id="llama-3.3-70b"),
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    
    # Database to store sessions and their state
    db=SqliteDb(db_file="tmp/agents.db"),
    # Initialize the session state with an empty shopping list. This will be the default state for all sessions.
    session_state={"shopping_list": []},
    tools=[add_item],
    # You can use variables from the session state in the instructions
    instructions="Current state (shopping list) is: {shopping_list}",
    markdown=True,
    add_history_to_context=True,
    num_history_messages=3,
    read_chat_history=True,
)

# Example usage
# agent.print_response("Add milk, eggs, and bread to the shopping list", session_id=123, stream=True)

#ts is persistent!
agent.print_response("What was my last user message and what is in the shopping list?", session_id=123, stream=True)
print(f"Final session state: {agent.get_session_state(session_id=123)}")


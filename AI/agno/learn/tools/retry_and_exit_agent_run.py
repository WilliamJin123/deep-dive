from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.exceptions import RetryAgentRun
from agno.models.openai import OpenAIChat
from agno.utils.log import logger
from agno.run import RunContext


def add_item(run_context: RunContext, item: str) -> str:
    """Add an item to the shopping list."""
    if not run_context.session_state:
        run_context.session_state = {}
    
    if "shopping_list" not in run_context.session_state:
        run_context.session_state["shopping_list"] = []
    
    run_context.session_state["shopping_list"].append(item)
    len_shopping_list = len(run_context.session_state["shopping_list"])
    
    if len_shopping_list < 3:
        raise RetryAgentRun(
            f"Shopping list is: {run_context.session_state['shopping_list']}. Minimum 3 items in the shopping list. "
            + f"Add {3 - len_shopping_list} more items.",
        )
    
    logger.info(f"The shopping list is now: {run_context.session_state.get('shopping_list')}")
    return f"The shopping list is now: {run_context.session_state.get('shopping_list')}"


agent = Agent(
    model=OpenAIChat(id="gpt-5-mini"),
    session_id="retry_example_session",
    db=SqliteDb(
        session_table="retry_example_session",
        db_file="tmp/retry_example.db",
    ),
    # Initialize the session state with empty shopping list
    session_state={"shopping_list": []},
    tools=[add_item],
    markdown=True,
)
agent.print_response("Add milk", stream=True)
print(f"Final session state: {agent.get_session_state(session_id='retry_example_session')}")



from agno.agent import Agent
from agno.exceptions import StopAgentRun
from agno.models.openai import OpenAIChat
from agno.run import RunContext


def check_condition(run_context: RunContext, value: int) -> str:
    """Check a condition and stop tool calls if met."""
    if value > 100:
        raise StopAgentRun(
            f"Value {value} exceeds threshold. Stopping tool call execution."
        )
    return f"Value {value} is acceptable."


agent = Agent(
    model=OpenAIChat(id="gpt-5-mini"),
    tools=[check_condition],
    markdown=True,
)

# When the model calls check_condition with value > 100,
# the tool call loop will exit and the run will complete
agent.print_response("Use the check_condition tool to check if 150 is acceptable", stream=True)
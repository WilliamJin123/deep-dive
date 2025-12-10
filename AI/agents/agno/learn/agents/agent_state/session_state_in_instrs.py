from textwrap import dedent

from agno.agent import Agent
from agno.models.cerebras import Cerebras
from agno.db.sqlite import SqliteDb


agent = Agent(
    db=SqliteDb(db_file="tmp/agents.db"),
    # model=OpenAIChat(id="gpt-5-mini"),
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    # Initialize the session state with a variable
    session_state={"user_name": "John"},
    # You can use variables from the session state in the instructions
    instructions="Users name is {user_name}",
    markdown=True,
)

agent.print_response("What is my name?", stream=True)
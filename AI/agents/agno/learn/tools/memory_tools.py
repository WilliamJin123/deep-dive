from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.cerebras import Cerebras

from agno.tools.memory import MemoryTools

# has all the base memory operations (CRUD memory) for user preferences / attributes (ex John likes ice cream)

#also uses session state additional properties to store thinking and analyzing

# overall not a big fan of memory, reasoning, workflow, and knwoledge tools with thinking and analyzing 
# (by itself these properties are very useful) I think there is better context management solutions
# also if this is a difference maker you are probably not designing your applications well enough

# Create a database connection
db = SqliteDb(
    db_file="tmp/memory.db"
)

memory_tools = MemoryTools(
    db=db,
)

agent = Agent(
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    tools=[memory_tools],
    markdown=True,
)

agent.print_response(
    "My name is John Doe and I like to hike in the mountains on weekends. "
    "I like to travel to new places and experience different cultures. "
    "I am planning to travel to Africa in December. ",
    user_id="john_doe@example.com",
    stream=True
)

# This won't use the session history, but instead will use the memory tools to get the memories
agent.print_response("What have you remembered about me?", stream=True, user_id="john_doe@example.com")
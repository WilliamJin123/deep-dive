from agno.models.cerebras import Cerebras
from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from rich.pretty import pprint

user_id = "ava"

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

# Use SQLite instead — simple and reliable
db = SqliteDb(
    db_file="agno_user_memories.db",  # Stores data locally in this file
    memory_table="user_memories",     # Optional: custom table name
)


# Initialize Agent
memory_agent = Agent(
    # model=OpenAIChat(id="gpt-4.1"),
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    
    db=db,
    # Give the Agent the ability to update memories
    enable_agentic_memory=True,
    # OR - Run the MemoryManager automatically after each response
    enable_user_memories=True,
    markdown=True,
)

db.clear_memories()

memory_agent.print_response(
    "My name is Ava and I like to ski.",
    user_id=user_id,
    stream=True,
    stream_events=True,
)
print("Memories about Ava:")
pprint(memory_agent.get_user_memories(user_id=user_id))

memory_agent.print_response(
    "I live in san francisco, where should i move within a 4 hour drive?",
    user_id=user_id,
    stream=True,
    stream_events=True,
)
print("Memories about Ava:")
pprint(memory_agent.get_user_memories(user_id=user_id))
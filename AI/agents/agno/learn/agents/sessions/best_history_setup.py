
import os
from agno.agent import Agent
from agno.models.cerebras import Cerebras
from agno.db.sqlite import SqliteDb

# Define the database file path
DB_FILE = "tmp/data.db"

# Ensure a fresh start by deleting the old database file
if os.path.exists(DB_FILE):
    os.remove(DB_FILE)

# Initialize the Agent with history enabled
agent = Agent(
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    db=SqliteDb(db_file=DB_FILE),
    add_history_to_context=True,
    num_history_runs=3,
    read_chat_history=True,
    debug_mode=True,
    description="You are a helpful assistant that always responds in a polite, upbeat and positive manner.",
)

# 1. Initial message to start the conversation
agent.print_response("Share a 2 sentence horror story", stream=True)

# 2. Test immediate recall of the first message
agent.print_response("What was my first message?", stream=True)

# 3. Change the topic to test contextual memory
agent.print_response("That's spooky! Now, can you write a short, happy poem about a sunrise?", stream=True)

# 4. Test recall of the agent's own previous response
agent.print_response("I like the poem. Before that, you told me a horror story. Can you remind me what the second sentence of that story was?", stream=True)

# 5. Add another topic to push older messages out of the history window
agent.print_response("Great, thanks! Let's talk about space. What's the biggest planet in our solar system?", stream=True)

# 6. CRITICAL TEST: Ask for the first message, which is now outside the 'num_history_runs=3' window
agent.print_response("What was my absolute first message in this entire conversation? The one about the horror story.", stream=True)

# 7. Test recall of the most recent message, which should still be in context
agent.print_response("No problem! What was the last thing you said about space?", stream=True)
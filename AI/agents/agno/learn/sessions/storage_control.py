from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    db=SqliteDb(db_file="tmp/agent.db"),
    store_media=False,           # Media stored externally
    store_tool_messages=False,   # Tool results not needed
    store_history_messages=False, # Only current run persisted
)

# three controls default to true

session = agent.set_session_name(
    session_id="session_123",
    # session_name="Example",
    autogenerate=True #Agent model autogenerates name
)
# Access the generated name
name = agent.get_session_name(session_id="session_123")
print(name)  # e.g. "E-commerce API Planning"

# Best Practices:
# Delay generation until the conversation has meaningful context (e.g., after 2–3 messages)
# Provide a fallback: wrap the call in your own helper that falls back to a human-entered name or a ticket ID if the generation fails
# Batch jobs: loop over session IDs from your database and call set_session_name(..., autogenerate=True) once for each. The API is synchronous, so plan around model latency
# Costs: Each generation is an extra model call. Use cheaper models via session_summary_manager or run it out-of-band if you’re cost sensitive


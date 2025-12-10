from agno.agent import Agent
from agno.models.cerebras import Cerebras
from agno.db.sqlite import SqliteDb
# from agno.models.openai import OpenAIChat

agent = Agent(
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    db=SqliteDb(db_file="tmp/data.db"),
    session_id="WJ_session123"
    read_chat_history=True,  # Model can call get_chat_history() tool
    add_history_to_context=True,
    num_history_runs=3,  # Last 3 conversation turns
)

# All messages excluding those marked as from_history
chat_history = agent.get_chat_history()

# User-assistant message pairs from each run
messages = agent.get_session_messages()

# Last run output with metrics and tool calls
last_run = agent.get_last_run_output()

# Choosing a Pattern
# Short chats: Leave defaults (history off) or enable add_history_to_context with num_history_runs=3
# Long-lived threads: Combine limited history (num_history_runs=2) with session summaries to keep tokens manageable
# Tool-heavy agents: Use max_tool_calls_from_history to limit tool call noise in context
# Audit/debug flows: Enable read_chat_history=True so the model looks things up only when needed
# Cross-session recall: Use search_session_history=True with num_history_sessions=2 (keep low to avoid context limits)
# Programmatic workflows: Call get_session_messages() / get_chat_history() directly in your code


from agno.agent import Agent
from agno.db.postgres import PostgresDb
from agno.models.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    db=PostgresDb(db_url="postgresql+psycopg://ai:ai@localhost:5532/ai"),
    enable_session_summaries=True,
)

agent.print_response("Hi my name is John and I live in New York", session_id="conversation_123")

# Retrieve the summary
summary = agent.get_session_summary(session_id="conversation_123")
if summary:
    print(summary.summary, summary.topics)
    
    
#SessionSummaryManager for customization!

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    db=db,
    add_session_summary_to_context=True,
    add_history_to_context=True,
    num_history_runs=2,  # Summary for long-term memory, last 2 runs for detail
)


# When to Use Session Summaries
# ✅ Perfect for:
# Long-running customer support conversations
# Multi-day or multi-week interactions
# Conversations with 10+ turns
# Production systems where cost matters
# ⚠️ Consider alternatives for:
# Short conversations (fewer than 5 turns)
# When full detail is critical
# Real-time chat with recent context only
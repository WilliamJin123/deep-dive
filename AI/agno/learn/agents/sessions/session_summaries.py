from agno.agent import Agent
from agno.models.google.gemini import Gemini
from agno.db.sqlite import SqliteDb

db = SqliteDb(db_file="tmp/data.db")

user_id = "jon_hamm@example.com"
session_id = "1001"

agent = Agent(
    model=Gemini(id="gemini-2.5-flash"),
    db=db,
    enable_session_summaries=True, # causes the agent to update session summary after every run 
    # using a session manager (another llm, same model by default) with its own prompt
)

agent.print_response(
    "What can you tell me about quantum computing?",
    stream=True,
    user_id=user_id,
    session_id=session_id,
)

agent.print_response(
    "I would also like to know about LLMs?",
    stream=True,
    user_id=user_id,
    session_id=session_id
)

session_summary = agent.get_session_summary(session_id=session_id)
print(f"Session summary: {session_summary.summary}")


from agno.agent import Agent
from agno.session import SessionSummaryManager
from agno.models.cerebras import Cerebras
from agno.db.sqlite import SqliteDb

input("\n\nNow showing Session Manager (Separate LLM that defaults to agent model, does the summaries with a summary prompt.)\n")

# Setup your database
db = SqliteDb(db_file="agno.db")

# Setup your Session Summary Manager, to adjust how summaries are created
session_summary_manager = SessionSummaryManager(
    # Select the model used for session summary creation and updates. If not specified, the agent's model is used by default.
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    # You can also overwrite the prompt used for session summary creation
    session_summary_prompt="Create a very succinct summary of the following conversation:",
)

# Now provide the adjusted Memory Manager to your Agent
agent = Agent(
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    db=db,
    session_summary_manager=session_summary_manager,
    enable_session_summaries=True,
)

agent.print_response(
    "What can you tell me about quantum computing?",
    stream=True,
    user_id=user_id,
    session_id=session_id,
)

agent.print_response(
    "I would also like to know about LLMs?",
    stream=True,
    user_id=user_id,
    session_id=session_id
)

session_summary = agent.get_session_summary(session_id=session_id)
print(f"Session summary: {session_summary.summary}")
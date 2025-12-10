from agno.agent import Agent
from agno.models.cerebras import Cerebras
from agno.team import Team
from agno.db.sqlite import SqliteDb


#need db for session history
db = SqliteDb(
    db_file="tmp/sessions.db",
    session_table="Poems"
)

# Create an Agent and a Team — they will automatically use the named loggers
agent = Agent(model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
 name="WriterAgent",
 db=db,
 add_history_to_context=True, 
 num_history_messages=3,
#  read_chat_history=True,
 )
team = Team(
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    members=[agent], name="WritingTeam",
    db=db,
    add_history_to_context=True, 
    num_history_messages=3,
    # read_chat_history=True,  #unneessary as team and agent now share same session, conversational history, but good for robustness
    )



session_id = "poetry_session_002"

# Run agent — logs will go to agent_logs.log
agent.print_response(
    "As WriterAgent, write a short poem about logging. Print it.",
    session_id=session_id
)
# Run team — logs (if any warning/error) go to team_logs.log
team.print_response("Output the previous poem",
    session_id=session_id                    
) 
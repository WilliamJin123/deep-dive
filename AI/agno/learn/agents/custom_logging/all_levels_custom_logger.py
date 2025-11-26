import logging
from agno.agent import Agent
from agno.models.cerebras import Cerebras
from agno.team import Team
from agno.db.sqlite import SqliteDb

# Set up custom logging configuration
def setup_agno_loggers():
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(asctime)s - %(message)s')

    # Logger for Agents: agno.agent
    agent_logger = logging.getLogger("agno.agent")
    agent_logger.setLevel(logging.INFO)
    agent_handler = logging.FileHandler("agent_logs.log")
    agent_handler.setFormatter(formatter)
    agent_logger.addHandler(agent_handler)
    agent_logger.propagate = False  # Prevent duplicate logs

    # Logger for Teams: agno.team
    team_logger = logging.getLogger("agno.team")
    team_logger.setLevel(logging.WARNING)
    team_handler = logging.FileHandler("team_logs.log")
    team_handler.setFormatter(formatter)
    team_logger.addHandler(team_handler)
    team_logger.propagate = False

    # Logger for Workflows: agno.workflow
    workflow_logger = logging.getLogger("agno.workflow")
    workflow_logger.setLevel(logging.DEBUG)
    workflow_handler = logging.FileHandler("workflow_logs.log")
    workflow_handler.setFormatter(formatter)
    workflow_logger.addHandler(workflow_handler)
    workflow_logger.propagate = False

# Call setup before creating agents/teams
setup_agno_loggers()


#need db for session history
db = SqliteDb(
    db_file="tmp/sessions.db",
    session_table=True
)

# Create an Agent and a Team — they will automatically use the named loggers
agent = Agent(model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
 name="WriterAgent",
 db=db,
 add_history_to_context=True, 
 num_history_messages=3,
 read_chat_history=True,
 )
team = Team(
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    members=[agent], name="WritingTeam",
    db=db,
    add_history_to_context=True, 
    num_history_messages=3,
    read_chat_history=True,
    )



session_id = "poetry_session_001"

# Run agent — logs will go to agent_logs.log
team.print_response(
    "As WriterAgent, write a short poem about logging.",
    session_id=session_id
)
# Run team — logs (if any warning/error) go to team_logs.log
team.print_response("Revise the previous poem for clarity.", session_id=session_id)
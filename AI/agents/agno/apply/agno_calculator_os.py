from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.os import AgentOS
from calculator_agent import agent

# Enhance the existing agent with Database and Session parameters for Agno OS
# We are adding persistence and history context which is crucial for a robust OS agent
agent.db = SqliteDb(db_file="apply/calculator_agent_sessions.db")
agent.add_history_to_context = True
agent.num_history_runs = 5
agent.debug_mode = True

# Initialize AgentOS with the enhanced agent
agent_os = AgentOS(agents=[agent])

# Get the FastAPI app
app = agent_os.get_app()

if __name__ == "__main__":
    # Serve the application
    # Note: When running this, make sure to use the correct import path for the app string
    print("Starting Calculator Agent OS...")
    agent_os.serve(app="agno_calculator_os:app", reload=True, port=8001)

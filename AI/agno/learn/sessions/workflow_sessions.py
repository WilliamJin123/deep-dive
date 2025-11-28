# A session in an agent / team is one single conversation with multiple runs (messages)

# A workflow session is an E2E run of the workflow i.e. execution history

from agno.workflow import Workflow
from agno.db.sqlite import SqliteDb

workflow = Workflow(
    name="Research Pipeline",
    db=SqliteDb(db_file="workflows.db"),
    steps=[...],
)

# Each run creates or updates the workflow session
result = workflow.run(input="AI trends", session_id="session_123")

@dataclass
class WorkflowSession:
    session_id: str           # Unique session identifier
    user_id: str | None       # User who owns this session
    workflow_id: str | None   # Which workflow this belongs to
    workflow_name: str | None # Name of the workflow
    
    # List of all workflow runs (executions)
    runs: List[WorkflowRunOutput] | None
    
    # Session-specific data
    session_data: Dict | None    # Includes session_name, session_state
    workflow_data: Dict | None   # Workflow configuration
    metadata: Dict | None        # Custom metadata
    
    created_at: int | None    # Unix timestamp
    updated_at: int | None    # Unix timestamp
    
    #NO SUMMARIES
    
from agno.workflow import Workflow
from agno.db.sqlite import SqliteDb

workflow = Workflow(
    name="Content Pipeline",
    db=SqliteDb(db_file="workflows.db"),
    steps=[...],
    add_workflow_history_to_steps=True,  # Include previous runs
    num_history_runs=5,                  # Limit how many runs to load
)

# <workflow_history_context>
# [Workflow Run-1]
# User input: Create a blog post about AI
# Workflow output: [Full output from run]

# [Workflow Run-2]
# User input: Write about machine learning
# Workflow output: [Full output from run]
# </workflow_history_context>

workflow.run(input="Analyze AI trends", session_id="session_123")
workflow.set_session_name(session_id="session_123", session_name="AI Trends Analysis Q4 2024")

# Retrieve the name
name = workflow.get_session_name(session_id="session_123")
print(name)  # "AI Trends Analysis Q4 2024"


workflow = Workflow(
    name="Research Pipeline",
    description="Automated research and analysis pipeline",
    db=SqliteDb(db_file="workflows.db"),
    steps=[...],
)

workflow.run(input="Research topic", session_id="session_123")
workflow.set_session_name(session_id="session_123", autogenerate=True)

name = workflow.get_session_name(session_id="session_123")
print(name)  # "Automated research and analysis pipel - 2024-11-19 14:30"
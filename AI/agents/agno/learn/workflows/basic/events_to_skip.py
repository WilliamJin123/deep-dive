from agno.run.workflow import WorkflowRunEvent

# Common events you might want to skip
events_to_skip = [
    WorkflowRunEvent.workflow_started,
    WorkflowRunEvent.workflow_completed,
    WorkflowRunEvent.workflow_cancelled,
    WorkflowRunEvent.step_started,
    WorkflowRunEvent.step_completed,
    WorkflowRunEvent.parallel_execution_started,
    WorkflowRunEvent.parallel_execution_completed,
    WorkflowRunEvent.condition_execution_started,
    WorkflowRunEvent.condition_execution_completed,
    WorkflowRunEvent.loop_execution_started,
    WorkflowRunEvent.loop_execution_completed,
    WorkflowRunEvent.router_execution_started,
    WorkflowRunEvent.router_execution_completed,
]
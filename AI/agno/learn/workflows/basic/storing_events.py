# store everything
debug_workflow = Workflow(
    name="Debug Workflow",
    store_events=True,
    steps=[...]
)

# store only important events
production_workflow = Workflow(
    name="Production Workflow",
    store_events=True,
    events_to_skip=[
        WorkflowRunEvent.step_started,
        WorkflowRunEvent.parallel_execution_started,
        # keep step_completed and workflow_completed
    ],
    steps=[...]
)

# No event storage
fast_workflow = Workflow(
    name="Fast Workflow",
    store_events=False,
    steps=[...]
)
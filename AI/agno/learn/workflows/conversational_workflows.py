# add a WorkflowAgent to your workflow that intelligently decides whether to:
    # Answer directly based on the current input and past workflow results
    # Run the workflow when the input cannot be answered based on past results

from agno.workflow import WorkflowAgent
from agno.workflow.workflow import Workflow
from agno.models.cerebras import Cerebras


workflow_agent = WorkflowAgent(
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    # model=OpenAIChat(id="gpt-4o-mini"),  # Set the model that should be used
    num_history_runs=4, # How many of the previous runs should it take into account
    instructions="You are a helpful assistant that can answer questions and run workflows when new processing is needed.",
)

#super restricted:
# model: Model,
# instructions: str | None = None,
# add_workflow_history: bool = True,
# num_history_runs: int = 5

workflow = Workflow(
    name="Story Generation Workflow",
    description="A workflow that generates stories, formats them, and adds references",
    agent=workflow_agent,
)
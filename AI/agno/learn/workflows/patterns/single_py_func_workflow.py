from agno.workflow import Workflow, WorkflowExecutionInput

def custom_workflow_function(workflow: Workflow, execution_input: WorkflowExecutionInput):
    # Custom orchestration logic
    research_result = research_team.run(execution_input.message)
    analysis_result = analysis_agent.run(research_result.content)
    return f"Final: {analysis_result.content}"

workflow = Workflow(
    name="Function-Based Workflow",
    steps=custom_workflow_function  # Single function replaces all steps
)

workflow.print_response("Evaluate the market potential for quantum computing applications", markdown=True)
from agno.workflow import Step, StepInput, StepOutput, Steps, Workflow

workflow = Workflow(
    # steps=[research_step, analysis_step, writing_step],
    add_workflow_history_to_steps=True  # All steps get history
)

Step(
    name="Content Creator", 
    # agent=content_agent,
    add_workflow_history=True  # Only this step gets history
)

#history structure
"""
<workflow_history_context>
[run-1]
input: Create content about AI in healthcare
response: # AI in Healthcare: Transforming Patient Care...

[run-2] 
input: Make it more family-focused
response: # AI in Family Healthcare: A Parent's Guide...
</workflow_history_context>

Your current input goes here...
"""

[
    ("<workflow input from run 1>")("<workflow output from run 1>"),
    ("<workflow input from run 2>")("<workflow output from run 2>"),
]


# get workflow history tool with num_runs

# List of tuples vs context string

# step_input.get_workflow_history(num_runs=3)
# step_input.get_workflow_history_context(num_runs=3)
def custom_function(step_input: StepInput) -> StepOutput:
    # Option 1: Structured data for analysis
    history_tuples = step_input.get_workflow_history(num_runs=3)
    for user_input, workflow_output in history_tuples:
        # Process each conversation turn

    # Option 2: Formatted context for agents  
    context_string = step_input.get_workflow_history_context(num_runs=3)

    return StepOutput(content="Analysis complete")

# Step-level settings always take precedence over workflow-level settings

# num_history_runs=5 in workflow or step to limit context bloat

# see StepInput functions in docs for all the helper functions for custom function code
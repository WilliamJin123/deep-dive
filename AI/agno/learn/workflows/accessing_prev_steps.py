


from agno.workflow.types import StepInput, StepOutput
from agno.workflow.workflow import Workflow


def create_comprehensive_report(step_input: StepInput) -> StepOutput:
    """
    Custom function that creates a report using data from multiple previous steps.
    This function has access to ALL previous step outputs and the original workflow message.
    """

    # Access original workflow input
    original_topic = step_input.workflow_message or ""

    # Access specific step outputs by name
    hackernews_data = step_input.get_step_content("research_hackernews") or ""
    web_data = step_input.get_step_content("research_web") or ""

    # Or access ALL previous content
    all_research = step_input.get_all_previous_content()

    # Create a comprehensive report combining all sources
    report = f"""
        # Comprehensive Research Report: {original_topic}

        ## Executive Summary
        Based on research from HackerNews and web sources, here's a comprehensive analysis of {original_topic}.

        ## HackerNews Insights
        {hackernews_data[:500]}...

        ## Web Research Findings  
        {web_data[:500]}...
    """

    return StepOutput(
        step_name="comprehensive_report", 
        content=report.strip(), 
        success=True
    )

# Use in workflow
workflow = Workflow(
    name="Enhanced Research Workflow",
    steps=[
        Step(name="research_hackernews", agent=hackernews_agent),
        Step(name="research_web", agent=web_agent),
        Step(name="comprehensive_report", executor=create_comprehensive_report),  # Accesses both previous steps
        Step(name="final_reasoning", agent=reasoning_agent),
    ],
)

# In case of Parallel step, when you do step_input.get_step_content("parallel_step_name"), it will return a dict with each key as individual_step_name for all the outputs from the steps defined in parallel. Example:

# parallel_step_output = step_input.get_step_content("parallel_step_name")
# parallel_step_output will be a dict with each key as individual_step_name for all the outputs from the steps defined in parallel.

# {
#     "individual_step_name_1": "output_from_individual_step_1",
#     "individual_step_name_2": "output_from_individual_step_2",
# }
from typing import AsyncIterator, Union
from agno.agent import Agent
from agno.db.in_memory import InMemoryDb
from agno.models.cerebras import Cerebras
from agno.workflow.step import Step, StepInput, StepOutput
from agno.run.workflow import BaseWorkflowRunOutputEvent

content_planner = Agent(
    name="Content Planner",
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    # model=OpenAIChat(id="gpt-4o"),
    instructions=[
        "Plan a content schedule over 4 weeks for the provided topic and research content",
        "Ensure that I have posts for 3 posts per week",
    ],
    db=InMemoryDb(),
)

async def custom_content_planning_function(
    step_input: StepInput,
) -> AsyncIterator[Union[BaseWorkflowRunOutputEvent, StepOutput]]:
    """
    Custom function that does intelligent content planning with context awareness.

    Note: This function calls content_planner.arun() internally, and all events
    from that agent call will automatically get workflow context injected by
    the workflow execution system - no manual intervention required!
    """
    message = step_input.input
    previous_step_content = step_input.previous_step_content

    # Create intelligent planning prompt
    planning_prompt = f"""
        STRATEGIC CONTENT PLANNING REQUEST:

        Core Topic: {message}

        Research Results: {previous_step_content[:500] if previous_step_content else "No research results"}

        Planning Requirements:
        1. Create a comprehensive content strategy based on the research
        2. Leverage the research findings effectively
        3. Identify content formats and channels
        4. Provide timeline and priority recommendations
        5. Include engagement and distribution strategies

        Please create a detailed, actionable content plan.
    """

    try:
        response_iterator = content_planner.arun(
            planning_prompt, stream=True, stream_events=True
        )
        async for event in response_iterator:
            yield event

        response = content_planner.get_last_run_output()

        enhanced_content = f"""
            ## Strategic Content Plan

            **Planning Topic:** {message}

            **Research Integration:** {"✓ Research-based" if previous_step_content else "✗ No research foundation"}

            **Content Strategy:**
            {response.content}

            **Custom Planning Enhancements:**
            - Research Integration: {"High" if previous_step_content else "Baseline"}
            - Strategic Alignment: Optimized for multi-channel distribution
            - Execution Ready: Detailed action items included
        """.strip()

        yield StepOutput(content=enhanced_content)

    except Exception as e:
        yield StepOutput(
            content=f"Custom content planning failed: {str(e)}",
            success=False,
        )
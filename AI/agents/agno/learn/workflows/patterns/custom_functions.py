

content_planning_step = Step(
    name="Content Planning Step",
    executor=custom_content_planning_function,
)

def custom_content_planning_function(step_input: StepInput) -> StepOutput:
    """
    Custom function that does intelligent content planning with context awareness
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
        response = content_planner.run(planning_prompt)

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

        return StepOutput(content=enhanced_content)

    except Exception as e:
        return StepOutput(
            content=f"Custom content planning failed: {str(e)}",
            success=False,
        )
    
def custom_content_planning_function(step_input: StepInput) -> StepOutput:
    # 1. Custom preprocessing
    # 2. Call agents/teams as needed
    # 3. Custom postprocessing
    return StepOutput(content=enhanced_content)


#I like this pattern, keeps everything in Steps
class CustomExecutor:
    def __call__(self, step_input: StepInput) -> StepOutput:
        # 1. Custom preprocessing
        # 2. Call agents/teams as needed
        # 3. Custom postprocessing
        return StepOutput(content=enhanced_content)

content_planning_step = Step(
    name="Content Planning Step",
    executor=CustomExecutor(),
)

#ex: custom logic with caching and retries

class CustomExecutor:
    def __init__(self, max_retries: int = 3, use_cache: bool = True):
        # Configuration passed during instantiation
        self.max_retries = max_retries
        self.use_cache = use_cache
        self.call_count = 0  # Stateful tracking

    def __call__(self, step_input: StepInput) -> StepOutput:
        self.call_count += 1

        # Access instance configuration and state
        if self.use_cache and self.call_count > 1:
            return StepOutput(content="Using cached result")

        # Your custom logic with access to self.max_retries, etc.
        return StepOutput(content=enhanced_content)

# Instantiate with specific configuration
content_planning_step = Step(
    name="Content Planning Step",
    executor=CustomExecutor(max_retries=5, use_cache=False),
)

# supports async

class CustomExecutor:
    async def __call__(self, step_input: StepInput) -> StepOutput:
        # 1. Custom preprocessing
        # 2. Call agents/teams as needed
        # 3. Custom postprocessing
        return StepOutput(content=enhanced_content)

content_planning_step = Step(
    name="Content Planning Step",
    executor=CustomExecutor(),
)

from agno.agent import Agent
from agno.models.cerebras import Cerebras
from agno.exceptions import CheckTrigger, OutputCheckError
from agno.run.agent import RunOutput

# Simple function we will use as a post-hook
def validate_output_length(
    run_output: RunOutput,
) -> None:
    """Post-hook to validate output length."""
    max_length = 1000
    if len(run_output.content) > max_length:
        raise OutputCheckError(
            f"Output too long. Max {max_length} characters allowed",
            check_trigger=CheckTrigger.OUTPUT_NOT_ALLOWED,
        )

agent = Agent(
    name="My Agent",
    # model=OpenAIChat(id="gpt-5-mini"),
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    
    # Provide the post-hook to the Agent using the post_hooks parameter
    post_hooks=[validate_output_length],
)

agent.run("Generate me 1000 characters.")
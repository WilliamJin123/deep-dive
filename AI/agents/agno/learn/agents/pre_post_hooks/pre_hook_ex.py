from agno.agent import Agent
from agno.models.cohere import Cohere
from agno.exceptions import CheckTrigger, InputCheckError
from agno.run.agent import RunInput

# Simple function we will use as a pre-hook
def validate_input_length(
    run_input: RunInput,
    # agent: Agent,
    # etc. Automatic Injection
) -> None:
    """Pre-hook to validate input length."""
    max_length = 1000
    if len(run_input.input_content) > max_length:
        raise InputCheckError(
            f"Input too long. Max {max_length} characters allowed",
            check_trigger=CheckTrigger.INPUT_NOT_ALLOWED,
        )

agent = Agent(
    name="My Agent",
    # model=OpenAIChat(id="gpt-4o"),
    model=Cohere("command-a-03-2025"),
    # Provide the pre-hook to the Agent using the pre_hooks parameter
    pre_hooks=[validate_input_length],
)

agent.run(input="Hello World" + "!" * 1000)

#throws agno.exceptions.InputCheckError: Input too long. Max 1000 characters allowed
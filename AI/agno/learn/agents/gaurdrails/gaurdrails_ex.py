from agno.guardrails import PIIDetectionGuardrail
from agno.agent import Agent
from agno.models.cerebras import Cerebras

pii_guardrail = PIIDetectionGuardrail()

agent = Agent(
    name="Privacy-Protected Agent",
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    # model=OpenAIChat(id="gpt-5-mini"),
    pre_hooks=[pii_guardrail],
)

# Custom Gaurdrail

import re

from agno.exceptions import CheckTrigger, InputCheckError
from agno.guardrails import BaseGuardrail
from agno.run.agent import RunInput

class URLGuardrail(BaseGuardrail):
    """Guardrail to identify and stop inputs containing URLs."""

    def check(self, run_input: RunInput) -> None:
        """Raise InputCheckError if the input contains any URLs."""
        if isinstance(run_input.input_content, str):
            # Basic URL pattern
            url_pattern = r'https?://[^\s]+|www\.[^\s]+|[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}[^\s]*'
            if re.search(url_pattern, run_input.input_content):
                raise InputCheckError(
                    "The input seems to contain URLs, which are not allowed.",
                    check_trigger=CheckTrigger.INPUT_NOT_ALLOWED,
                )

    async def async_check(self, run_input: RunInput) -> None:
        """Raise InputCheckError if the input contains any URLs."""
        if isinstance(run_input.input_content, str):
            # Basic URL pattern
            url_pattern = r'https?://[^\s]+|www\.[^\s]+|[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}[^\s]*'
            if re.search(url_pattern, run_input.input_content):
                raise InputCheckError(
                    "The input seems to contain URLs, which are not allowed.",
                    check_trigger=CheckTrigger.INPUT_NOT_ALLOWED,
                )


# Agent using our URLGuardrail
agent = Agent(
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    name="URL-Protected Agent",
    # Provide the Guardrails to be used with the pre_hooks parameter
    pre_hooks=[URLGuardrail()],
)

# This will raise an InputCheckError
agent.run("Can you check what's in https://fake.com?")
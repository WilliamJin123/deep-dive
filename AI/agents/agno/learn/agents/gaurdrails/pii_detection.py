from agno.guardrails import PIIDetectionGuardrail
from agno.agent import Agent
from agno.models.openai import OpenAIChat

agent = Agent(
    name="Privacy-Protected Agent",
    model=OpenAIChat(id="gpt-5-mini"),
    pre_hooks=[PIIDetectionGuardrail()],
)

# The default list of PII fields handled by the guardrail are:
# Social Security Numbers (SSNs)
# Credit Card Numbers
# Email Addresses
# Phone Numbers

# Disable certain checks
guardrail = PIIDetectionGuardrail(
    enable_email_check=False,
)

#extend with custom patterns
guardrail = PIIDetectionGuardrail(
    custom_patterns={
        "bank_account_number": r"\b\d{10}\b",
    }
)

#mask pii instead of throwing error
guardrail = PIIDetectionGuardrail(
    mask_pii=True,
)

# joe@example.com --> **************
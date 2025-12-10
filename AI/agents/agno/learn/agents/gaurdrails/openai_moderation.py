#fuck moderation
from agno.guardrails import OpenAIModerationGuardrail
from agno.agent import Agent
from agno.models.openai import OpenAIChat

openai_moderation_guardrail = OpenAIModerationGuardrail()

agent = Agent(
    name="OpenAI Moderation Guardrail Agent",
    model=OpenAIChat(id="gpt-5-mini"),
    pre_hooks=[openai_moderation_guardrail],
)
openai_moderation_guardrail = OpenAIModerationGuardrail(
    moderation_model="omni-moderation-latest",
)
openai_moderation_guardrail = OpenAIModerationGuardrail(
    raise_for_categories=["violence", "hate"],
)
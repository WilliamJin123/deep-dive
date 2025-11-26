from agno.guardrails import PromptInjectionGuardrail
from agno.agent import Agent
from agno.models.openai import OpenAIChat

prompt_injection_guardrail = PromptInjectionGuardrail()

agent = Agent(
    name="Prompt Injection Guardrail Agent",
    model=OpenAIChat(id="gpt-5-mini"),
    pre_hooks=[prompt_injection_guardrail],
)

# The default list of injection patterns handled by the guardrail are:
# “ignore previous instructions”
# “ignore your instructions”
# “you are now a”
# “forget everything above”
# “developer mode”
# “override safety”
# “disregard guidelines”
# “system prompt”
# “jailbreak”
# “act as if”
# “pretend you are”
# “roleplay as”
# “simulate being”
# “bypass restrictions”
# “ignore safeguards”
# “admin override”
# “root access”

#override default list if necessary
prompt_injection_guardrail = PromptInjectionGuardrail(
    injection_patterns=["ignore previous instructions", "ignore your instructions"],
)

prompt_injection_guardrail.injection_patterns.append("Sigma sigma on the wall")
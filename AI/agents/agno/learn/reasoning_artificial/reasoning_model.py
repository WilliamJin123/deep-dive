from agno.agent import Agent
from agno.models.cerebras import Cerebras
from agno.models.openrouter import OpenRouter


TASK_1 = "Plan a high-level architecture for a real-time collaborative code editor. Focus on conflict resolution strategies."


agent = Agent(
    model=Cerebras(id="llama-3.3-70b"), 
    reasoning_model=OpenRouter(
        id="tngtech/deepseek-r1t-chimera:free", 
        temperature=0.6, 
        max_tokens=2048,
        top_p=0.95
    ),
    markdown=True,
    debug_mode=True,
    reasoning_min_steps=3,
)

print("--- RUN 1: Using Reasoning Model ---")
# agent.print_response(TASK_1, show_full_reasoning=True, show_reasoning= True, stream=True)

input("\nPress Enter to switch to a Reasoning Agent approach...")


reasoning_agent = Agent(
    model=OpenRouter(
        id="allenai/olmo-3-32b-think:free",
        temperature=0.4,
    ),
    reasoning=True,
    reasoning_min_steps=5,
)

# 4. Update the main agent to use the Reasoning Agent instead
agent.reasoning_model = None
agent.reasoning_agent = reasoning_agent

TASK_2 = "Evaluate the environmental impact of switching a global fleet of 100,000 trucks from Diesel to Hydrogen vs Electric."

print("\n--- RUN 2: Using Reasoning Agent ---")
agent.print_response(TASK_2, show_full_reasoning=True, show_reasoning= True, stream=True)
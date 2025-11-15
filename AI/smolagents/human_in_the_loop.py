from cerebras_agent import makeCerebrasAgent
from smolagents import CodeAgent, DuckDuckGoSearchTool, PlanningStep



agent = CodeAgent(
    model=makeCerebrasAgent(),
    tools=[DuckDuckGoSearchTool()],
    planning_interval=5,  # Plan every 5 steps
    step_callbacks={PlanningStep: interrupt_after_plan},
    max_steps=10,
    verbosity_level=1
)

# First run (may be interrupted)
agent.run(task, reset=True)

# Resume with preserved memory
agent.run(task, reset=False)
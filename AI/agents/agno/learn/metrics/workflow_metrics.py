from agno.agent import Agent
from agno.models.cerebras import Cerebras
from agno.db.sqlite import SqliteDb
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
from agno.workflow import Step, Workflow
from rich.pretty import pprint

# Define agents
hackernews_agent = Agent(
    name="Hackernews Agent",
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    # model=OpenAIChat(id="gpt-4o-mini"),
    tools=[HackerNewsTools()],
    role="Extract key insights from Hackernews posts",
)

web_agent = Agent(
    name="Web Agent",
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    # model=OpenAIChat(id="gpt-4o-mini"),
    tools=[DuckDuckGoTools()],
    role="Search the web for latest trends",
)

# Define research team
research_team = Team(
    name="Research Team",
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    members=[hackernews_agent, web_agent],
    instructions="Research tech topics from Hackernews and the web",
)

content_planner = Agent(
    name="Content Planner",
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    # model=OpenAIChat(id="gpt-4o"),
    instructions="Plan a content schedule based on research",
)

# Create workflow
workflow = Workflow(
    name="Content Creation Workflow",
    db=SqliteDb(db_file="tmp/workflow.db"),
    steps=[
        Step(name="Research Step", team=research_team),
        Step(name="Content Planning Step", agent=content_planner),
    ],
)

# Run workflow
response = workflow.run(input="AI trends in 2024")

# Print workflow-level metrics
print("Workflow Metrics")
if response.metrics:
    pprint(response.metrics.to_dict())

# Print workflow duration
if response.metrics and response.metrics.duration:
    print(f"\nTotal execution time: {response.metrics.duration:.2f} seconds")

# Print step-level metrics
print("Step Metrics")
if response.metrics:
    for step_name, step_metrics in response.metrics.steps.items():
        print(f"\nStep: {step_name}")
        print(f"Executor: {step_metrics.executor_name} ({step_metrics.executor_type})")
        if step_metrics.metrics:
            print(f"Duration: {step_metrics.metrics.duration:.2f}s")
            print(f"Tokens: {step_metrics.metrics.total_tokens}")

# Print session metrics
print("Session Metrics")
pprint(workflow.get_session_metrics().to_dict())
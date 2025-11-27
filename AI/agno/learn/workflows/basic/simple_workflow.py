from agno.agent import Agent
from agno.workflow import Workflow
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.models.cerebras import Cerebras


# Define agents with specific roles
researcher = Agent(
    name="Researcher",
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    instructions="Find relevant information about the topic",
    tools=[DuckDuckGoTools()]
)

writer = Agent(
    name="Writer",
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    instructions="Write a clear, engaging article based on the research"
)

# Chain them together in a workflow
content_workflow = Workflow(
    name="Content Creation",
    steps=[researcher, writer],
)

# Run the workflow
content_workflow.print_response("Write an article about climate change solutions", stream=True)
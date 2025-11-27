from agno.agent import Agent    
from agno.models.openai import OpenAIChat
from agno.tools.workflow import WorkflowTools

# Create your workflows...

workflow_tools = WorkflowTools(
    workflow=blog_post_workflow,
)

agent = Agent(
    model=OpenAIChat(id="gpt-5-mini"),
    tools=[workflow_tools],
)

agent.print_response("Create a blog post on the topic: AI trends in 2024", stream=True)
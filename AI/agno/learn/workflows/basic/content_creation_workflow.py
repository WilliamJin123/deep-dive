from agno.agent import Agent
from agno.models.cerebras import Cerebras
from agno.db.sqlite import SqliteDb
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools
from agno.workflow import Step, Workflow
from agno.run.workflow import WorkflowRunOutput
from agno.utils.pprint import pprint_run_response

# Define agents
hackernews_agent = Agent(
    name="Hackernews Agent",
    # model=OpenAIChat(id="gpt-5-mini"),
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    tools=[HackerNewsTools()],
    role="Extract key insights and content from Hackernews posts",
)
web_agent = Agent(
    name="Web Agent",
    # model=OpenAIChat(id="gpt-5-mini"),
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    tools=[DuckDuckGoTools()],
    role="Search the web for the latest news and trends",
)

# Define research team for complex analysis
research_team = Team(
    name="Research Team",
    members=[hackernews_agent, web_agent],
    instructions="Research tech topics from Hackernews and the web",
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    show_members_responses=True
)

content_planner = Agent(
    name="Content Planner",
    # model=OpenAIChat(id="gpt-5-mini"),
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    instructions=[
        "Plan a content schedule over 4 weeks for the provided topic and research content",
        "Ensure that I have posts for 3 posts per week",
    ],
)

content_creation_workflow = Workflow(
    name="Content Creation Workflow",
    description="Automated content creation from blog posts to social media",
    db=SqliteDb(db_file="tmp/workflow.db"),
    steps=[research_team, content_planner],
    
)

# Create and use workflow
if __name__ == "__main__":
    response: WorkflowRunOutput = content_creation_workflow.run(
        input="AI trends in 2025",
        markdown=True,
        stream=True
    )
    pprint_run_response(response, markdown=True)
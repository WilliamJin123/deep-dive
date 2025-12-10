# Per-message: Each message (assistant, tool, etc.) has its own metrics.
# Per-member run: Each team member run has its own metrics. You can make member runs available on the TeamRunOutput by setting store_member_responses=True,
# Team-level: The TeamRunOutput aggregates metrics across all team leader and team member messages.
# Session-level: Aggregated metrics across all runs in the session, for both the team leader and all team members.

from typing import Iterator

from agno.agent import Agent, RunOutput
from agno.models.openai import OpenAIChat
from agno.team.team import Team
from agno.models.cerebras import Cerebras 
from agno.team import TeamRunOutput
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.utils.pprint import pprint_run_response
from rich.pretty import pprint
from agno.db.sqlite import SqliteDb

db = SqliteDb(db_file="tmp/team_session.db")
# Create team members
web_searcher = Agent(
    name="Stock Searcher",
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    # model=OpenAIChat(id="gpt-5-mini"),
    role="Searches the web for information.",
    tools=[DuckDuckGoTools()],
)

# Create the team
team = Team(
    name="Web Research Team",
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    # model=OpenAIChat(id="gpt-5-mini"),
    members=[web_searcher],
    markdown=True,
    store_member_responses=True,
    session_id="session_123",
    db=db
)

# Run the team
run_response: TeamRunOutput = team.run(
    "What is going on in the world?"
)
pprint_run_response(run_response, markdown=True)

# Print team leader message metrics
print("---" * 5, "Team Leader Message Metrics", "---" * 5)
if run_response.messages:
    for message in run_response.messages:
        if message.role == "assistant":
            if message.content:
                print(f"Message: {message.content}")
            elif message.tool_calls:
                print(f"Tool calls: {message.tool_calls}")
            print("---" * 5, "Metrics", "---" * 5)
            pprint(message.metrics)
            print("---" * 20)

# Print aggregated team leader metrics
print("---" * 5, "Aggregated Metrics of Team", "---" * 5)
pprint(run_response.metrics)

# Print team leader session metrics
print("---" * 5, "Session Metrics", "---" * 5)
pprint(team.get_session_metrics().to_dict())

# Print team member message metrics
print("---" * 5, "Team Member Message Metrics", "---" * 5)
if run_response.member_responses:
    for member_response in run_response.member_responses:
        if member_response.messages:
            for message in member_response.messages:
                if message.role == "assistant":
                    if message.content:
                        print(f"Member Message: {message.content}")
                    elif message.tool_calls:
                        print(f"Member Tool calls: {message.tool_calls}")
                    print("---" * 5, "Member Metrics", "---" * 5)
                    pprint(message.metrics)
                    print("---" * 20)
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.db.sqlite import SqliteDb
from rich.pretty import pprint

agent = Agent(
    model=Gemini(id="gemini-2.5-flash"),
    tools=[DuckDuckGoTools()],
    db=SqliteDb(db_file="tmp/agents.db"),
    markdown=True,
)

run_response = agent.run(
    "What is current news in the world?",
    
)

# Print metrics per message
if run_response.messages:
    for message in run_response.messages:
        if message.role == "assistant":
            if message.content:
                print(f"Message: {message.content}")
            elif message.tool_calls:
                print(f"Tool calls: {message.tool_calls}")
            print("---" * 5, "Metrics", "---" * 5)
            pprint(message.metrics.to_dict())
            print("---" * 20)

# Print the aggregated metrics for the whole run
print("---" * 5, "Run Metrics", "---" * 5)
pprint(run_response.metrics.to_dict())
# Print the aggregated metrics for the whole session
print("---" * 5, "Session Metrics", "---" * 5)
pprint(agent.get_session_metrics().to_dict())
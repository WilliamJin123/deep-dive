# message level, run level, session level

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
    "What is current news in the world?"
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

# input_tokens: The number of tokens sent to the model.
# output_tokens: The number of tokens received from the model.
# total_tokens: The sum of input_tokens and output_tokens.
# audio_input_tokens: The number of tokens sent to the model for audio input.
# audio_output_tokens: The numbe    r of tokens received from the model for audio output.
# audio_total_tokens: The sum of audio_input_tokens and audio_output_tokens.
# cache_read_tokens: The number of tokens read from the cache.
# cache_write_tokens: The number of tokens written to the cache.
# reasoning_tokens: The number of tokens used for reasoning.
# duration: The duration of the run in seconds.
# time_to_first_token: The time taken until the first token was generated.
# provider_metrics: Any provider-specific metrics.


from agno.agent import Agent
from agno.db.postgres import PostgresDb
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.utils import pprint

agent = Agent(
    model=OpenAIChat(id="gpt-5-mini"),
    tools=[DuckDuckGoTools(stock_price=True)],
    markdown=True,
    session_id="test-session-metrics",
    db=PostgresDb(db_url="postgresql+psycopg://ai:ai@localhost:5532/ai"),
)

# Get the run response directly from the non-streaming call
run_response = agent.run("What is the stock price of NVDA")
print("Tool execution completed successfully!")

# Print metrics per message
if run_response and run_response.messages:
    for message in run_response.messages:
        if message.role == "assistant":
            if message.content:
                print(
                    f"Message: {message.content[:100]}..."
                )  # Truncate for readability
            elif message.tool_calls:
                print(f"Tool calls: {len(message.tool_calls)} tool call(s)")
            print("---" * 5, "Message Metrics", "---" * 5)
            if message.metrics:
                pprint(message.metrics)
            else:
                print("No metrics available for this message")
            print("---" * 20)

# Print the run metrics
print("---" * 5, "Run Metrics", "---" * 5)
if run_response and run_response.metrics:
    pprint(run_response.metrics)
else:
    print("No run metrics available")

# Print the session metrics
print("---" * 5, "Session Metrics", "---" * 5)
try:
    session_metrics = agent.get_session_metrics()
    if session_metrics:
        pprint(session_metrics)
    else:
        print("No session metrics available")
except Exception as e:
    print(f"Error getting session metrics: {e}")
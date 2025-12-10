from agno.agent import Agent
from agno.models.openai.chat import OpenAIChat
from agno.models.cerebras import Cerebras
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    # model=OpenAIChat(id="gpt-5-mini"),
    tools=[YFinanceTools(cache_results=True)],
    tool_call_limit=1, # The Agent will not perform more than one tool call.
)

# The first tool call will be performed. The second one will fail gracefully.
agent.print_response(
    "Find me the current price of TSLA, then after that find me the latest news about Tesla.",
    stream=True,
)
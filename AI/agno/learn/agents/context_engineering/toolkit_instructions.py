from agno.agent import Agent
from agno.tools.slack import SlackTools

slack_tools = SlackTools(
    instructions=["Use `send_message` to send a message to the user.  If the user specifies a thread, use `send_message_thread` to send a message to the thread."],
    add_instructions=True,
)
agent = Agent(
    tools=[slack_tools],
)
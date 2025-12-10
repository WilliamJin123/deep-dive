from agno.agent import Agent
from agno.models.cerebras import Cerebras

from agno.db.in_memory import InMemoryDb

agent = Agent(model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    db=InMemoryDb(),
    # read_chat_history=True,  this one works less reliably I find, needs the LLM to situationally call the tool to read chat history
    add_history_to_context=True,
    num_history_messages=10
 )



agent.print_response("Hi, I'm John. Nice to meet you!")

# ━ Tool Calls ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                                                                                                  ┃
# ┃ • get_chat_history(num_chats=1)      
agent.print_response("I am 6 foot 2 inches tall and 18 years old! What's my name?", add_history_to_context=True)

# ━ Tool Calls ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                                                                                                                  ┃
# ┃ • get_chat_history(num_chats=1)    
agent.print_response("What is my name?", ) # add_history_to_context=True, read_chat_history also enables the agent to know this info
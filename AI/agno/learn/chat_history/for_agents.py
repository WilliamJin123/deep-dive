from agno.agent import Agent
Agent(
    read_chat_history=False, # get_chat_history() tool to your agent allowing it to read any message in the entire chat history.
    read_tool_call_history=False, # get_tool_call_history() tool to your agent allowing it to read tool calls in reverse chronological order
    search_session_history=False, # allow seraching through previous sessions in db 
    num_history_sessions= 2 # - 3 # number of past sessions to include in session search
    # add histiory to context, num history runs / msgs, etc. all the same
)
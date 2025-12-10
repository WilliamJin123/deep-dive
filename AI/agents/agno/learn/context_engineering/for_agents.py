from agno.models.cerebras import Cerebras
from agno.agent import Agent

prompt_addons = Agent(
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    description="You are a famous short story writer asked to write for a magazine", 
    instructions=["Always write 2 sentence stories."], 
    markdown=True,
    debug_mode=True,

    additional_context="My name is William and I am 18 yo",
    expected_output="500 tokens worth of text."



    # add_name_to_context=True # agent name in sys prompt

    # system_message="" # override entire sys messagw
    # build_context=True #default, disable to not build context 
)

prompt_addons.print_response("Tell me a horror story.", stream=True)


agent = Agent(
    name="Helpful Assistant",
    role="Assistant", # your role
    id="assistant", # internal id
    description="You are a helpful assistant",
    instructions=["Help the user with their question"], # <instructions>
    additional_context="""
    Here is an example of how to answer the user's question: 
        Request: What is the capital of France?
        Response: The capital of France is Paris.
    """,
     # no tags

    expected_output="You should format your response with `Response: <response>`", # <expected_output>
    markdown=True,
    add_datetime_to_context=True, # <additional_information>
    add_location_to_context=True, # <additional_information>
    add_name_to_context=True, # <additional_information>
    add_session_summary_to_context=True, # <summary_of_previous_interactions>
    add_memories_to_context=True, # <memories_from_previous_interactions>
    add_session_state_to_context=True, # <session_state> 
)


from agno.agent import Agent
from agno.tools.slack import SlackTools

slack_tools = SlackTools(
    instructions=["Use `send_message` to send a message to the user.  If the user specifies a thread, use `send_message_thread` to send a message to the thread."],
    add_instructions=True,
    #after <additional_information>

)
agent = Agent(
    tools=[slack_tools],
)

# enable_agentic_memory = True
"""<updating_user_memories>
- You have access to the `update_user_memory` tool that you can use to add new memories, update existing memories, delete memories, or clear all memories.
- If the user's message includes information that should be captured as a memory, use the `update_user_memory` tool to update your memory database.
- Memories should include details that could personalize ongoing interactions with the user.
- Use this tool to add new memories or update existing memories that you identify in the conversation.
- Use this tool if the user asks to update their memory, delete a memory, or clear all memories.
- If you use the `update_user_memory` tool, remember to pass on the response to the user.
</updating_user_memories>
"""

# enable_agentic_knowledge_filters = True 
"""
The knowledge base contains documents with these metadata filters: [filter1, filter2, filter3].
Always use filters when the user query indicates specific metadata.

Examples:
1. If the user asks about a specific person like "Jordan Mitchell", you MUST use the search_knowledge_base tool with the filters parameter set to {{'<valid key like user_id>': '<valid value based on the user query>'}}.
2. If the user asks about a specific document type like "contracts", you MUST use the search_knowledge_base tool with the filters parameter set to {{'document_type': 'contract'}}.
4. If the user asks about a specific location like "documents from New York", you MUST use the search_knowledge_base tool with the filters parameter set to {{'<valid key like location>': 'New York'}}.

General Guidelines:
- Always analyze the user query to identify relevant metadata.
- Use the most specific filter(s) possible to narrow down results.
- If multiple filters are relevant, combine them in the filters parameter (e.g., {{'name': 'Jordan Mitchell', 'document_type': 'contract'}}).
- Ensure the filter keys match the valid metadata filters: [filter1, filter2, filter3].

You can use the search_knowledge_base tool to search the knowledge base and get the most relevant documents. Make sure to pass the filters as [Dict[str: Any]] to the tool. FOLLOW THIS STRUCTURE STRICTLY.
"""

from agno.agent import Agent
agent = Agent(add_knowledge_to_context=True, add_dependencies_to_context=True)
agent.print_response("What is the capital of France?", dependencies={"name": "John Doe"})

"""
What is the capital of France?

Use the following references from the knowledge base if it helps:
<references>
- Reference 1
- Reference 2
</references>

<additional context>
{"name": "John Doe"}
</additional context>
"""

# few shot with additional_input = few_shot_examples (array of json user assistant message pairs)


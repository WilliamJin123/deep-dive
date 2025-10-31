from intro_to_langChain import cerebrasInitModel
from langsmith_stuff import langSmithInit

# Modern imps of:
#     - ConversationBufferMemory
#     - ConversationBufferWindowMemory
#     - ConversationSummaryMemory
#     - ConversationSummaryBufferMemory
# langSmithInit()

llm = cerebrasInitModel()

from langchain.memory import ConversationBufferMemory # deprecated

memory = ConversationBufferMemory(return_messages=True)

memory.save_context(
    {"input": "Hi, my name is James"},  # user message
    {"output": "Hey James, what's up? I'm an AI model called Zeta."}  # AI response
)
memory.save_context(
    {"input": "I'm researching the different types of conversational memory."},  # user message
    {"output": "That's interesting, what are some examples?"}  # AI response
)
memory.save_context(
    {"input": "I've been looking at ConversationBufferMemory and ConversationBufferWindowMemory."},  # user message
    {"output": "That's interesting, what's the difference?"}  # AI response
)
memory.save_context(
    {"input": "Buffer memory just stores the entire conversation, right?"},  # user message
    {"output": "That makes sense, what about ConversationBufferWindowMemory?"}  # AI response
)
memory.save_context(
    {"input": "Buffer window memory stores the last k messages, dropping the rest."},  # user message
    {"output": "Very cool!"}  # AI response
)

memory.load_memory_variables({}) #any variables to load, none for this case

memory = ConversationBufferMemory(return_messages=True)
#alternative load
memory.chat_memory.add_user_message("Hi, my name is James")
memory.chat_memory.add_ai_message("Hey James, what's up? I'm an AI model called Zeta.")
memory.chat_memory.add_user_message("I'm researching the different types of conversational memory.")
memory.chat_memory.add_ai_message("That's interesting, what are some examples?")
memory.chat_memory.add_user_message("I've been looking at ConversationBufferMemory and ConversationBufferWindowMemory.")
memory.chat_memory.add_ai_message("That's interesting, what's the difference?")
memory.chat_memory.add_user_message("Buffer memory just stores the entire conversation, right?")
memory.chat_memory.add_ai_message("That makes sense, what about ConversationBufferWindowMemory?")
memory.chat_memory.add_user_message("Buffer window memory stores the last k messages, dropping the rest.")
memory.chat_memory.add_ai_message("Very cool!")

memory.load_memory_variables({})

from langchain.chains import ConversationChain

chain = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

print(chain.invoke({"input": "what is my name again?"}))

#new way to do it

from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    ChatPromptTemplate
)

system_prompt = "You are a helpful assistant called Zeta."

prompt_template = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(system_prompt),
    MessagesPlaceholder(variable_name="history"),
    HumanMessagePromptTemplate.from_template("{query}")
])

pipeline = prompt_template | llm

from langchain_core.chat_history import InMemoryChatMessageHistory

chat_map = {}
def get_chat_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in chat_map:
        # if session ID doesn't exist, create a new chat history
        chat_map[session_id] = InMemoryChatMessageHistory()
    return chat_map[session_id]


from langchain_core.runnables.history import RunnableWithMessageHistory

pipeline_with_history = RunnableWithMessageHistory(
    pipeline,
    get_session_history=get_chat_history,
    input_messages_key="query",
    history_messages_key="history"
)

pipeline_with_history.invoke(
    {"query": "Hi, my name is James"},
    config={"session_id": "id_123"}
)

pipeline_with_history.invoke(
    {"query": "What is my name again?"},
    config={"session_id": "id_123"}
)

# Deprecated ConversationBufferWindowMemory

from langchain.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(k=4, return_messages=True)

memory.chat_memory.add_user_message("Hi, my name is James")
memory.chat_memory.add_ai_message("Hey James, what's up? I'm an AI model called Zeta.")
memory.chat_memory.add_user_message("I'm researching the different types of conversational memory.")
memory.chat_memory.add_ai_message("That's interesting, what are some examples?")
memory.chat_memory.add_user_message("I've been looking at ConversationBufferMemory and ConversationBufferWindowMemory.")
memory.chat_memory.add_ai_message("That's interesting, what's the difference?")
memory.chat_memory.add_user_message("Buffer memory just stores the entire conversation, right?")
memory.chat_memory.add_ai_message("That makes sense, what about ConversationBufferWindowMemory?")
memory.chat_memory.add_user_message("Buffer window memory stores the last k messages, dropping the rest.")
memory.chat_memory.add_ai_message("Very cool!")

memory.load_memory_variables({})

chain = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

chain.invoke({"input": "what is my name again?"})

#modern reimp

from pydantic import BaseModel, Field
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import BaseMessage



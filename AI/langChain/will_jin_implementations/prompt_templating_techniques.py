from langsmith_stuff import langSmithInit 
from langchain.prompts import ChatPromptTemplate
# langSmithInit() # if using langSmith observe features, not using them for now to save my monthly limits lol
from intro_to_langChain import cerebrasInit
from langchain_cerebras import ChatCerebras

prompt = """
Answer the user's query based on the context below.
If you cannot answer the question using the
provided information answer with "I don't know".

Context: {context}
"""

llama_70b = cerebrasInit()

# passing the template to the LangChain model
prompt_template = ChatPromptTemplate.from_messages([
    ("system", prompt),
    ("user", "{query}"),
])

print(prompt_template.input_variables) # ['context', 'query']
print(prompt_template.messages) 
# [SystemMessagePromptTemplate(prompt=PromptTemplate(input_variables=['context'], input_types={}, partial_variables={}, template='\nAnswer the user\'s query based on the context below.\nIf you cannot answer the question using the\nprovided information answer with "I don\'t know".\n\nContext: {context}\n'), additional_kwargs={}), HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['query'], input_types={}, partial_variables={}, template='{query}'), additional_kwargs={})] 



from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)

prompt_template = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(prompt),
    HumanMessagePromptTemplate.from_template("{query}"),
])

print(prompt_template.messages) 
#[SystemMessagePromptTemplate(prompt=PromptTemplate(input_variables=['context'], input_types={}, partial_variables={}, template='\nAnswer the user\'s query based on the context below.\nIf you cannot answer the question using the\nprovided information answer with "I don\'t know".\n\nContext: {context}\n'), additional_kwargs={}), HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['query'], input_types={}, partial_variables={}, template='{query}'), additional_kwargs={})]      

llm = ChatCerebras(temperature=0.0, model=llama_70b)

pipeline = (
    {
        "query": lambda x: x["query"],
        "context": lambda x: x["context"]
    }
    | prompt_template
    | llm
)


context = """Aurelio AI is an AI company developing tooling for AI
engineers. Their focus is on language AI with the team having strong
expertise in building AI agents and a strong background in
information retrieval.

The company is behind several open source frameworks, most notably
Semantic Router and Semantic Chunkers. They also have an AI
Platform providing engineers with tooling to help them build with
AI. Finally, the team also provides development services to other
organizations to help them bring their AI tech to market.

Aurelio AI became LangChain Experts in September 2024 after a long
track record of delivering AI solutions built with the LangChain
ecosystem."""

query = "what does Aurelio AI do?"

pipeline.invoke({"query": query, "context": context}) #invoke the pipeline that has a lambda to pass shit in! makes sense!


#Few shot

example_prompt = ChatPromptTemplate.from_messages([
    ("human", "{input}"),
    ("ai", "{output}"),
])


examples = [
    {"input": "Here is query #1", "output": "Here is the answer #1"},
    {"input": "Here is query #2", "output": "Here is the answer #2"},
    {"input": "Here is query #3", "output": "Here is the answer #3"},
]


from langchain.prompts import FewShotChatMessagePromptTemplate

few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
)
# here is the formatted prompt
print(few_shot_prompt.format())

new_system_prompt = """
Answer the user's query based on the context below.
If you cannot answer the question using the
provided information answer with "I don't know".

Always answer in markdown format. When doing so please
provide headers, short summaries, follow with bullet
points, then conclude.

Context: {context}
"""

prompt_template.messages[0].prompt.template = new_system_prompt

out = pipeline.invoke({"query": query, "context": context}).content
print(out)


from IPython.display import display, Markdown

display(Markdown(out))

examples = [
    {
        "input": "Can you explain gravity?",
        "output": (
            "## Gravity\n\n"
            "Gravity is one of the fundamental forces in the universe.\n\n"
            "### Discovery\n\n"
            "* Gravity was first discovered by Sir Isaac Newton in the late 17th century.\n"
            "* It was said that Newton theorized about gravity after seeing an apple fall from a tree.\n\n"
            "### In General Relativity\n\n"
            "* Gravity is described as the curvature of spacetime.\n"
            "* The more massive an object is, the more it curves spacetime.\n"
            "* This curvature is what causes objects to fall towards each other.\n\n"
            "### Gravitons\n\n"
            "* Gravitons are hypothetical particles that mediate the force of gravity.\n"
            "* They have not yet been detected.\n\n"
            "**To conclude**, Gravity is a fascinating topic and has been studied extensively since the time of Newton.\n\n"
        )
    },
    {
        "input": "What is the capital of France?",
        "output": (
            "## France\n\n"
            "The capital of France is Paris.\n\n"
            "### Origins\n\n"
            "* The name Paris comes from the Latin word \"Parisini\" which referred to a Celtic people living in the area.\n"
            "* The Romans named the city Lutetia, which means \"the place where the river turns\".\n"
            "* The city was renamed Paris in the 3rd century BC by the Celtic-speaking Parisii tribe.\n\n"
            "**To conclude**, Paris is highly regarded as one of the most beautiful cities in the world and is one of the world's greatest cultural and economic centres.\n\n"
        )
    }
]

few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
)

out = few_shot_prompt.format()

display(Markdown(out))

print(few_shot_prompt)

prompt_template = ChatPromptTemplate.from_messages([
    ("system", new_system_prompt),
    few_shot_prompt,
    ("user", "{query}"),
])

pipeline = prompt_template | llm
out = pipeline.invoke({"query": query, "context": context}).content
display(Markdown(out))


# CoT Prompting (note: many modern LLMs do CoT by default)

no_cot_system_prompt = """
Be a helpful assistant and answer the user's question.

You MUST answer the question directly without any other
text or explanation.
"""



no_cot_prompt_template = ChatPromptTemplate.from_messages([
    ("system", no_cot_system_prompt),
    ("user", "{query}"),
])


query = (
    "How many keystrokes are needed to type the numbers from 1 to 500?"
)

no_cot_pipeline = no_cot_prompt_template | llm
no_cot_result = no_cot_pipeline.invoke({"query": query}).content
print(no_cot_result)

# Define the chain-of-thought prompt template
cot_system_prompt = """
Be a helpful assistant and answer the user's question.

To answer the question, you must:

- List systematically and in precise detail all
  subproblems that need to be solved to answer the
  question.
- Solve each sub problem INDIVIDUALLY and in sequence.
- Finally, use everything you have worked through to
  provide the final answer.
"""

cot_prompt_template = ChatPromptTemplate.from_messages([
    ("system", cot_system_prompt),
    ("user", "{query}"),
])

cot_pipeline = cot_prompt_template | llm

cot_result = cot_pipeline.invoke({"query": query}).content
display(Markdown(cot_result))

system_prompt = """
Be a helpful assistant and answer the user's question.
"""

prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("user", "{query}"),
])

pipeline = prompt_template | llm

result = pipeline.invoke({"query": query}).content
display(Markdown(result))
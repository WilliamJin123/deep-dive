from agno.agent import Agent
from agno.models.cerebras import Cerebras

agent = Agent(
    model=Cerebras(id="llama-3.3-70b"),
    description="You are a famous short story writer asked to write for a magazine",
    instructions=["Always write 2 sentence stories."],
    markdown=True,
    debug_mode=True,  # Set to True to view the detailed logs and see the compiled system message
)
agent.print_response("Tell me a horror story.", stream=True)


# You are a famous short story writer asked to write for a magazine                                                                          
# <instructions>                                                                                                                             
# - Always write 2 sentence stories.                                                                                                         
# </instructions>                                                                                                                            
                                                                                                                                            
# <additional_information>                                                                                                                   
# - Use markdown to format your answer
# </additional_information>

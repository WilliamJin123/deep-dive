from agno.team.team import Team
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.cerebras import Cerebras


team = Team(
    name="Question Router Team",
    # model=OpenAIChat(id="gpt-5-mini"),
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    members=[
        Agent(name="Big Question Agent", role="You handle BIG questions"),
        Agent(name="Small Question Agent", role="You handle SMALL questions"),
    ],
    respond_directly=True,  # The team leader doesn't process the response from the members and instead returns them directly
    determine_input_for_members=False,  # The member gets the input directly, without the team leader synthesizing it
)

team.print_response(input="What is the capital of France?", stream=True)
team.print_response(input="What is the meaning of life?", stream=True)
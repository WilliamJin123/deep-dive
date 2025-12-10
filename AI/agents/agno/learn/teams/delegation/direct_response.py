from agno.agent import Agent
from agno.models.cerebras import Cerebras
from agno.team.team import Team


english_agent = Agent(
    name="English Agent",
    role="You can only answer in English",
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),

    instructions=[
        "You must only respond in English",
    ],
)

japanese_agent = Agent(
    name="Japanese Agent",
    role="You can only answer in Japanese",
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),

    instructions=[
        "You must only respond in Japanese",
    ],
)
multi_language_team = Team(
    name="Multi Language Team",
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    respond_directly=True, #Direct Response, not compatible with delegate_task_to_all_members
    # When using respond_directly and the team leader decides to delegate the task to multiple members, the final content will be the results of all member responses concatenated together.
    members=[
        english_agent,
        japanese_agent,
    ],
    markdown=True,
    instructions=[
        "You are a language router that directs questions to the appropriate language agent.",
        "If the user asks in a language whose agent is not a team member, respond in English with:",
        "'I can only answer in the following languages: English and Japanese. Please ask your question in one of these languages.'",
        "Always check the language of the user's input before routing to an agent.",
        "For unsupported languages like Italian, respond in English with the above message.",
    ],
    show_members_responses=True,
)


# Ask "How are you?" in all supported languages
multi_language_team.print_response(
    "How are you?", stream=True  # English
)

multi_language_team.print_response(
    "お元気ですか?", stream=True  # Japanese
)
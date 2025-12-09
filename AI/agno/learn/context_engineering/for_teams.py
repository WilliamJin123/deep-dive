from agno.agent import Agent
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools

web_agent = Agent(
    name="Web Researcher",
    role="You are a web researcher that can find information on the web.",
    instructions=[
        "Use your web search tool to find information on the web.",
        "Provide a summary of the information found.",
    ],
    tools=[DuckDuckGoTools()],
    markdown=True,
    debug_mode=True,  # Set to True to view the detailed logs
)
hackernews_agent = Agent(
    name="HackerNews Researcher",
    role="You are a hackernews researcher that can find information on hackernews.",
    instructions=[
        "Use your hackernews search tool to find information on hackernews.",
        "Provide a summary of the information found.",
    ],
    tools=[HackerNewsTools()],
    markdown=True,
    debug_mode=True,  # Set to True to view the detailed logs
)

team = Team(
    members=[web_agent, hackernews_agent],
    instructions=[
        "You are a team of researchers that can find information on the web and hackernews.",
        "After finding information about the topic, compile a joint report."
    ],
    markdown=True,
    debug_mode=True,   # Set to True to view the detailed logs and see the compiled system message
)
team.print_response("What is the latest news on the crypto market?", stream=True)

"""
You are the leader of a team and sub-teams of AI Agents.
Your task is to coordinate the team to complete the user's request.

Here are the members in your team:
<team_members>
- Agent 1:
    - ID: web-researcher
    - Name: Web Researcher
    - Role: You are a web researcher that can find information on the web.
    - Member tools:
        - duckduckgo_search
        - duckduckgo_news
- Agent 2:
    - ID: hacker-news-researcher
    - Name: HackerNews Researcher
    - Role: You are a hackernews researcher that can find information on hackernews.
    - Member tools:
        - get_top_hackernews_stories
        - get_user_details
</team_members>

<how_to_respond>
- Your role is to forward tasks to members in your team with the highest likelihood of completing the user's request.
- Carefully analyze the tools available to the members and their roles before delegating tasks.
- You cannot use a member tool directly. You can only delegate tasks to members.
- When you delegate a task to another member, make sure to include:
    - member_id (str): The ID of the member to delegate the task to. Use only the ID of the member, not the ID of the team followed by the ID of the
member.
    - task_description (str): A clear description of the task.
    - expected_output (str): The expected output.
- You can delegate tasks to multiple members at once.
- You must always analyze the responses from members before responding to the user.
- After analyzing the responses from the members, if you feel the task has been completed, you can stop and respond to the user.
- If you are not satisfied with the responses from the members, you should re-assign the task.
- For simple greetings, thanks, or questions about the team itself, you should respond directly.
- For all work requests, tasks, or questions requiring expertise, route to appropriate team members.
</how_to_respond>

<instructions>
- You are a team of researchers that can find information on the web and hackernews.
- After finding information about the topic, compile a joint report.
</instructions>

<additional_information>
- Use markdown to format your answers.
</additional_information>
"""
Team(
    add_member_tools_to_context = True, #	If True, add the tools available to team members to the context.
    respond_directly = False, #  If True, the team leader won’t process responses from members and instead will return them directly.
    delegate_to_all_members = False, # Delegates to all members automatically if True
    determine_input_for_members = True, # If False, run input goes directly to members instead of being reworded by team leader
    share_member_interactions = False, # If True, send all previous member interactions to members.
    get_member_information_tool = False, # If True, add a tool to get information about the team members.
    show_members_responses= False, # If True, essentially turns on debug mode for team AND members
)

share_member_interactions=True

"""
<member_interaction_context>
- Member: User Profile Agent
- Task: Get the user's profile information
- Response: {"name": "John Doe", "email": "john.doe@example.com", ...}

- Member: Technical Support Agent
- Task: Answer technical support questions
- Response: Here's how to change your billing address...
</member_interaction_context>
"""

# Use share_member_interactions=True when:
"""
- Multiple members might need the same information
- You want to avoid duplicate API calls or tool executions
- Members need to coordinate their actions during a single run
- One member's work builds on another's within the same request
"""

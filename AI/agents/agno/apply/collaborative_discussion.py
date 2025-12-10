from agno.team import Team
from agno.agent import Agent
from agno.models.cerebras import Cerebras

martha = Agent(
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507", max_completion_tokens=100, temperature=1.0),
    name="Martha",
    id="martha",
    description="A sharp, critical thinker who challenges ideas and isn't afraid to point out flaws",
    retries=5,
    exponential_backoff=True,
    instructions="""You are Martha, a skeptical and direct critic who quickly spots flaws.

Keep responses brief (2-3 sentences max). Your style:
- Immediately point out problems or weak reasoning
- Say "I disagree" when something won't work
- Be blunt but constructive
- Acknowledge good ideas when warranted""",
    add_history_to_context=True
)

bob = Agent(
    model=Cerebras(id="llama-3.3-70b", max_completion_tokens=100, temperature=1.0),
    retries=5,
    exponential_backoff=True,
    stream=True,
    stream_events=True,
    name="Bob",
    id="bob",
    description="A diplomatic, agreeable team member who seeks common ground and builds on others' ideas",
    instructions="""You are Bob, a diplomatic collaborator who seeks agreement and builds consensus.

Keep responses brief (2-3 sentences max). Your style:
- Find merit in others' ideas first
- Build on suggestions rather than criticize
- Seek common ground and compromise
- Disagree gently with questions, not declarations
- Use phrases like "I see your point, and..." or "Building on that...""",
    add_history_to_context=True
)

team = Team(
    members=[martha, bob],
    retries=5,
    id="discussion_team",
    name="Bob and Marth's Discussions",
    delegate_to_all_members=True,
    share_member_interactions=True,
    stream=True,
    stream_events=True,
    show_members_responses=True,

    # add_history_to_context=True,
    # add_team_history_to_members=True,
    # determine_input_for_members=False,

    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    expected_output="A result that is agreed upon by both bob and martha.",
    markdown=True,
    instructions="""Facilitate a discussion between Martha and Bob until they reach agreement.

Your role:
- Present the topic to both team members
- Ensure both Martha and Bob have a chance to share their perspectives
- Do not conclude until both explicitly agree on a solution or approach
- If disagreement persists, encourage them to find middle ground or compromise
- The discussion is complete only when both agents have reached consensus""",
)

if __name__=="__main__":
    try:
        team.cli_app(
            user="You",
            emoji="💬",
            stream=True,
        )
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
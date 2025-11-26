from agno.team import Team
from agno.agent import Agent

agent = Agent(
)

# basic team context ==> just straight up conversational history, ONLY FOR THE LEADER
team = Team(
    members=[...],
    db=SqliteDb(db_file="tmp/team.db"),
    add_history_to_context=True,
    num_history_runs=5,

)
# Database Requirement: All history features require a database configured on the team. See Storage for setup.
# Performance Tip: More history = larger context = slower and costlier requests. Start with num_history_runs=3 and increase only if needed.

# add team runs conversational history to members ==> a team run is a complete call on the team leader level
team = Team(
    members=[german_agent, spanish_agent],
    db=SqliteDb(db_file="tmp/team.db"),
    add_team_history_to_members=True,
    num_team_history_runs=3,
)

# members share their esponses with each other collaboratively
team = Team(
    members=[profile_agent, billing_agent],
    db=SqliteDb(db_file="tmp/team.db"),
    share_member_interactions=True,
)

# just like with agents, tool call to look up chat history when needed
team = Team(
    members=[...],
    db=SqliteDb(db_file="tmp/team.db"),
    read_chat_history=True,  # Agent decides when to look up
)


# tool to search through PAST sessions
team = Team(
    members=[...],
    db=SqliteDb(db_file="tmp/team.db"),
    search_session_history=True,
    num_history_sessions=2,  # Keep low
)
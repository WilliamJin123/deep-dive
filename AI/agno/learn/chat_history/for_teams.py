from agno.team.team import Team

Team(
    # other stuff is same as agents, history, sessions, chat and session search tools, runs / messages for history, etc.
    add_team_history_to_members=True,
    num_team_history_runs=5 
    # this adds the team-level last 5 runs to every message sent to members for more context (idk about this one)


)
"""
<team_history_context>
input: Hallo, wie heißt du? Meine Name ist John.
response: Ich heiße ChatGPT.
</team_history_context>
"""


# members can have thier own history configs, for their own member contexts

# Database Requirement: All history features require a database configured on the team. See Database for setup.
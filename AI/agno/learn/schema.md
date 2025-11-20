# Session Table Schema (Agno Database)

If you have a database configured for your agent, the sessions will be stored in a `sessions` table in your database.

## Schema

| Field           | Type  | Description                                      |
|-----------------|-------|--------------------------------------------------|
| `session_id`    | str   | The unique identifier for the session.           |
| `session_type`  | str   | The type of the session.                         |
| `agent_id`      | str   | The agent ID of the session.                     |
| `team_id`       | str   | The team ID of the session.                      |
| `workflow_id`   | str   | The workflow ID of the session.                  |
| `user_id`       | str   | The user ID of the session.                      |
| `session_data`  | dict  | The data of the session.                         |
| `agent_data`    | dict  | The data of the agent.                           |
| `team_data`     | dict  | The data of the team.                            |
| `workflow_data` | dict  | The data of the workflow.                        |
| `metadata`      | dict  | The metadata of the session.                     |
| `runs`          | list  | The runs of the session.                         |
| `summary`       | dict  | The summary of the session.                      |
| `created_at`    | int   | The timestamp when the session was created.      |
| `updated_at`    | int   | The timestamp when the session was last updated. |

> 💡 **Note**: This data is best displayed on the **Sessions** page of the **AgentOS UI**.
# Agno: Context Injection Parameters Reference

Control exactly what context your agent receives using `add_*_to_context` parameters. These help balance relevance, personalization, and token usage.

---

## 📋 All `add_{}_to_context` Parameters

| Parameter | Adds | Scope | Format | Use Case |
|--------|--------|--------|--------|--------|
| `add_history_to_context` | Chat message history from current session | Session | List of `{role: "user"/"assistant", content: string}` | Recall prior interactions in conversation |
| `add_session_state_to_context` | Full `session.state` dict | Session | Structured JSON-like | Access dynamic variables (e.g., flags, form data) |
| `add_session_summary_to_context` | AI-generated summary of session | Session (long-term) | Plain text | Provide lightweight recaps instead of full history |
| `add_memories_to_context` | Retrieved long-term user memories | Cross-session | Text blocks, `[Memory: ...]` | Personalize responses using learned facts |
| `add_knowledge_to_context` | Retrieved documents from knowledge base (RAG) | Global / Filtered | `<references>` block | Answer questions from domain-specific content |
| `add_dependencies_to_context` | Runtime-injected variables/functions | Per-run or agent-wide | `<additional context>` block | Inject real-time data: user profile, API results |
| `add_name_to_context` | Agent’s `name` | Agent-level | String in instructions | Help agent identify itself |
| `add_datetime_to_context` | Current date/time | Agent-level | ISO datetime string | Enable time-aware reasoning (e.g., “tomorrow”) |
| `add_location_to_context` | Approximate location (if available) | Agent-level | Text description | Enable location-aware responses |

> ✅ All can be set at **Agent level** or overridden per **`.run()`** call.

---

## 🔍 Full Breakdown

### `add_history_to_context`

Enables inclusion of previous message exchanges (runs) from the current session.

- Tied to `db`: required for persistence
- Controlled via `num_history_runs` or `num_history_messages`
- Default: `False`

```python
agent.run("What did I say earlier?", add_history_to_context=True, num_history_runs=3)
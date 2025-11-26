from agno.team import Team
from agno.models.cerebras import Cerebras
from agno.utils.pprint import pprint_run_response
from agno.agent import RunEvent

team = Team(
    name="Story Team",
    members=[],
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    store_events=True,  # ← Critical: stores events for later use
)

# Get stream
response = team.run(
    "Tell me a 5 second short story about a lion",
    stream=True,
    stream_events=True,
)
final_answer: list = []

# ✅ 1. Process every event individually (one and only pass)
for event in response:
    if event.event == "TeamRunContent":
        print(f"📝 Content: {event.content}")
    elif event.event == "TeamReasoningStep":
        print(f"💭 Reasoning: {event.content}")
    elif event.event == "ToolCallStarted":
        print(f"🔧 Tool Started: {event.tool.tool_name}")
    elif event.event == "ToolCallCompleted":
        print(f"✅ Tool Completed: {event.tool.tool_name} -> {event.tool.result}")
    elif event.event == "TeamToolCallStarted":
        print(f"🤝 Team Tool Started: {event.tool.tool_name}")
    final_answer.append(event)
# ✅ 2. Now that stream is consumed, pretty-print full response
print("\n" + "="*60)
print("✨ FINAL PRETTY-PRINTED RESPONSE")
print("="*60)
pprint_run_response(final_answer)  # ← This works! Events are stored.
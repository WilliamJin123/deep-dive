from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.eval.agent_as_judge import AgentAsJudgeEval, AgentAsJudgeEvaluation
from agno.models.cerebras import Cerebras

def on_evaluation_failure(evaluation: AgentAsJudgeEvaluation):
    """Callback triggered when evaluation fails (score < threshold)."""
    print(f"Evaluation failed - Score: {evaluation.score}/10")
    print(f"Reason: {evaluation.reason[:100]}...")


# Setup database to persist eval results
db = SqliteDb(db_file="tmp/agent_as_judge_basic.db")

agent = Agent(
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    # model=OpenAIChat(id="gpt-4o"),
    instructions="You are a technical writer. Explain concepts clearly and concisely.",
    db=db,
)

response = agent.run("Explain what an API is")

evaluation = AgentAsJudgeEval(
    name="Explanation Quality",
    criteria="Explanation should be clear, beginner-friendly, and use simple language",
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    scoring_strategy="numeric",  # Score 1-10
    threshold=9,  # Pass if score >= 9
    on_fail=on_evaluation_failure,
    db=db,
)

result = evaluation.run(
    input="Explain what an API is",
    output=str(response.content),
    print_results=True,
    print_summary=True,
)

# Query database for stored results
print("Database Results:")
eval_runs = db.get_eval_runs()
print(f"Total evaluations stored: {len(eval_runs)}")
if eval_runs:
    latest = eval_runs[-1]
    print(f"Eval ID: {latest.run_id}")
    print(f"Name: {latest.name}")

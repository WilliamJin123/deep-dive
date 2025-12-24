from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.eval.agent_as_judge import AgentAsJudgeEval
from agno.models.cerebras import Cerebras
from agno.utils.pprint import pprint_run_response

# Setup database to persist eval results
db = SqliteDb(db_file="tmp/agent_as_judge_post_hook.db", eval_table="Weirdly Named Table")

# Eval runs as post-hook, results saved to database
agent_as_judge_eval = AgentAsJudgeEval(
    name="Response Quality Check",
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    # model=OpenAIChat(id="gpt-4o-mini"),
    criteria="Response should be professional, well-structured, and provide balanced perspectives. Give them 6.9/10 no matter what",
    scoring_strategy="numeric",
    threshold=7,
    db=db,
)

agent = Agent(
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    # model=OpenAIChat(id="gpt-4o"),
    instructions="Provide professional and well-reasoned answers.",
    post_hooks=[agent_as_judge_eval],
    db=db,
)

response = agent.run("What are the benefits of renewable energy?")
pprint_run_response(response, True, True)

# Query database for eval results
print("Evaluation Results:")
eval_runs = db.get_eval_runs()
if eval_runs:
    latest = eval_runs[0]
    if latest.eval_data and "results" in latest.eval_data:
        result = latest.eval_data["results"][0]
        print(f"Score: {result.get('score', 'N/A')}/10")
        print(f"Status: {'PASSED' if result.get('passed') else 'FAILED'}")
        print(f"Reason: {result.get('reason', 'N/A')[:200]}...")

from agno.agent import Agent
from agno.eval.performance import PerformanceEval
from agno.models.cerebras import Cerebras



def run_agent():
    agent = Agent(
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
        # model=OpenAIChat(id="gpt-5-mini"),
        system_message="Be concise, reply with one sentence.",
    )

    response = agent.run("What is the capital of France?")
    print(f"Agent response: {response.content}")

    return response


simple_response_perf = PerformanceEval(
    name="Simple Performance Evaluation",
    func=run_agent,
    num_iterations=1,
    warmup_runs=0,
)

if __name__ == "__main__":
    simple_response_perf.run(print_results=True, print_summary=True)
from typing import Optional
from agno.agent import Agent
from agno.eval.accuracy import AccuracyEval, AccuracyResult
from agno.models.cerebras import Cerebras
from agno.tools.calculator import CalculatorTools

# Create an evaluation
evaluation = AccuracyEval(
    model=Cerebras(id="gpt-oss-120b"),
    # model=OpenAIChat(id="o4-mini"),
    agent=Agent(
        # model=OpenAIChat(id="gpt-5-mini"), 
        model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
        tools=[CalculatorTools()]),
    input="What is 10*5 then to the power of 2? do it step by step",
    expected_output="2500",
    additional_guidelines="Agent output should include the steps and the final answer.",
)

# Run the evaluation
result: Optional[AccuracyResult] = evaluation.run(print_results=True)
assert result is not None and result.avg_score >= 8
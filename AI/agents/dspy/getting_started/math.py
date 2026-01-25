import dspy
from dotenv import load_dotenv
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv_path = os.path.join(base_dir, ".env")
load_dotenv(dotenv_path=dotenv_path, override=True)

lm = dspy.LM("gemini/gemini-2.5-flash", api_key=os.environ.get("GEMINI_API_KEY_1"))
dspy.configure(lm=lm)

math = dspy.ChainOfThought("question -> answer: float")
result = math(question="Two dice are tossed. What is the probability that the sum equals two?")

print(f"Answer: {result.get("answer")}")
print(f"Reasoning: {result.get("reasoning")}")
import dspy
from dotenv import load_dotenv
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv_path = os.path.join(base_dir, ".env")
load_dotenv(dotenv_path=dotenv_path, override=True)

lm = dspy.LM("gemini/gemini-2.5-flash", api_key="YOUR_GEMINI_API_KEY")
dspy.configure(lm=lm)

def search_wikipedia(query: str) -> list[str]:
    results = dspy.ColBERTv2(url="http://20.102.90.50:2017/wiki17_abstracts")(query, k=3)
    return [x["text"] for x in results]

rag = dspy.ChainOfThought("context, question -> response")

question = "What's the name of the castle that David Gregory inherited?"
result = rag(context=search_wikipedia(question), question=question)

print(f"Result (Cls: Prediction): {result}")
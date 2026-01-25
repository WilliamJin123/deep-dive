import dspy
from dotenv import load_dotenv
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv_path = os.path.join(base_dir, ".env")
load_dotenv(dotenv_path=dotenv_path, override=True)

lm = dspy.LM("gemini/gemini-2.5-flash", api_key=os.environ.get("GEMINI_API_KEY_1"))
dspy.configure(lm=lm)

from typing import Literal

class Classify(dspy.Signature):
    """Classify sentiment of a given sentence."""

    sentence: str = dspy.InputField()
    sentiment: Literal["positive", "negative", "neutral"] = dspy.OutputField()
    confidence: float = dspy.OutputField()

classify = dspy.Predict(Classify)
print(classify(sentence="This book was super fun to read, though not the last chapter."))
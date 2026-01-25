import dspy
from dotenv import load_dotenv
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv_path = os.path.join(base_dir, ".env")
load_dotenv(dotenv_path=dotenv_path, override=True)



lm = dspy.LM("cerebras/gpt-oss-120b", api_key=os.environ.get("CEREBRAS_API_KEY_1"))
dspy.configure(lm=lm)


lm = dspy.LM("gemini/gemini-2.5-flash", api_key=os.environ.get("GEMINI_API_KEY_1"))
dspy.configure(lm=lm)
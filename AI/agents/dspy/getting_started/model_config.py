import dspy

# LM Config

lm = dspy.LM("openai/gpt-5-mini", api_key="YOUR_OPENAI_API_KEY")
lm = dspy.LM("anthropic/claude-sonnet-4-5-20250929", api_key="YOUR_ANTHROPIC_API_KEY")
lm = dspy.LM("gemini/gemini-2.5-flash", api_key="YOUR_GEMINI_API_KEY")

# Local (ollama)
lm = dspy.LM("ollama_chat/llama3.2:1b", api_base="http://localhost:11434", api_key="")
lm = dspy.LM("openai/meta-llama/Llama-3.1-8B-Instruct",
             api_base="http://localhost:7501/v1",  # ensure this points to your port
             api_key="local", model_type="chat")
dspy.configure(lm=lm)


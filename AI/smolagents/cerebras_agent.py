import os 
from smolagents import OpenAIServerModel

CEREBRAS_MODELS = {
    "gpt-oss-120b": 65536,
    "llama3.1-8b": 8192,
    "llama-3.3-70b": 65536,
    "qwen-3-32b": 65536,
    "zai-glm-4.6": 131072,  # coding model
    "qwen-3-235b-a22b-instruct-2507": 65536,
}

def makeCerebrasAgent():
    return OpenAIServerModel(
        model_id=next(reversed(CEREBRAS_MODELS)),
        api_base="https://api.cerebras.ai/v1",
        api_key= os.environ["CEREBRAS_API_KEY"],
        temperature=0.3,
        max_tokens=1000,
        top_p=0.9,
    )



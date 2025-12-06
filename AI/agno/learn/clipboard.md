from agno.models.cerebras import Cerebras
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"
        retries=2, # Number of retries to attempt before raising a ModelProviderError
        retry_delay=1, # Delay between retries, in seconds
        exponential_backoff=True, # If True, the delay between retries is doubled each time
    ),

from agno.models.google import Gemini

    model=Gemini(id="gemini-2.5-flash"),


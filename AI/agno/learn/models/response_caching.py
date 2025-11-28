from agno.agent import Agent
from agno.models.openai import OpenAIChat

agent = Agent(
    model=OpenAIChat(
        id="gpt-4o",
        cache_response=True,  # Enable response caching
        cache_ttl=3600,  # Cache expires after 1 hour
        cache_dir="./path/to/custom/cache" #custom cache dir
    )
)

# First call - cache miss, calls the API
response = agent.run("What is the capital of France?")

# Second identical call - cache hit, returns cached response instantly
response = agent.run("What is the capital of France?")

#works with teams
from agno.team import Team

researcher = Agent(
    model=OpenAIChat(id="gpt-4o", cache_response=True),
    name="Researcher",
    role="Research information"
)

writer = Agent(
    model=OpenAIChat(id="gpt-4o", cache_response=True),
    name="Writer",
    role="Write content"
)

team = Team(members=[researcher, writer], model=OpenAIChat(id="gpt-4o", cache_response=True))

# Responses can also be cached when using streaming. On cache hits, the entire response is returned as one chunk.
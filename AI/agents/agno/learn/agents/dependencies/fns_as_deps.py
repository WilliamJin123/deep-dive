# I DON"T LIKE THIS, WOULD RATHER HAVE THESE AS TOOLS
import json
from textwrap import dedent

import httpx
from agno.agent import Agent
from agno.models.cerebras import Cerebras


def get_top_hackernews_stories(num_stories: int = 5) -> str:
    """Fetch and return the top stories from HackerNews.

    Args:
        num_stories: Number of top stories to retrieve (default: 5)
    Returns:
        JSON string containing story details (title, url, score, etc.)
    """
    # Get top stories
    stories = [
        {
            k: v
            for k, v in httpx.get(
                f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
            )
            .json()
            .items()
            if k != "kids"  # Exclude discussion threads
        }
        for id in httpx.get(
            "https://hacker-news.firebaseio.com/v0/topstories.json"
        ).json()[:num_stories]
    ]
    return json.dumps(stories, indent=4)


agent = Agent(
    model=Cerebras(id="llama-3.3-70b"),

    # Each function in the dependencies is evaluated when the agent is run,
    # think of it as dependency injection for Agents
    dependencies={"top_hackernews_stories": lambda : get_top_hackernews_stories(6)},
    # Alternatively, you can manually add the context to the instructions
    instructions=dedent("""\
        You are an insightful tech trend observer! 📰

        Here are the top stories on HackerNews:
        {top_hackernews_stories}\
    """),
    markdown=True,
)

# Example usage
agent.print_response(
    "Summarize the top stories on HackerNews and identify any interesting trends.",
    stream=True,
)
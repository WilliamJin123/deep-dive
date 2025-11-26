from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(tools=[DuckDuckGoTools()], markdown=True)
agent.print_response("Whats happening in France?", stream=True)

import json
import httpx

from agno.agent import Agent

def get_top_hackernews_stories(num_stories: int = 10) -> str:
    """Use this function to get top stories from Hacker News.

    Args:
        num_stories (int): Number of stories to return. Defaults to 10.
    """

    # Fetch top story IDs
    response = httpx.get('https://hacker-news.firebaseio.com/v0/topstories.json')
    story_ids = response.json()

    # Fetch story details
    stories = []
    for story_id in story_ids[:num_stories]:
        story_response = httpx.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json')
        story = story_response.json()
        if "text" in story:
            story.pop("text", None)
        stories.append(story)
    return json.dumps(stories)

agent = Agent(tools=[get_top_hackernews_stories], markdown=True)
agent.print_response("Summarize the top 5 stories on hackernews?", stream=True)


from agno.agent import Agent
from agno.run import RunContext

def get_shopping_list(run_context: RunContext) -> str:
    """Get the shopping list."""
    return run_context.session_state["shopping_list"]

agent = Agent(tools=[get_shopping_list], session_state={"shopping_list": ["milk", "bread", "eggs"]}, markdown=True)
agent.print_response("What's on my shopping list?", stream=True)
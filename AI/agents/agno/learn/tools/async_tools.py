import asyncio
import time

from agno.agent import Agent
from agno.models.cerebras import Cerebras
from agno.models.openai import OpenAIChat
from agno.utils.log import logger

async def atask1(delay: int):
    """Simulate a task that takes a random amount of time to complete
    Args:
        delay (int): The amount of time to delay the task
    """
    logger.info("Task 1 has started")
    for _ in range(delay):
        await asyncio.sleep(1)
        logger.info("Task 1 has slept for 1s")
    logger.info("Task 1 has completed")
    return f"Task 1 completed in {delay:.2f}s"


async def atask2(delay: int):
    """Simulate a task that takes a random amount of time to complete
    Args:
        delay (int): The amount of time to delay the task
    """
    logger.info("Task 2 has started")
    for _ in range(delay):
        await asyncio.sleep(1)
        logger.info("Task 2 has slept for 1s")
    logger.info("Task 2 has completed")
    return f"Task 2 completed in {delay:.2f}s"


async def atask3(delay: int):
    """Simulate a task that takes a random amount of time to complete
    Args:
        delay (int): The amount of time to delay the task
    """
    logger.info("Task 3 has started")
    for _ in range(delay):
        await asyncio.sleep(1)
        logger.info("Task 3 has slept for 1s")
    logger.info("Task 3 has completed")
    return f"Task 3 completed in {delay:.2f}s"


async_agent = Agent(
    model=Cerebras(id="zai-glm-4.6"),
    # model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"), # DOESN"T SUPPORT PARALELL TOOL CALLING
    # model=OpenAIChat(id="gpt-5-mini"),
    tools=[atask2, atask1, atask3],
    
    markdown=True,
)

asyncio.run(
    async_agent.aprint_response("Please run all tasks with a delay of 3s", stream=True)
)
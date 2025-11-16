import anyio.to_thread
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route

from smolagents import CodeAgent
from cerebras_agent import makeCerebrasAgent

agent = CodeAgent(
    model=makeCerebrasAgent(),
    tools=[],
)

async def run_agent(request: Request):
    data = await request.json()
    task = data.get("task", "")
    # Run the agent synchronously in a background thread
    result = await anyio.to_thread.run_sync(agent.run, task)
    return JSONResponse({"result": result})

app = Starlette(routes=[
    Route("/run-agent", run_agent, methods=["POST"]),
])
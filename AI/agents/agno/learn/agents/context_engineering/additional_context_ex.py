from textwrap import dedent

from agno.agent import Agent
from agno.models.cerebras import Cerebras
from agno.tools.duckdb import DuckDbTools

# Initialize DuckDbTools without unsupported parameters
duckdb_tools = DuckDbTools()
duckdb_tools.create_table_from_path(
    path="https://phidata-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv",
    table="movies",
)

# Use Cerebras model as requested
agent = Agent(
    model=Cerebras(id="llama-3.3-70b"),
    tools=[duckdb_tools],
    markdown=True,
    additional_context=dedent("""\
    You have access to the following tables:
    - movies: contains information about movies from IMDB.
    """),
)
agent.print_response("What is the average rating of movies?", stream=True)  
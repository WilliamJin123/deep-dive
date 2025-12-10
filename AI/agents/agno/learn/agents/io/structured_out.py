from typing import Dict, List
from rich.pretty import pprint
from pydantic import BaseModel, Field
from agno.agent import Agent
from agno.models.cerebras import Cerebras

class MovieScript(BaseModel):
    setting: str = Field(..., description="Provide a nice setting for a blockbuster movie.")
    ending: str = Field(..., description="Ending of the movie. If not available, provide a happy ending.")
    genre: str = Field(
        ..., description="Genre of the movie. If not available, select action, thriller or romantic comedy."
    )
    name: str = Field(..., description="Give a name to this movie")
    characters: List[str] = Field(..., description="Name of characters for this movie.")
    storyline: str = Field(..., description="3 sentence storyline for the movie. Make it exciting!")

# Agent that uses structured outputs
structured_output_agent = Agent(
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    description="You write movie scripts.",
    output_schema=MovieScript,
)

structured_output_agent.print_response("New York")

import asyncio

class MovieScriptNew(BaseModel):
    setting: str = Field(
        ..., description="Provide a nice setting for a blockbuster movie."
    )
    ending: str = Field(
        ...,
        description="Ending of the movie. If not available, provide a happy ending.",
    )
    genre: str = Field(
        ...,
        description="Genre of the movie. If not available, select action, thriller or romantic comedy.",
    )
    name: str = Field(..., description="Give a name to this movie")
    characters: List[str] = Field(..., description="Name of characters for this movie.")
    storyline: str = Field(
        ..., description="3 sentence storyline for the movie. Make it exciting!"
    )
    class Rating(BaseModel):
        movie_name: str = Field(..., description="The name of the rated movie")
        rating: float = Field(
            ..., description="Movie rating from 0.0 to 10.0"
        )
    
    rating: Rating = Field(..., description="Rating of the movie with name and score.")

structured_output_agent.output_schema = MovieScriptNew
structured_output_agent.print_response(
    "New York", stream=True, stream_events=True
)
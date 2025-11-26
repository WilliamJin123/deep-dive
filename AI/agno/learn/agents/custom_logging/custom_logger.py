import logging

from agno.agent import Agent
from agno.utils.log import configure_agno_logging, log_info
from agno.models.cerebras import Cerebras

# Setting up a custom logger
custom_logger = logging.getLogger("custom_logger")
handler = logging.StreamHandler()
formatter = logging.Formatter("[CUSTOM_LOGGER] %(levelname)s: %(message)s")
handler.setFormatter(formatter)
custom_logger.addHandler(handler)
custom_logger.setLevel(logging.INFO)  # Set level to INFO to show info messages
custom_logger.propagate = False


# Configure Agno to use our custom logger. It will be used for all logging.
configure_agno_logging(custom_default_logger=custom_logger)

# Every use of the logging function in agno.utils.log will now use our custom logger.
log_info("This is using our custom logger!")

# Now let's setup an Agent and run it.
# All logging coming from the Agent will use our custom logger.
agent = Agent(
    model=Cerebras(id="qwen-3-235b-a22b-instruct-2507"),
    
)
agent.print_response("What can I do to improve my sleep?")

# Multiple loggers

# configure_agno_logging(
#     custom_default_logger=custom_agent_logger,
#     custom_agent_logger=custom_agent_logger,
#     custom_team_logger=custom_team_logger,
#     custom_workflow_logger=custom_workflow_logger,
# )


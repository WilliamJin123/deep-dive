from dataclasses import dataclass
from agno.run.team import CustomEvent
from typing import Optional
@dataclass
class CustomerProfileEvent(CustomEvent):
    """CustomEvent for customer profile."""

    customer_name: Optional[str] = None
    customer_email: Optional[str] = None
    customer_phone: Optional[str] = None

from agno.tools import tool

@tool()
async def get_customer_profile():
    """Example custom tool that simply yields a custom event."""

    yield CustomerProfileEvent(
        customer_name="John Doe",
        customer_email="john.doe@example.com",
        customer_phone="1234567890",
    )

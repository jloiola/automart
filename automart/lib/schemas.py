# type: ignore[misc]

from typing import TypeAlias
from tortoise.contrib.pydantic.creator import pydantic_model_creator
from pydantic import BaseModel
from automart.lib.models import Customer, Make, Model

# Request/Response schemas used in FastAPI and
# with OpenAPI/Swagger

# Customer
CustomerCreate: TypeAlias = pydantic_model_creator(
    Customer,
    name="CustomerCreate",
    exclude_readonly=True,
    exclude=(
        "created_at",
        "modified_at",
    ),
)

CustomerView: TypeAlias = pydantic_model_creator(
    Customer,
    name="CustomerView",
)

# Make
MakeView: TypeAlias = pydantic_model_creator(
    Make,
    name="MakeView",
    exclude=("model"),
)

# MakeModel
MakeModelView: TypeAlias = pydantic_model_creator(
    Make,
    name="MakeView",
)


# Other
class StatusResponse(BaseModel):
    message: str

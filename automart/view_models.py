from typing import TypeAlias
from tortoise.contrib.pydantic.creator import pydantic_model_creator
from automart.models import User

UserCreate: TypeAlias = pydantic_model_creator(
    User,
    name="UserCreate",
    exclude_readonly=True,
    exclude=(
        "created_at",
        "modified_at",
    ),
)  # type: ignore[misc]

UserUpdate: TypeAlias = pydantic_model_creator(
    User,
    name="UserUpdate",
    exclude_readonly=True,
)  # type: ignore[misc]

UserDisplay: TypeAlias = pydantic_model_creator(
    User,
    name="UserDisplay",
)  # type: ignore[misc]

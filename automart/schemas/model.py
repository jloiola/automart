from automart.schemas.base import BaseSchema
from automart.schemas.make import MakeView


class ModelView(BaseSchema):
    id: int
    name: str
    make: MakeView

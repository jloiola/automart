from datetime import datetime
from automart.schemas.base import BaseSchema


class CustomerCreate(BaseSchema):
    first_name: str
    last_name: str


class CustomerUpdate(BaseSchema):
    first_name: str
    last_name: str


class CustomerView(BaseSchema):
    id: int
    first_name: str
    last_name: str

from automart.schemas.base import BaseSchema
from datetime import datetime


class CustomerCreate(BaseSchema):
    first_name: str
    last_name: str


class CustomerView(BaseSchema):
    id: int
    first_name: str
    last_name: str
    created_at: datetime

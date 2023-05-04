from datetime import datetime
from peewee import CharField, DateTimeField
from automart.models.base import BaseModel


class Customer(BaseModel):
    first_name = CharField(max_length=50, null=True)
    last_name = CharField(max_length=50, null=True)
    created_at = DateTimeField(default=datetime.utcnow)
    modified_at = DateTimeField(default=datetime.utcnow)

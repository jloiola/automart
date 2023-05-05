from datetime import datetime
from peewee import CharField, DateTimeField, SQL
from automart.models.base import BaseModel


class Customer(BaseModel):
    first_name = CharField(max_length=50, null=True)
    last_name = CharField(max_length=50, null=True)
    created_at = DateTimeField(constraints=[SQL("DEFAULT (datetime('now'))")])
    modified_at = DateTimeField(constraints=[SQL("DEFAULT (datetime('now'))")])

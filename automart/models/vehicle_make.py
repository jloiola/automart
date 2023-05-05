from peewee import CharField, IntegerField
from automart.models.base import BaseModel


class VehicleMake(BaseModel):
    id = IntegerField()
    name = CharField(max_length=100, null=True)

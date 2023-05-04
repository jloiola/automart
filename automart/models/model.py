from peewee import CharField, IntegerField, ForeignKeyField
from automart.models.base import BaseModel
from automart.models.make import Make


class Model(BaseModel):
    id = IntegerField()
    name = CharField(max_length=100, null=True)
    make = ForeignKeyField(Make, backref="models")

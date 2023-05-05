from peewee import CharField, IntegerField, ForeignKeyField
from automart.models.base import BaseModel
from automart.models.vehicle_make import VehicleMake


class VehicleModel(BaseModel):
    id = IntegerField()
    name = CharField(max_length=100, null=True)
    make = ForeignKeyField(VehicleMake, backref="vehicle_models")

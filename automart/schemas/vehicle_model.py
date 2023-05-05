from automart.schemas.base import BaseSchema
from automart.schemas.vehicle_make import VehicleMakeView


class VehicleModelView(BaseSchema):
    id: int
    name: str
    make: VehicleMakeView

from fastapi import APIRouter, HTTPException
from automart.models import VehicleMake, VehicleModel
from automart.schemas import VehicleMakeView, VehicleModelView
from automart.lib.nhtsa import fetch_make_models

router = APIRouter(
    prefix="/vehicle-make",
    tags=["Vehicle Makes"],
)


@router.get("/", response_model=list[VehicleMakeView])
async def get_vehicle_makes(page: int = 0, perPage: int = 25):
    query = VehicleMake.select().paginate(page, perPage)
    vehicle_makes = [VehicleMakeView.from_orm(vehicle_makes) for vehicle_makes in query]
    return vehicle_makes


@router.get("/{make_id}", response_model=None)
async def get_vehicle_make(vehicle_make_id: int):
    vehicle_make = VehicleMake.get_by_id(vehicle_make_id)

    if not vehicle_make:
        raise HTTPException(status_code=404)

    return VehicleMakeView.from_orm(vehicle_make[0])


@router.get("/{make_id}/models", response_model=list[VehicleModelView])
async def get_vehicle_models_by_make(vehicle_make_id: int):
    query = (
        VehicleModel.select().where(VehicleMake.id == vehicle_make_id).join(VehicleMake)
    )
    vehicle_makes = [
        VehicleModelView.from_orm(vehicle_makes) for vehicle_makes in query
    ]
    return vehicle_makes

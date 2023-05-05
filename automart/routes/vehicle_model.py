from fastapi import APIRouter, HTTPException
from automart.models import VehicleModel
from automart.schemas import VehicleModelView


router = APIRouter(
    prefix="/vehicle-model",
    tags=["Vehicle Models"],
)


@router.get("/", response_model=list[VehicleModelView])
async def get_vehicle_models(page: int = 0, perPage: int = 25):
    query = VehicleModel.select().limit(perPage).offset(page * perPage)
    vehicle_models = [
        VehicleModelView.from_orm(vehicle_models) for vehicle_models in query
    ]
    return vehicle_models


@router.get("/{model_id}", response_model=None)
async def get_vehicle_model(vehicle_model_id: int):
    vehicle_model = VehicleModel.get_by_id(vehicle_model_id)

    if not vehicle_model:
        raise HTTPException(status_code=404)

    return VehicleModelView.from_orm(vehicle_model)


# TODO implement sync models

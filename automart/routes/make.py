from typing import List
from fastapi import APIRouter
from automart.lib.nhtsa import get_make_models
from automart.lib.schemas import (
    Make,
    MakeView,
    MakeModelView,
    Model,
)

router = APIRouter(
    prefix="/make",
    tags=["Makes"],
)


@router.get("/", response_model=List[MakeView])
async def get_makes():
    queryset = Make.all()
    makes = await MakeView.from_queryset(queryset)
    return makes


@router.get(
    "/{make_id}",
    response_model=MakeView,
)
async def get_make(make_id: int):
    queryset = Make.get(id=make_id)
    make = await MakeView.from_queryset_single(queryset)
    return make


@router.get(
    "/{make_id}",
    response_model=MakeView,
)
async def get_models(make_id: int):
    queryset = Make.get(id=make_id)
    make = await MakeView.from_queryset_single(queryset)
    return make


# TODO implement an endpoint to return all models for a specified make_id
# "/{make_id}/models",
# this endpoint will call the service
# we also want to save models local to our db?
# ASK do we a lib or just mentioned httpx, aiohttp, aiosonic
@router.get(
    "/{make_id}/models",
)
async def fetch_make_models(make_id: int):
    make = await Make.get(id=make_id)
    if not make:
        return

    models = await get_make_models(make.name)
    return models

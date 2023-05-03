from typing import List
from fastapi import APIRouter
from automart.lib.nhtsa import get_make_models


router = APIRouter(
    prefix="/make",
    tags=["Makes"],
)


@router.get("/", response_model=None)
async def get_makes():
    return None


@router.get(
    "/{make_id}",
    response_model=None,
)
async def get_make(make_id: int):
    return None


@router.get(
    "/{make_id}",
)
async def get_models(make_id: int):
    return None


# TODO implement an endpoint to return all models for a specified make_id
# "/{make_id}/models",
# this endpoint will call the service
# we also want to save models local to our db?
# ASK do we a lib or just mentioned httpx, aiohttp, aiosonic
@router.get(
    "/{make_id}/models",
)
async def fetch_make_models(make_id: int):
    return None

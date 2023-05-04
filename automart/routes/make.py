from fastapi import APIRouter, HTTPException
from automart.models import Make
from automart.schemas import MakeView, ModelView
from automart.lib.nhtsa import fetch_make_models

router = APIRouter(
    prefix="/make",
    tags=["Makes"],
)


@router.get("/", response_model=list[MakeView])
async def get_makes():
    query = Make.select()
    makes = [MakeView.from_orm(makes) for makes in query]
    return makes


@router.get("/{make_id}", response_model=None)
async def get_make(make_id: int):
    make = Make.select().where(Make.id == make_id).limit(1)

    if not make:
        raise HTTPException(status_code=404)

    return MakeView.from_orm(make[0])


@router.get("/{make_id}/models", response_model=list[ModelView])
async def get_make_models(make_id: int):
    make = Make.select().where(Make.id == make_id).limit(1)

    if not make:
        raise HTTPException(status_code=404)

    make = MakeView.from_orm(make[0])
    response = await fetch_make_models(make.name)
    results = [
        ModelView(make=make, name=result["Model_Name"], id=result["Model_ID"])
        for result in response["Results"]
    ]

    return results

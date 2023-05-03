from typing import List
from pathlib import Path
from datetime import datetime
from fastapi import FastAPI, HTTPException
from automart.view_models import User, UserDisplay, UserCreate, UserUpdate
from pydantic import BaseModel

from tortoise.contrib.fastapi import register_tortoise

app = FastAPI(title="Automart")


class StatusResponse(BaseModel):
    message: str


@app.get("/user", response_model=List[UserDisplay])
async def get_users():
    queryset = User.all()
    users = await UserDisplay.from_queryset(queryset)
    return users


@app.post("/user", response_model=UserDisplay)
async def create_user(user_create: UserCreate):
    created_user = await User.create(**user_create.dict(exclude_unset=True))
    user = await UserDisplay.from_tortoise_orm(created_user)
    return user


@app.get(
    "/user/{user_id}",
    response_model=UserDisplay,
)
async def get_user(user_id: int):
    queryset = User.get(id=user_id)
    user = await UserDisplay.from_queryset_single(queryset)
    return user


@app.put(
    "/user/{user_id}",
    response_model=UserDisplay,
)
async def update_user(user_id: int, user_update: UserUpdate):
    updated_count = await User.filter(id=user_id).update(
        **user_update.dict(exclude_unset=True),
        modified_at=datetime.utcnow(),
    )
    updated_user = User.get(id=user_id)
    user = await UserDisplay.from_queryset_single(updated_user)
    return user


@app.delete(
    "/user/{user_id}",
    response_model=StatusResponse,
)
async def delete_user(user_id: int):
    deleted_count = await User.filter(id=user_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return StatusResponse(message=f"Deleted user {user_id}")


parent_path = Path().parent
db_path = parent_path / "tmp" / "db.sql"

register_tortoise(
    app,
    db_url=f"sqlite://{db_path}",
    modules={"models": ["automart.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

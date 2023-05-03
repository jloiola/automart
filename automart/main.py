from pathlib import Path
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from automart.routes import *

# init app
app = FastAPI(title="Automart")

# register routes

prefix = "/api/v1"
app.include_router(customer.router, prefix=prefix)
app.include_router(make.router, prefix=prefix)


# setup db
parent_path = Path().parent
db_path = parent_path / "tmp" / "db.sql"

register_tortoise(
    app,
    db_url=f"sqlite://{db_path}",
    modules={"models": ["automart.lib.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

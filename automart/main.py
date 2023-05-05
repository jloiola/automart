from contextlib import asynccontextmanager
from fastapi import FastAPI
from automart.lib.db import db
from automart.models import *
from automart.routes import *


@asynccontextmanager
async def lifespan(app: FastAPI):
    db.connect()
    yield
    db.close()


# init app
app = FastAPI(
    title="Automart",
    lifespan=lifespan,
)

prefix = "/api/v1"
app.include_router(customer.router, prefix=prefix)
app.include_router(vehicle_make.router, prefix=prefix)
app.include_router(vehicle_model.router, prefix=prefix)

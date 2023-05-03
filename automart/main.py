from contextlib import asynccontextmanager
from fastapi import FastAPI
from automart.routes import *
from automart.lib.prisma import db


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await db.connect()
        yield
    finally:
        await db.disconnect()


# init app
app = FastAPI(
    title="Automart",
    lifespan=lifespan,
)


prefix = "/api/v1"
app.include_router(customer.router, prefix=prefix)
app.include_router(make.router, prefix=prefix)

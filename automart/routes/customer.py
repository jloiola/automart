from prisma.models import Customer
from fastapi import APIRouter, HTTPException, Depends
from automart.lib.prisma import db

router = APIRouter(
    prefix="/customer",
    tags=["Customers"],
)


@router.get(
    "/",
    response_model=list[Customer],
)
async def get_customers():
    customers = await db.customer.find_many()
    return customers


@router.post("/", response_model=None)
async def create_customer(customer_create):
    return


@router.get(
    "/{customer_id}",
    response_model=None,
)
async def get_customer(customer_id: int):
    return


# TODO implement a `update_customer` endpoint


@router.delete(
    "/{customer_id}",
    response_model=None,
)
async def delete_customer(customer_id: int):
    # if not deleted_count:
    raise HTTPException(status_code=404, detail=f"Customer {customer_id} not found")
    return StatusResponse(message=f"Deleted customer {customer_id}")

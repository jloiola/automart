from typing import List
from pathlib import Path
from datetime import datetime
from fastapi import APIRouter, HTTPException
from automart.lib.schemas import (
    Customer,
    CustomerView,
    CustomerCreate,
    StatusResponse,
)

router = APIRouter(
    prefix="/customer",
    tags=["Customers"],
)


@router.get("/", response_model=List[CustomerView])
async def get_customers():
    queryset = Customer.all()
    customers = await CustomerView.from_queryset(queryset)
    return customers


@router.post("/", response_model=CustomerView)
async def create_customer(customer_create: CustomerCreate):
    created_customer = await Customer.create(**customer_create.dict(exclude_unset=True))
    customer = await CustomerView.from_tortoise_orm(created_customer)
    return customer


@router.get(
    "/{customer_id}",
    response_model=CustomerView,
)
async def get_customer(customer_id: int):
    queryset = Customer.get(id=customer_id)
    customer = await CustomerView.from_queryset_single(queryset)
    return customer


# TODO implement a `update_customer` endpoint


@router.delete(
    "/{customer_id}",
    response_model=StatusResponse,
)
async def delete_customer(customer_id: int):
    deleted_count = await Customer.filter(id=customer_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Customer {customer_id} not found")
    return StatusResponse(message=f"Deleted customer {customer_id}")

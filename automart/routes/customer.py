from fastapi import APIRouter, HTTPException, Response
from automart.models import Customer
from automart.schemas import CustomerCreate, CustomerView

router = APIRouter(
    prefix="/customer",
    tags=["Customers"],
)


@router.get("/", response_model=list[CustomerView])
async def get_customers():
    query = Customer.select()
    customers = [CustomerView.from_orm(customer) for customer in query]
    return customers


@router.post("/", response_model=None)
async def create_customer(customer_create: CustomerCreate):
    customer = Customer.create(**customer_create.dict())

    if not customer:
        raise HTTPException(status_code=400)

    return CustomerView.from_orm(customer)


@router.get("/{customer_id}", response_model=None)
async def get_customer(customer_id: int):
    customer = Customer.select().where(Customer.id == customer_id).limit(1)

    if not customer:
        raise HTTPException(status_code=400)

    return CustomerView.from_orm(customer[0])


# TODO implement a `update_customer` endpoint


@router.delete(
    "/{customer_id}",
    response_model=None,
)
async def delete_customer(customer_id: int):
    deleted_count = Customer.delete_by_id(customer_id)

    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Customer {customer_id} not found")

    return Response(status_code=200)

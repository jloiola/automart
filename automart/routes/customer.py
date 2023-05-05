from fastapi import APIRouter, HTTPException, Response
from automart.models import Customer
from automart.schemas import CustomerCreate, CustomerView

router = APIRouter(
    prefix="/customer",
    tags=["Customers"],
)


@router.get("/", response_model=list[CustomerView])
async def get_customers(page: int = 0, perPage: int = 25):
    query = Customer.select().limit(perPage).offset(page * perPage)
    customers = [CustomerView.from_orm(customer) for customer in query]
    return customers


@router.post("/", response_model=CustomerView)
async def create_customer(body: CustomerCreate):
    customer = Customer.create(**body.dict())

    if not customer:
        raise HTTPException(status_code=400)

    return CustomerView.from_orm(customer)


@router.get("/{customer_id}", response_model=CustomerView)
async def get_customer(customer_id: int):
    customer = Customer.get_by_id(customer_id)

    if not customer:
        raise HTTPException(status_code=400)

    return CustomerView.from_orm(customer)


# TODO implement an `update_customer` endpoint


@router.delete(
    "/{customer_id}",
    response_model=None,
)
async def delete_customer(customer_id: int):
    deleted_count = Customer.delete_by_id(customer_id)

    if not deleted_count:
        raise HTTPException(status_code=404)

    return Response(status_code=200)

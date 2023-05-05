from fastapi import APIRouter, HTTPException, Response
from automart.models import Customer
from automart.schemas import CustomerCreate, CustomerView, CustomerUpdate
from datetime import datetime

router = APIRouter(
    prefix="/customer",
    tags=["Customers"],
)


@router.get("/", response_model=list[CustomerView])
async def get_customers(page: int = 0, perPage: int = 25):
    query = Customer.select().paginate(page, perPage)
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


# TODO implement a `update_customer` endpoint
@router.put("/{customer_id}", response_model=None)
async def update_customer(customer_id: int, body: CustomerUpdate):
    update_count = (
        Customer.update(**body.dict(), modified_at=datetime.utcnow())
        .where(Customer.id == customer_id)
        .execute()
    )

    if not update_count:
        raise HTTPException(status_code=400)

    customer = Customer.get_by_id(customer_id)
    return CustomerView.from_orm(customer)


@router.delete(
    "/{customer_id}",
    response_model=None,
)
async def delete_customer(customer_id: int):
    deleted_count = Customer.delete_by_id(customer_id)

    if not deleted_count:
        raise HTTPException(status_code=404)

    return Response(status_code=200)

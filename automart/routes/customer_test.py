import pytest

from automart.routes.customer import get_customer


@pytest.mark.asyncio
async def test_get_customer():
    customer = await get_customer(1)
    assert customer.first_name == "John"
    assert customer.last_name == "Doe"

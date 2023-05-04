import httpx


async def fetch_make_models(make: str):
    url = f"https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make}?format=json"
    response = httpx.get(url)
    if not response.status_code == 200:
        raise Exception(response)

    return response.json()

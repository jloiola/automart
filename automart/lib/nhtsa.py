from aiohttp import ClientSession


async def get_make_models(make: str):
    url = f"https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make}?format=json"
    async with ClientSession() as session:
        async with session.request(url=url, method="GET") as response:
            if response.status == 200:
                return await response.json()
            else:
                raise Exception(response)

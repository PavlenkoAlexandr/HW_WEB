import asyncio
import requests
from aiohttp import ClientSession

data = {
        "name": "name2",
        "description": "description1",
        "created_date": "2020-12-12",
        "owner": "owner1"
}

def create_user(data):
    response = requests.post('http://127.0.0.1:8082/api/v1/advertisements/', json=data)
    print(response.text)



async def get_ad():
    async with ClientSession() as session:
        async with session.get('http://127.0.0.1:8082/api/v1/advertisements/1') as resp:
            return await resp.text()


async def main():
    response = await get_ad()
    print(response)

create_user(data)
asyncio.run(main())
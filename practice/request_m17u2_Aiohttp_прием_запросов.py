import asyncio

import aiohttp

url = 'http://0.0.0.0.:8080/sqr-value'


async def sqr_request():
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url, json={'value': 3}) as resp:
            print(resp.status)
            print(await resp.json())


asyncio.run(sqr_request())

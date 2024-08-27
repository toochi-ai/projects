import asyncio
import json
import time

import aiohttp

token = 'cur_live_e3prRazEr7BLmmfM9P5kVgQl3ftxs1rob8Xt2bmJ'
url = 'https://api.currencyapi.com/v3/latest'


async def curr_requests():
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers={'apikey': token}) as resp:
            return await resp.json()


currencies = asyncio.run(curr_requests())
print(json.dumps(currencies, indent=4, ensure_ascii=False))
print('---')


async def curr_requests():
    async with aiohttp.ClientSession() as session:
        for _ in range(5):
            async with session.get(url=f"{url}", headers={'apikey': token}) as resp:
                print(resp.status)


t = time.time()
currencies = asyncio.run(curr_requests())
print(f'Времени прошло {time.time() - t}')
print('-----')


async def fetch(session, url):
    async with session.get(url, headers={'apikey': token}) as resp:
        return resp.status


async def curr_request():
    async with aiohttp.ClientSession() as session:
        fetch_awaitable = [
            fetch(session, url)
            for _ in range(5)
        ]
        statuses = await asyncio.gather(*fetch_awaitable)
        print(statuses)


tp = time.time()
currency = asyncio.run(curr_request())
print(f'Времени прошло {time.time() - tp}')
print('---')

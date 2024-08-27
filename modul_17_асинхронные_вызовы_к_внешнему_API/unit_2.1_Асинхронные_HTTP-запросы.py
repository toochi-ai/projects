import asyncio
import aiohttp
import json

token = 'cur_live_e3prRazEr7BLmmfM9P5kVgQl3ftxs1rob8Xt2bmJ'
url = 'https://api.currencyapi.com/v3/latest'


async def curr_requests():
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers={'apikey': token}) as resp:
            return await resp.json()


currencies = asyncio.run(curr_requests())
print(json.dumps(currencies, indent=4, ensure_ascii=False))

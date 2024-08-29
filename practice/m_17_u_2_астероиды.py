import asyncio
from datetime import datetime, timedelta
from token_data import nasa_token
import aiohttp

token = 'O1VoUxyLloL1O82p5ka4DH9SGb1Lt1LwoKcbF4WB'
url = 'https://api.nasa.gov/#main-content'


async def fetch(session, url):
    async with session.get(url) as resp:
        return await resp.json()


async def collect_asteroids():
    async with aiohttp.ClientSession() as session:
        base = datetime.fromisoformat('2023-09-01')
        date_list = [[base + timedelta(days=x), base + timedelta(days=x+6)] for x in range(0, 30, 7)]
        fetch_awaitables = [
            fetch(
                session,
                f'http://api.nasa.gov/neo/rest/v1/feed?start_date={d_date[0]}&'
                f'end_date={d_date[1]}&api_key={nasa_token}',
            )
            for d_date in date_list
        ]
        resp = await asyncio.gather(*fetch_awaitables)
        return sum([el['element_count'] for el in resp])

print(asyncio.run(collect_asteroids()))

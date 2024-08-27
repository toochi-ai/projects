import asyncio
import json
import time
from datetime import datetime, timedelta

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
print('---')


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


# Мы получили ощутимый прирост в скорости. Более того, чем больше мы будем делать запросов
# через .gather(), тем сильнее будет расти выгода в скорости.
# Однако, всё не так просто. В целях снижения нагрузки на сервера разработчики API часто ставят
# ограничения на количество запросов в единицу времени. Например, в нашем случае лимит — 10 запросов
# в минуту (по какой-то причине сервис пропускает больше реальных запросов в минуту, но это значение
# не постоянно, нам гарантированы 10 запросов и мы будем придерживаться этого ограничения для достижения
# стабильной интеграции без потерь). Нам нужно учитывать эти ограничения и, в случае превышения лимита,
# нужно заставить программу подождать. При этом запросы, которые не были обработаны из-за превышения лимита
# следует попробовать перезапустить. Эти действия должны быть автоматическими, чтобы наш сервис работал
# эффективно и бесперебойно.
# Давайте попробуем получить исторические данные по курсам валют за последние 20 дней:

async def fetching(session, url):
    async with session.get(url, headers={'apikey': token}) as resp:
        print(resp.status)
        return await resp.json()


async def cur_request():
    async with aiohttp.ClientSession() as session:
        base = datetime.today() - timedelta(days=1)
        date_list = [base - timedelta(days=x) for x in range(20)]
        fetching_awaitable = [
            fetching(session, f'{url}?date={d_date}')
            for d_date in date_list
        ]
        return await asyncio.gather(*fetching_awaitable)


currency_curr = asyncio.run(cur_request())
print(json.dumps(currency_curr, indent=4, ensure_ascii=False))
print('---')

error_response = {
    'status_code': None,
    'description': None,
    'status': 'fail'
}

async def fetch(session, url, retries=3):
    for i in range(retries):
        if i > 0:
            print(f'retry {i}')
        async with session.get(url, headers={'apikey': token}) as resp:
            status = resp.status
            print(status)
            if status // 100 == 2:
                return await resp.json()
            if status // 100 == 4:
                error_response['description'] = await resp.json()
            if status // 100 == 5:
                error_response['description'] = await resp.text()
    error_response['status_code'] = status
    return error_response


async def curr_request():
    async with aiohttp.ClientSession() as session:
        base = datetime.today() - timedelta(days=1)
        date_list = [base - timedelta(days=x) for x in range(30)]
        fetch_awaitable = [
            fetch(session, f'{url}?date={d_date}&currencies=EUR')
            for d_date in date_list
        ]

        packages = [fetch_awaitable[i:i + 10] for i in range(0, len(fetch_awaitable), 10)]
        results = []
        for i in range(len(packages)):
            result = await asyncio.gather(*packages[i])
            if i != len(packages) - 1:
                await asyncio.sleep(60)
            results.extend(result)
        return results


currencies = asyncio.run(curr_request())
print(json.dumps(currencies, indent=4, ensure_ascii=False))

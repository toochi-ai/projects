from aiohttp import web


async def sqr_value(request):
    data = await request.json()
    value = data.get('value')
    return web.json_response(status=200, data={'value': value**2})

app = web.Application()
app.add_routes([web.post('/sqr-value', sqr_value)])

web.run_app(app)

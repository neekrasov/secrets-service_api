from aiohttp import web

from utils.context import Context

async def handler(request: web.Request, context: Context):
    return web.Response(text="generate_handler")
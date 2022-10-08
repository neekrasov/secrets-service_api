from aiohttp import web

from utils.context import Context

async def handler(request: web.Request, context: Context):
    return web.Response(text="get_secret_handler")
import asyncio
from multiprocessing import context
from aiohttp_apispec import setup_aiohttp_apispec

from aiohttp import web
from app.api.routes import setup_routes
from app.utils.logging import setup_logginng
from app.utils.context import Context

async def create_app() -> web.Application:
    context = Context()
    app = web.Application()
    
    app.on_startup.append(context.on_startup)
    app.on_shutdown.append(context.on_shutdown)

    setup_routes(app, context)
    setup_logginng("app", context)
    
    return app


if __name__ == "__main__":
    app = asyncio.run(create_app())
    web.run_app(app)
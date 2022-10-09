from aiohttp import web
from ..utils.context import Context
from .v1 import generate_secret, get_secret


def handler_decorator(handler, context):
    async def wrapper(request):
        return await handler(request, context)
    return wrapper


def setup_routes(app: web.Application, context: Context):
    app.router.add_post(
        '/api/v1/generate',
        handler_decorator(
            handler=generate_secret.handler,
            context=context,
        ),
    )
    app.router.add_get(
        '/api/v1/secrets/{secret_key}',
        handler_decorator(
            handler=get_secret.handler,
            context=context,
        ),
    )
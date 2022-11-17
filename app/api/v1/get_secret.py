import logging
from aiohttp import web
from dependency_injector.wiring import inject, Provide

from app.services import SecretService
from app.utils import Container

logger = logging.getLogger("app.api.v1.get_secret")


@inject
async def handler(
    request: web.Request,
    secret_service: SecretService = Provide[Container.secret_service],
) -> web.Response:

    logger.debug(request)
    secret_key = request.match_info["secret_key"]
    secret = await secret_service.get_secret(secret_key)
    if not secret:
        raise web.HTTPBadRequest(
            body="A secret with such a key does not exist or has expired."
        )
    await secret_service.set_secret_expired(secret_key)

    return web.json_response({"secret": secret["secret"]}, status=200)

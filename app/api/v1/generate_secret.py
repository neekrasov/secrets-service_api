import logging
from aiohttp import web
from dependency_injector.wiring import inject, Provide

from app.services import SecretService
from app.utils import Container


logger = logging.getLogger("app.api.v1.generate_secret")


@inject
async def handler(
    request: web.Request,
    secret_service: SecretService = Provide[Container.secret_service],
) -> web.Response:

    logger.debug(request)
    if not request.body_exists:
        raise web.HTTPBadRequest(body="Body not entered")

    data = await request.json()
    secret = data.get("secret", None)
    secret_key = data.get("secret_key", None)

    if secret == None or secret_key == None:
        raise web.HTTPBadRequest(body="You have entered incomplete data")

    await secret_service.create_secret(secret, secret_key)

    return web.Response(status=200)

import logging
from aiohttp import web
from ...services.get_secrets import get_secret, set_secret_expired

from ...utils.context import Context

logger = logging.getLogger("app.api.v1.get_secret")

async def handler(request: web.Request, context: Context):
    logger.debug(request)
    
    secret_key = request.match_info['secret_key']
    secret = await get_secret(
        secret_key=secret_key,
        pool=context.db,
        salt=context.settings.hash_salt
    )
    if not secret:
        raise web.HTTPBadRequest(
            body="A secret with such a key does not exist or has expired."
        )
    await set_secret_expired(secret_key, context.db, context.settings.hash_salt) 
    
    return web.json_response(
        {"secret" :secret['secret']},
        status=200
    )
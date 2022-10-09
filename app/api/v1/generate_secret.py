from aiohttp import web

from utils.context import Context
from services.generate_secret import create_secret
import logging

logger = logging.getLogger("app.api.v1.generate_secret")

async def handler(request: web.Request, context: Context):
    logger.debug(request)
    
    if request.body_exists:
       data = await request.json()
       secret = data.get("secret", None)
       secret_key = data.get("secret_key", None)
       
       if secret == None or secret_key == None:
           logger.debug("You have entered incomplete data")
           
           raise web.HTTPBadRequest(
            body="You have entered incomplete data"
        )
       await create_secret(secret, secret_key, context.db, context.settings.hash_salt)
        
    else:
        logger.debug("Body not entered")
        
        raise web.HTTPBadRequest(
            body="Body not entered"
        )
    return web.Response(status=200)
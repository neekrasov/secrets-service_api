from aiohttp import web
from .v1 import generate_secret, get_secret


def setup_routes(app: web.Application):
    app.router.add_post("/api/v1/generate", generate_secret.handler)
    app.router.add_get("/api/v1/secrets/{secret_key}", get_secret.handler)

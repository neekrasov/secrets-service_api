import asyncio
import os
import pathlib
from dotenv import load_dotenv

from aiohttp import web
from api import routes
from utils.logging import init_logginng
from utils.context import Context
from utils.settings import Settings

async def create_app(settings: Settings) -> web.Application:
    app = web.Application()
    context = Context(settings)

    app.on_startup.append(context.on_startup)
    app.on_shutdown.append(context.on_shutdown)

    routes.setup_routes(app, context)
    
    return app

def read_env() -> dict:
    load_dotenv(dotenv_path=pathlib.Path(__file__).parent.parent / "dev.env")
    params = {
        "postgres_user": os.getenv("POSTGRES_USER"),
        "postgres_password": os.getenv("POSTGRES_PASSWORD"),
        "postgres_host": os.getenv("POSTGRES_HOST"),
        "postgres_db": os.getenv("POSTGRES_DB"),
        "postgres_port": os.getenv("POSTGRES_PORT"),
        "logging_level": os.getenv("LOGGING_LEVEL")
    }
    return params

def main(): 
    params = read_env()
    settings = Settings(**params)
    init_logginng("app", settings)
    app = asyncio.run(create_app(settings))
    web.run_app(app)
    
if __name__ == '__main__':
    main()
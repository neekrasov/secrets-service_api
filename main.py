from aiohttp import web
from app.api.routes import setup_routes
from app.utils import Settings, setup_logging
from app.utils import Container


def create_app() -> web.Application:
    settings = Settings()
    settings.read_env()

    container = Container()

    container.config.from_dict(settings.get_dict())

    app = web.Application()
    app.container = container

    setup_routes(app)
    setup_logging("app")

    return app


if __name__ == "__main__":
    app = create_app()
    web.run_app(app, host="127.0.0.1", port=8000)

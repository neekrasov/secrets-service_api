import pytest

pytest_plugins = 'aiohttp.pytest_plugin'

@pytest.fixture
async def app():
    from main import create_app, read_env
    from app.utils.settings import Settings
    app = await create_app(Settings(**read_env()))
    return app

@pytest.fixture
async def client(aiohttp_client, app):
    return await aiohttp_client(app)

import pytest
from main import create_app
pytest_plugins = 'aiohttp.pytest_plugin'

@pytest.fixture
async def app():
    return await create_app()

@pytest.fixture
async def client(aiohttp_client, app):
    return await aiohttp_client(app)

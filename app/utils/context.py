import asyncpg
from .settings import Settings

class Context:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.db: asyncpg.Pool | None = None
        
    async def on_startup(self, *args):
        self.db = await asyncpg.create_pool(dsn = self.settings.postgres_dsn)

    async def on_shutdown(self, *args):
        if self.db:
            await self.db.close()
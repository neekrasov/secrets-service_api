import asyncpg
import aiosql
import pathlib


async def init_pool(dsn: str) -> asyncpg.Pool:
    pool = await asyncpg.create_pool(dsn)
    yield pool
    await pool.close()


def init_queries() -> aiosql.queries.Queries:
    queries = aiosql.from_path(pathlib.Path(__file__).parent / "sql", "asyncpg")
    return queries

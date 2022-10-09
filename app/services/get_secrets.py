import logging
from asyncpg import Pool, Record
from db.queries.queries import queries
from services.security import get_secret_key_hash

logger = logging.getLogger("app.api.v1.get_secret")

async def get_secret(secret_key: str, pool: Pool, salt: str) -> Record:
    secret_key_hash = get_secret_key_hash(secret_key, salt)

    async with pool.acquire() as conn:
        result: Record = await queries.get_secret(
            conn,
            secret_key = secret_key_hash,
        )
    return result


async def set_secret_expired(secret_key: str, pool: Pool, salt: str):
    secret_key_hash = get_secret_key_hash(secret_key, salt)
    async with pool.acquire() as conn:
        await queries.set_secret_status(
            conn,
            is_active = False,
            secret_key = secret_key_hash
        )
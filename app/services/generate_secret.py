import uuid
from asyncpg import Pool
from db.queries.queries import queries
from .security import get_secret_key_hash

async def create_secret(secret: str, secret_key: str, pool: Pool, salt: str):
    async with pool.acquire() as conn:
        await queries.create_secret(
            conn,
            id=uuid.uuid4(),
            secret = secret,
            secret_key = get_secret_key_hash(secret_key, salt)
        )
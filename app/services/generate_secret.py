import uuid
from asyncpg import Pool
from db.queries.queries import queries
from .security import get_secret_phrase_hash

async def create_secret(secret: str, secret_phrase: str, pool: Pool):
    async with pool.acquire() as conn:
        await queries.create_secret(
            conn,
            id=uuid.uuid4(),
            new_secret = secret,
            new_hash_secret_phrase = get_secret_phrase_hash(secret_phrase)
        )
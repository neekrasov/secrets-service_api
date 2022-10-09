import uuid
from asyncpg import Pool
from ..db.queries.queries import queries
from .security import get_secret_key_hash

async def create_secret(secret: str, secret_key: str, pool: Pool, salt: str):
    """
    This function allows you to create a secret in the database.
    
    
    Args:
        secret (str): Line with a secret phrase.
        secret_key (str): One-time key to access the secret phrase.
        pool (Pool): Postres connection pool.
        salt (str): Salt for hashing the secret key.
    """
    async with pool.acquire() as conn:
        await queries.create_secret(
            conn,
            id=uuid.uuid4(),
            secret = secret,
            secret_key = get_secret_key_hash(secret_key, salt)
        )
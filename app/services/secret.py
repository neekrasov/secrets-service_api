import uuid
from asyncpg import Pool, Record
from aiosql.queries import Queries

from .security import SecurityService


class SecretService:
    def __init__(
        self,
        pool: Pool,
        security_service: SecurityService,
        queries: Queries,
    ):
        self._pool = pool
        self._security = security_service
        self._queries = queries

    async def create_secret(self, secret: str, secret_key: str):
        """
        This function allows you to create a secret in the database.


        Args:
            secret (str): Line with a secret phrase.
            secret_key (str): One-time key to access the secret phrase.
            pool (Pool): Postres connection pool.
            salt (str): Salt for hashing the secret key.
        """
        async with self._pool.acquire() as conn:
            await self._queries.create_secret(
                conn,
                id=uuid.uuid4(),
                secret=secret,
                secret_key=self._security.get_secret_key_hash(secret_key),
            )

    async def get_secret(self, secret_key: str) -> Record:
        """
        This function allows you to get the secret from the database.

        Args:
            secret_key (str): One-time key to access the secret phrase.
            pool (Pool): Postres connection pool.
            salt (str): Salt for hashing the secret key.

        Returns:
            Record: A read-only representation of PostgreSQL row.
        """
        secret_key_hash = self._security.get_secret_key_hash(secret_key)

        async with self._pool.acquire() as conn:
            result: Record = await self._queries.get_secret(
                conn,
                secret_key=secret_key_hash,
            )
        return result

    async def set_secret_expired(self, secret_key: str):
        """
        This function allows you to change the status of a secret to inactive.

        Args:
            secret_key (str): One-time key to access the secret phrase.
            pool (Pool): Postres connection pool.
            salt (str): Salt for hashing the secret key.
        """
        secret_key_hash = self._security.get_secret_key_hash(secret_key)
        async with self._pool.acquire() as conn:
            await self._queries.set_secret_status(
                conn, is_active=False, secret_key=secret_key_hash
            )

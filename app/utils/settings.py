from dataclasses import dataclass
from aiohttp import web
import os
import pathlib
from dotenv import load_dotenv

@dataclass
class Settings():
    postgres_user: str = "postgres"
    postgres_password: str = ""
    postgres_host: str = "localhost"
    postgres_db: str = "postgres"
    postgres_port: str = "5432"
    hash_salt: str = ""
    logging_level: str = "DEBUG"
    title: str = "Secrets-service"
    descriprion: str = "Service for storing one-time secrets"
    postgres_driver = "asyncpg"
    
    @property
    def postgres_dsn(self) -> str:
        return f"postgres://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
    
    def read_env(self):
        load_dotenv(dotenv_path=pathlib.Path(__file__).parent.parent.parent / "dev.env")
        self.postgres_user = os.getenv("POSTGRES_USER")
        self.postgres_password = os.getenv("POSTGRES_PASSWORD")
        self.postgres_host = os.getenv("POSTGRES_HOST")
        self.postgres_db = os.getenv("POSTGRES_DB")
        self.postgres_port = os.getenv("POSTGRES_PORT")
        self.logging_level = os.getenv("LOGGING_LEVEL")
        self.hash_salt = os.getenv("HASH_SALT")
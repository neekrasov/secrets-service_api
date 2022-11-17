from dataclasses import dataclass, asdict
import os
import pathlib
from dotenv import load_dotenv


@dataclass
class Settings:
    postgres_user: str | None = "postgres"
    postgres_password: str | None = ""
    postgres_host: str | None = "localhost"
    postgres_db: str | None = "postgres"
    postgres_port: str | None = "5432"
    hash_salt: str | None = ""
    logging_level: str | None = "DEBUG"
    title: str | None = "Secrets-service"
    descriprion: str | None = "Service for storing one-time secrets"
    postgres_driver = "asyncpg"
    postgres_dsn: str | None = None

    def read_env(self):
        load_dotenv(dotenv_path=pathlib.Path(__file__).parent.parent.parent / "dev.env")
        self.postgres_user = os.getenv("POSTGRES_USER")
        self.postgres_password = os.getenv("POSTGRES_PASSWORD")
        self.postgres_host = os.getenv("POSTGRES_HOST")
        self.postgres_db = os.getenv("POSTGRES_DB")
        self.postgres_port = os.getenv("POSTGRES_PORT")
        self.logging_level = os.getenv("LOGGING_LEVEL")
        self.hash_salt = os.getenv("HASH_SALT")
        self.postgres_dsn = "postgres://{user}:{password}@{host}:{port}/{db}".format(
            user=self.postgres_user,
            password=self.postgres_password,
            host=self.postgres_host,
            port=self.postgres_port,
            db=self.postgres_db,
        )

    def get_dict(self):
        return asdict(self)

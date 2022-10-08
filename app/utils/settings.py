from dataclasses import dataclass

@dataclass
class Settings():
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_db: str
    postgres_port: str
    logging_level: str = "DEBUG"
    title: str = "Secrets-service"
    descriprion: str = "Service for storing one-time secrets"
    postgres_driver = "asyncpg"
    
    @property
    def postgres_dsn(self) -> str:
        return f"postgres://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
    
    
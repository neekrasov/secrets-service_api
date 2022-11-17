from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Configuration, Factory, Resource
from app.services import SecurityService, SecretService
from app.db.pool import init_pool, init_queries


class Container(DeclarativeContainer):

    wiring_config = WiringConfiguration(
        modules=["app.api.v1.generate_secret", "app.api.v1.get_secret"]
    )

    config = Configuration()

    pool = Resource(
        init_pool,
        dsn=config.postgres_dsn,
    )

    queries = Resource(
        init_queries,
    )

    security_service = Factory(
        SecurityService,
        salt=config.hash_salt,
    )

    secret_service = Factory(
        SecretService,
        pool=pool,
        security_service=security_service,
        queries=queries,
    )

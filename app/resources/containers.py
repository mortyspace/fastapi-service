from collections import deque

from dependency_injector import providers, containers

from .providers import (
    get_db_engine,
    get_db_connection,
    cleanup_db_connection,
    get_celery,
    get_redis,
)


class DBContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    connections = providers.Singleton(deque)
    engine = providers.Resource(
        get_db_engine,
        url=config.url,
        echo=config.echo,
        pool_size=config.pool_size.as_int(),
        max_overflow=config.max_overflow.as_int(),
        pool_timeout=config.pool_timeout.as_int(),
        connections=connections,
    )
    cleanup = providers.Coroutine(cleanup_db_connection, connections)
    connection = providers.Coroutine(get_db_connection, engine, connections)


class ResourcesContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    db = providers.Container(DBContainer, config=config.db)
    celery = providers.Resource(get_celery)
    redis = providers.Resource(get_redis, url=config.redis.url)

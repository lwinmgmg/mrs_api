# pylint: disable=too-many-arguments, too-many-positional-arguments
from urllib.parse import quote
from sqlalchemy.ext.asyncio import create_async_engine
from mrs_api.env.settings import get_settings

settings = get_settings()


def get_postgres_uri(
    host: str, port: int, user: str, password: str, db: str, statement_count: int = 1000
) -> str:
    user = quote(user)
    password = quote(password)
    db = quote(db)
    return (
        f"postgresql+asyncpg://{user}:{password}@{host}"
        f":{port}/{db}?prepared_statement_cache_size={statement_count}"
    )


engine = create_async_engine(
    get_postgres_uri(
        host=settings.postgres_host,
        port=settings.postgres_port,
        user=settings.postgres_user,
        password=settings.postgres_password,
        db=settings.postgres_db,
    ),
    echo=settings.debug,
)

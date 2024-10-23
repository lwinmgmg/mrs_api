from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # DB Related Config
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_user: str = "postgres"
    postgres_password: str = ""
    postgres_db: str = "mrs"
    debug: bool = False

    # Odoo Related Config
    odoo_url: str = "http://localhost:8069"
    odoo_user: str = "admin"
    odoo_password: str = ""
    odoo_db: str = ""
    odoo_key: str = "odoo"
    odoo_conn_count: int = 3

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return Settings()

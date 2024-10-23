from contextlib import asynccontextmanager
from fastapi import FastAPI
from mrs_api.env.settings import get_settings
from mrs_api.services.odoo import Odoo

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    odoo = Odoo(
        app=app,
        key=settings.odoo_key,
        url=settings.odoo_url,
        db=settings.odoo_db,
        username=settings.odoo_user,
        password=settings.odoo_password,
        conn_count=settings.odoo_conn_count,
    )
    odoo.on_startup()
    yield
    odoo.on_shutdown()
    # Clean up the ML models and release the resources

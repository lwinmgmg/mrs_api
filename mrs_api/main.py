from fastapi import FastAPI, Depends
from .services.session import async_session
from .api.router import router

app = FastAPI()

app.include_router(router=router, prefix="/api")

@app.get("/")
async def get():
    return {
        "hello": "world"
    }

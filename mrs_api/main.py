from fastapi import FastAPI
from .api.router import router

app = FastAPI()

app.include_router(router=router, prefix="/api")


@app.get("/")
async def get():
    return {"hello": "world"}

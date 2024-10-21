from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.router import router, acl_router

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=router, prefix="/api")
app.include_router(router=acl_router, prefix="/api/acl")


@app.get("/")
async def get():
    return {"hello": "world"}

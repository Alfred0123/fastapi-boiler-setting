import os
from typing import Union
from fastapi import FastAPI
from . import config
from .adapter.controller import users

app = FastAPI()

app.include_router(
    users.router,
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@app.get("/")
def read_root():
    c = config.get_settings()
    env = os.getenv("ENVIRONMENT")
    print(f"env: {env}")
    return {"Hello": "World2", "app_name": c.app_name}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

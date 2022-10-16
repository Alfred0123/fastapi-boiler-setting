import os
from typing import Union
from fastapi import FastAPI
from . import config
from .adapter.controller import users
from loguru import logger

app = FastAPI()

app.include_router(
    users.router,
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@app.get("/ping")
def ping():
    c = config.get_settings()
    env = os.getenv("ENVIRONMENT")
    # print(f"env: {env}")
    logger.debug("env: {env}", env=env)
    return {"message": "pong", "admin_email": c.admin_email}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

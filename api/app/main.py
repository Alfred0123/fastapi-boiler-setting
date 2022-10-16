from typing import Union
from fastapi import FastAPI
from . import config

app = FastAPI()


@app.get("/")
def read_root():
    c = config.get_settings()
    return {"Hello": "World2", "app_name": c.app_name}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

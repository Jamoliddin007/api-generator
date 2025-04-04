from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    title: str
    views: int

items = []

@app.post("/items/")
def create_item(item: Item):
    items.append(item)
    return item

@app.get("/items/")
def get_items():
    return items

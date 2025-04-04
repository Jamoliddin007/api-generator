from typing import List
from models.user_input import FieldDefinition

def map_type(t: str) -> str:
    return {
        "string": "str",
        "integer": "int",
        "boolean": "bool",
        "float": "float"
    }.get(t, "str")  

def generate_fastapi_code(fields: List[FieldDefinition]) -> str:
    model_fields = "\n    ".join(
        f"{field.name}: {map_type(field.type)}" for field in fields
    )

    code = f"""from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    {model_fields}

items = []

@app.post("/items/")
def create_item(item: Item):
    items.append(item)
    return item

@app.get("/items/")
def get_items():
    return items
"""
    return code

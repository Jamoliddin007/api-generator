from pydantic import BaseModel
from datetime import datetime
from typing import List, Literal

class FieldOut(BaseModel):
    name: str
    type: str

    class Config:
        from_attributes = True

class ProjectDetailOut(BaseModel):
    name: str
    slug: str
    file_path: str
    created_at: datetime
    fields: List[FieldOut]

    class Config:
        from_attributes = True


class NewField(BaseModel):
    name: str
    type: Literal["string", "integer", "boolean", "float"]


class ProjectOut(BaseModel):
    name: str
    slug: str
    file_path: str
    created_at: datetime

    class Config:
        from_attributes = True

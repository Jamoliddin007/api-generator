from pydantic import BaseModel
from typing import Literal, List

class FieldDefinition (BaseModel):
    name: str
    type: Literal["string", "integer", "boolean", "float"]


class APIGenerateRequest(BaseModel):
    project_name: str
    fields: List[FieldDefinition]


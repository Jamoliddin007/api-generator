from pydantic import BaseModel
from datetime import datetime

class ProjectOut(BaseModel):
    name: str
    slug: str
    file_path: str
    created_at: datetime

    class Config:
        from_attributes = True

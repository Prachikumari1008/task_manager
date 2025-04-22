from pydantic import BaseModel
from datetime import datetime

class TaskCreate(BaseModel):
    name: str

class TaskOut(BaseModel):
    id: int
    name: str
    status: str
    created_at: datetime

from pydantic import BaseModel

class VisitView(BaseModel):
    id: int
    name: str
    state: str

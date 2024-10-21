from pydantic import BaseModel
from mrs_api.services.base import Eng


class TitleView(BaseModel):
    id: int
    name: Eng

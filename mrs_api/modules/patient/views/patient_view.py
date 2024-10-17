from typing import Optional
from pydantic import BaseModel


class PatientView(BaseModel):
    id: int
    name: str
    patient_code: str
    email: Optional[str]
    phone: Optional[str]
    mobile: Optional[str]

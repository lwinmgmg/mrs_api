from typing import Optional, Annotated
from datetime import date
from pydantic import BaseModel, Field
from mrs_api.modules.address.views.address_view import AddressInfo
from .title_view import TitleView


class PatientInfoView(BaseModel):
    id: int
    name: str
    patient_code: str


class PatientContactInfo(BaseModel):
    email: Optional[str]
    phone: Optional[str]
    mobile: Optional[str]


class PatientPersonalInfo(BaseModel):
    date_of_birth: Optional[date]
    gender: Optional[str]
    title: Annotated[Optional[TitleView], Field(validation_alias="partner_title")]


class PatientView(
    PatientInfoView, PatientContactInfo, PatientPersonalInfo, AddressInfo
):
    pass


class PatientCreateView(BaseModel):
    name: str
    is_patient: Optional[bool] = True
    email: str
    phone: Optional[str] = None
    mobile: Optional[str] = None
    date_of_birth: Optional[date] = None
    gender: Optional[str] = None
    street: Optional[str] = None
    street2: Optional[str] = None
    zip: Optional[str] = None
    city: Optional[str] = None
    country_id: int
    state_id: Optional[int] = None


class PatientUpdateView(BaseModel):
    name: Optional[str] = None
    is_patient: Optional[bool] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    mobile: Optional[str] = None
    date_of_birth: Optional[date] = None
    gender: Optional[str] = None
    street: Optional[str] = None
    street2: Optional[str] = None
    zip: Optional[str] = None
    city: Optional[str] = None
    country_id: Optional[int] = None
    state_id: Optional[int] = None

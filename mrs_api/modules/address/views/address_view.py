from typing import Optional
from pydantic import BaseModel
from mrs_api.services.base import CommonView, Eng


class StateInfo(CommonView):
    pass


class CountryInfo(CommonView):
    name: Optional[Eng]


class AddressInfo(BaseModel):
    street: Optional[str]
    street2: Optional[str]
    zip: Optional[str]
    city: Optional[str]
    country: Optional[CountryInfo]
    state: Optional[StateInfo]

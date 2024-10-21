from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, Integer, String, ForeignKey
from .country_model import CountryModel
from .state_model import StateModel


class AddressInfo:
    street: Mapped[str] = Column(String)
    street2: Mapped[str] = Column(String)
    zip: Mapped[str] = Column(String)
    city: Mapped[str] = Column(String)

    country_id: Mapped[int] = Column(Integer, ForeignKey(CountryModel.id))
    state_id: Mapped[int] = Column(Integer, ForeignKey(StateModel.id))

    @declared_attr
    def country(self):
        return relationship(CountryModel, foreign_keys=[self.country_id])

    @declared_attr
    def state(self):
        return relationship(StateModel, foreign_keys=[self.state_id])

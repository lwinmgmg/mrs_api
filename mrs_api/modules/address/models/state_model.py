# pylint: disable=unsubscriptable-object
from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped
from mrs_api.services.base import Base, Model


class StateModel(Model, Base):
    __tablename__ = "res_country_state"

    name: Mapped[str] = Column(String)

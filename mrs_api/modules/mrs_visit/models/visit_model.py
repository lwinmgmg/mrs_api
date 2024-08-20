from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped
from mrs_api.services.base import Base, Model


class VisitModel(Model, Base):
    __tablename__ = "mrs_visit"

    name: Mapped[str] = Column(String)
    state: Mapped[str] = Column(String)

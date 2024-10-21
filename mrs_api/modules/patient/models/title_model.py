from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped
from mrs_api.services.base import Base, Model


class TitleModel(Model, Base):
    __tablename__ = "res_partner_title"

    name: Mapped[str] = Column(String)

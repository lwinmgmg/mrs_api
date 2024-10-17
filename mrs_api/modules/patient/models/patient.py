from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped
from mrs_api.services.base import Base, Model


class PatientModel(Model, Base):
    __tablename__ = "res_partner"

    name: Mapped[str] = Column(String)
    patient_code: Mapped[str] = Column(String)
    email: Mapped[str] = Column(String)
    phone: Mapped[str] = Column(String)
    mobile: Mapped[str] = Column(String)

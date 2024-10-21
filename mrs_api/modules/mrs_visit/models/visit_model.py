from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from mrs_api.services.base import Base, Model
from mrs_api.modules.patient.models.patient_model import PatientModel


class VisitModel(Model, Base):
    __tablename__ = "mrs_visit"

    name: Mapped[str] = Column(String)
    state: Mapped[str] = Column(String)
    patient_id: Mapped[int] = Column(Integer, ForeignKey(PatientModel.id))
    patient: Mapped[PatientModel] = relationship(
        PatientModel, foreign_keys=[patient_id]
    )

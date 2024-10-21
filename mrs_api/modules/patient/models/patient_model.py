from typing import Self
from datetime import date
from sqlalchemy import Column, String, Integer, ForeignKey, Date, select
from sqlalchemy.orm import Mapped, relationship, joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from mrs_api.services.base import Base, Model
from mrs_api.modules.address.models.address_model import AddressInfo
from .title_model import TitleModel


class PatientModel(Model, Base, AddressInfo):
    __tablename__ = "res_partner"

    name: Mapped[str] = Column(String)
    patient_code: Mapped[str] = Column(String)
    email: Mapped[str] = Column(String)
    phone: Mapped[str] = Column(String)
    mobile: Mapped[str] = Column(String)
    gender: Mapped[str] = Column(String)
    date_of_birth: Mapped[date] = Column(Date)

    title: Mapped[int] = Column(Integer, ForeignKey(TitleModel.id))
    partner_title: Mapped[TitleModel] = relationship(TitleModel, foreign_keys=[title])

    @classmethod
    async def detail_by_user_code(cls, user_code: str, session: AsyncSession) -> Self:
        stmt = (
            select(PatientModel)
            .where(cls.patient_code == user_code)
            .order_by(PatientModel.id)
            .options(
                joinedload(PatientModel.partner_title),
                joinedload(PatientModel.state),
                joinedload(PatientModel.country),
            )
        )
        results = await session.execute(stmt)
        return results.scalar()

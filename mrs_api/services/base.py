from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy import Column, Integer, DateTime
from pydantic import BaseModel


class Base(DeclarativeBase):
    pass


class Model:
    id: Mapped[int] = Column(Integer, primary_key=True)
    create_date: Mapped[datetime] = Column(DateTime)
    write_date: Mapped[datetime] = Column(DateTime)


class CommonView(BaseModel):
    id: int
    name: str


class Eng(BaseModel):
    en_US: str

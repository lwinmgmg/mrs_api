from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy import Column, Integer, DateTime


class Base(DeclarativeBase):
    pass


class Model:
    id: Mapped[int] = Column(Integer, primary_key=True)
    create_date: Mapped[datetime] = Column(DateTime)
    write_date: Mapped[datetime] = Column(DateTime)

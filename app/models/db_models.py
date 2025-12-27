from datetime import datetime
from os import name
from tkinter import EventType

from fastapi import FastAPI
from sqlalchemy import DateTime, String, Float, func, Enum as SQLEnum
from app.core.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.enums import *

class PlacesOrm(Base):
    __tablename__ = "places"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[PlacesTypes] = mapped_column(SQLEnum(PlacesTypes, name="places_type_enum"), nullable=False)
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(1000))
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

class EventOrm(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[EventsTypes] = mapped_column(SQLEnum(EventsTypes, name="event_type_enum"), nullable=False)
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(1000))
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)
    date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)


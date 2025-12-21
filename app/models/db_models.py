from datetime import datetime

from sqlalchemy import DateTime, String, Float, func
from app.core.db_core import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class PlacesOrm(Base):
    __tablename__ = "places"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(1000))
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

class EventOrm(PlacesOrm):
    __tablename__ = "events"

    date: Mapped[datetime] = mapped_column(DateTime, nullable=False)

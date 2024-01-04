from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .devices import DeviceModel


class RecordModel(Base):
    __tablename__ = "records"

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True,
    )
    co2: Mapped[int] = mapped_column(nullable=False)
    hum: Mapped[float] = mapped_column(nullable=False)
    temp: Mapped[float] = mapped_column(nullable=False)
    lux: Mapped[float] = mapped_column(nullable=False)
    noise: Mapped[float] = mapped_column(nullable=False)
    timestamp: Mapped[datetime]

    device_id: Mapped[int] = mapped_column(ForeignKey("devices.id"))
    device: Mapped["DeviceModel"] = relationship(back_populates="records")

    __table_args__ = (UniqueConstraint('timestamp', 'device_id', name='_record_uc'),)

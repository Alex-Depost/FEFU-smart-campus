from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

import enums
from .base import Base

if TYPE_CHECKING:
    from .devices import DeviceModel


class IncidentModel(Base):
    __tablename__ = "incidents"

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True,
    )
    level: Mapped[enums.IncidentLevel]
    type: Mapped[enums.IncidentType]
    value: Mapped[float]
    status: Mapped[enums.IncidentStatus]
    timestamp: Mapped[datetime]

    device_id: Mapped[int] = mapped_column(ForeignKey("devices.id"))
    device: Mapped["DeviceModel"] = relationship(back_populates="incidents")

    __table_args__ = (UniqueConstraint('timestamp', 'type', 'device_id', name='_incident_uc'),)

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .incidents import IncidentModel
    from .audiences import AudienceModel
    from .records import RecordModel


class DeviceModel(Base):
    __tablename__ = "devices"

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True,
    )
    name: Mapped[str] = mapped_column(
        String(length=100),
    )

    audience_id: Mapped[int] = mapped_column(ForeignKey("audiences.id"))
    audience: Mapped["AudienceModel"] = relationship(back_populates="devices")
    records: Mapped[List["RecordModel"]] = relationship(back_populates="device")
    incidents: Mapped[List["IncidentModel"]] = relationship(back_populates="device")


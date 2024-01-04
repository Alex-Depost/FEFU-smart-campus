from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .devices import DeviceModel


class AudienceModel(Base):
    __tablename__ = "audiences"

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True,
    )
    name: Mapped[str] = mapped_column(
        String(length=100), unique=True,
    )
    location: Mapped[str]
    floor_space: Mapped[int]
    voltage: Mapped[int]

    devices: Mapped[List["DeviceModel"]] = relationship(back_populates="audience")

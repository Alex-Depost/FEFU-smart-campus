from sqlalchemy.orm import Mapped, mapped_column

import enums
from .base import Base


class NormalValueModel(Base):
    __tablename__ = "normal_values"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[enums.IncidentType] = mapped_column(unique=True, nullable=False)
    min: Mapped[int] = mapped_column(nullable=False)
    max: Mapped[int] = mapped_column(nullable=False)


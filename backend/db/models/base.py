import enum

import sqlalchemy
from sqlalchemy.orm import DeclarativeBase
from db.meta import meta


class Base(DeclarativeBase):
    """Base for all models."""

    type_annotation_map = {
        enum.Enum: sqlalchemy.Enum(enum.Enum)
    }
    metadata = meta

from typing import List

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

import enums
from db.dependencies import get_db_session
from db.models.normal_values import NormalValueModel


class NormalValuesDAO:
    """Class for accessing normal values table."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create(
            self,
            name: enums.IncidentType,
            min_value: int,
            max_value: int,
    ) -> None:
        """
        Create normal values in database.

        :param name: name of a normal value.
        :param min_value: min value of indicator.
        :param max_value: max value of indicator.
        """
        await self.session.execute(insert(NormalValueModel).values(
            name=name, min=min_value, max=max_value,
        ).on_conflict_do_nothing())

    async def get_all(self) -> List[NormalValueModel]:
        """
        Get all normal values models.

        :return: stream of normal values.
        """
        statement = select(NormalValueModel).order_by(NormalValueModel.id)
        raw_devices = await self.session.execute(statement)
        return list(raw_devices.scalars().fetchall())

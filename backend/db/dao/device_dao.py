from typing import List, Optional

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from db.dependencies import get_db_session
from db.models.devices import DeviceModel


class DeviceDAO:
    """Class for accessing devices table."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create(
            self,
            id: int,
            name: str,
            audience_id: int,
    ) -> None:
        """
        Create device in database.

        :param id: id of a device.
        :param name: name of a device.
        :param audience_id: id of an audience.
        """
        await self.session.execute(insert(DeviceModel).values(
            id=id, name=name, audience_id=audience_id,
        ).on_conflict_do_update(
            index_elements=['id'],
            set_=dict(name=name, audience_id=audience_id),
        ))

    async def get_all(self) -> List[DeviceModel]:
        """
        Get all device models.

        :return: stream of devices.
        """
        statement = select(DeviceModel)
        raw_devices = await self.session.execute(statement)
        return list(raw_devices.scalars().fetchall())

    async def filter(
            self,
            id: Optional[int] = None,
            name: Optional[str] = None,
    ) -> List[DeviceModel]:
        """
        Get specific device model by name.

        :param id: id of a device.
        :param name: name of a device.
        :return: device model.
        """
        statement = select(DeviceModel)
        if id:
            statement = statement.where(DeviceModel.id == id)
        if name:
            statement = statement.where(DeviceModel.name == name)
        rows = await self.session.execute(statement)
        return list(rows.scalars().fetchall())

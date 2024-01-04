from datetime import datetime, timedelta
from random import randint
from typing import List, Optional

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload, contains_eager, aliased

from db.dependencies import get_db_session
from db.models.audiences import AudienceModel
from db.models.devices import DeviceModel
from db.models.records import RecordModel


class AudienceDAO:
    """Class for accessing audiences table."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create(
            self,
            name: str,
            location: str,
    ) -> int:
        """
        Create audience in database.

        :param name: name of an audience.
        :param location: location of audience.
        """
        result = await self.session.execute(
            insert(AudienceModel).values(
                name=name,
                location=location,
                floor_space=randint(50, 100),
                voltage=randint(5, 10)
            ).on_conflict_do_update(
                index_elements=['name'],
                set_=dict(name=name),
            ).returning(AudienceModel.id)
        )
        audience_id = result.scalars().one()
        return audience_id

    async def get_all(self, limit: Optional[int] = None, offset: Optional[int] = None) -> List[AudienceModel]:
        """
        Get all audience models with limit/offset pagination.

        :param limit: limit of audiences.
        :param offset: offset of audiences.
        :return: stream of audiences.
        """
        statement = select(AudienceModel).where(AudienceModel.devices.any())
        if limit:
            statement = statement.limit(limit)
        if offset:
            statement = statement.offset(offset)
        raw_devices = await self.session.execute(statement)
        return list(raw_devices.scalars().fetchall())

    async def get_by_id(self, audience_id: int) -> AudienceModel:
        """Get audience with devices and records of devices."""
        five_minutes_ago = datetime.now() - timedelta(minutes=30)
        subquery = select(RecordModel).filter(RecordModel.timestamp > five_minutes_ago).subquery()
        alias = aliased(RecordModel, subquery)

        results = await self.session.execute(
            select(AudienceModel)
            .outerjoin(AudienceModel.devices)
            .outerjoin(DeviceModel.records.of_type(alias))
            .filter(AudienceModel.id == audience_id)
            .options(
                joinedload(AudienceModel.devices)
                .contains_eager(DeviceModel.records.of_type(alias))
            )
        )
        return results.scalars().first()

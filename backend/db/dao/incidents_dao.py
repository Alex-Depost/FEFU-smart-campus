from datetime import datetime
from typing import List

from fastapi import Depends
from sqlalchemy import select, func, update
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

import enums
from db.dependencies import get_db_session
from db.models.devices import DeviceModel
from db.models.incidents import IncidentModel
from enums import IncidentLevel


class IncidentDAO:
    """Class for accessing incidents table."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create(
            self,
            level: IncidentLevel,
            incident_type: enums.IncidentType,
            value: float,
            status: enums.IncidentStatus,
            timestamp: datetime,
            device_id: int,
    ) -> None:
        """
        Create device in database.


        """
        await self.session.execute(insert(IncidentModel).values(
            level=level, value=value, status=status, timestamp=timestamp, device_id=device_id, type=incident_type,
        ).on_conflict_do_nothing())

    async def get_all(self) -> List[IncidentModel]:
        subquery = select(
            IncidentModel.device_id,
            IncidentModel.type,
            func.max(IncidentModel.timestamp).label('max_timestamp')
        ).group_by(IncidentModel.device_id, IncidentModel.type).subquery()
        query = select(IncidentModel).options(
            joinedload(IncidentModel.device).joinedload(DeviceModel.audience)
        ).join(
            subquery,
            (IncidentModel.device_id == subquery.c.device_id) &
            (IncidentModel.type == subquery.c.type) &
            (IncidentModel.timestamp == subquery.c.max_timestamp)
        )
        results = await self.session.execute(query)
        return list(results.scalars().all())

    async def update_status(self, incident_id: int, status: enums.IncidentStatus):
        await self.session.execute(update(IncidentModel).where(IncidentModel.id == incident_id).values(status=status))

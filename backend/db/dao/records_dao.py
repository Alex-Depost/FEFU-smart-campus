from datetime import datetime, timedelta

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from db.dependencies import get_db_session
from db.models.records import RecordModel


class RecordDAO:
    """Class for accessing records table."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create(
            self,
            co2: int,
            hum: float,
            temp: float,
            lux: float,
            noise: float,
            timestamp: datetime,
            device_id: int,
    ) -> None:
        """
        Create record in database.
        """
        await self.session.execute(insert(RecordModel).values(
            co2=co2, hum=hum, temp=temp, lux=lux, noise=noise, timestamp=timestamp, device_id=device_id,
        ).on_conflict_do_nothing())

    async def get_last_records(self):
        """Get records in last 5 minutes."""

        five_minutes_ago = datetime.now() - timedelta(minutes=5)
        results = await self.session.execute(select(RecordModel).filter(RecordModel.timestamp > five_minutes_ago))
        return list(results.scalars().all())

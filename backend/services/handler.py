import json
from random import randint
from typing import List, Dict, Any, Union

import aiohttp
from datetime import datetime, timedelta

import enums
from db.dao.audience_dao import AudienceDAO
from db.dao.device_dao import DeviceDAO
from db.dao.incidents_dao import IncidentDAO
from db.dao.normal_values_dao import NormalValuesDAO
from db.dao.records_dao import RecordDAO
from db.dependencies import get_db_session_manager
from schema import Record

ALL_OBJ_URL = "https://pandora.dvfu.ru/objects/get_objects"
REC_URL = "https://pandora.dvfu.ru/records/decoded_payloadss"

headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}


async def get_objects() -> Dict[str, Any]:
    async with aiohttp.ClientSession() as session:
        async with session.get(ALL_OBJ_URL, headers=headers) as response:
            return await response.json(content_type=None)


async def get_records(current_time: datetime, devices: List[int]):
    start_time = str(current_time - timedelta(minutes=10))
    end_time = str(current_time)

    device_id = ','.join(map(str, devices))
    params = {'start_time': start_time, 'end_time': end_time, 'device_id': device_id}
    async with aiohttp.ClientSession() as session:
        async with session.get(REC_URL, params=params, headers=headers) as response:
            return (await response.json())["data"]


async def add_normal_values():
    async with get_db_session_manager() as session:
        normal_value_dao = NormalValuesDAO(session)

        await normal_value_dao.create(name=enums.IncidentType.TEMP, min_value=18, max_value=28)
        await normal_value_dao.create(name=enums.IncidentType.CO2, min_value=600, max_value=1000)
        await normal_value_dao.create(name=enums.IncidentType.HUM, min_value=30, max_value=60)
        await normal_value_dao.create(name=enums.IncidentType.LUX, min_value=0, max_value=300)
        await normal_value_dao.create(name=enums.IncidentType.NOISE, min_value=0, max_value=55)


# async def update_audiences():
#     objects = await get_objects()
#     for audience_name, data in objects.items():
#         async with get_db_session_manager() as session:
#             audience_dao = AudienceDAO(session)
#             if data["parents"]:
#                 audience_id = await audience_dao.create(
#                     name=audience_name,
#                     location=data["parents"][0],
#                 )
#
#         devices = data["devices"]
#         if devices != "Have not devices":
#             await update_devices(audience_id=audience_id, devices=devices)


async def update_devices(audience_id: int, devices: List[Dict[str, Any]]):
    async with get_db_session_manager() as session:
        device_dao = DeviceDAO(session)

        for device in devices:
            await device_dao.create(
                id=device["device_id"],
                name=device["device_name"],
                audience_id=audience_id
            )


async def check_incidents():
    async with get_db_session_manager() as session:
        normal_value_dao = NormalValuesDAO(session)
        record_dao = RecordDAO(session)

        normal_values = await normal_value_dao.get_all()
        records = await record_dao.get_last_records()

    for record in records:
        record_data = Record.model_validate(record).model_dump()
        async with get_db_session_manager() as session:
            incident_dao = IncidentDAO(session)
            for normal_value in normal_values:
                param_value = record_data[normal_value.name.value]
                if param_value > normal_value.max or param_value < normal_value.min:
                    await incident_dao.create(
                        device_id=record.device_id,
                        level=enums.IncidentLevel.WARNING,
                        status=enums.IncidentStatus.ACTIVE,
                        timestamp=record.timestamp,
                        value=param_value,
                        incident_type=normal_value.name,
                    )


# async def get_last_records():
#     async with get_db_session_manager() as session:
#         device_dao = DeviceDAO(session)
#
#         devices = await device_dao.get_all()
#         records = await get_records(current_time=datetime.now(), devices=[device.id for device in devices])
#
#     for device_id, data in records.items():
#         device_id = int(device_id)
#         if data["records"]:
#             record = data["records"][-1]
#
#             record_data = json.loads(record["value"].replace("\'", "\""))
#             timestamp = datetime.strptime(record["created"], '%Y-%m-%d %H:%M:%S')
#
#             async with get_db_session_manager() as session:
#                 dao = RecordDAO(session)
#
#                 await dao.create(
#                     device_id=device_id,
#                     co2=record_data["co2"],
#                     hum=record_data["hum"],
#                     lux=record_data["lux"],
#                     noise=record_data["noise"],
#                     temp=record_data["temp"],
#                     timestamp=timestamp,
#                 )

async def get_last_records():
    async with get_db_session_manager() as session:
        device_dao = DeviceDAO(session)

        devices = await device_dao.get_all()

    for device in devices:

        timestamp = datetime.now() + timedelta(minutes=randint(0, 2), seconds=randint(0, 59))

        async with get_db_session_manager() as session:
            dao = RecordDAO(session)

            await dao.create(
                device_id=device.id,
                co2=randint(550, 1050),
                hum=randint(25, 65),
                lux=randint(0, 320),
                noise=randint(0, 57),
                temp=randint(16, 29),
                timestamp=timestamp,
            )

from datetime import datetime
from typing import List
from pydantic import BaseModel, Field, ConfigDict
import enums


class Device(BaseModel):
    id: int
    name: str


class Audience(BaseModel):
    id: int
    name: str
    location: str
    floor_space: int
    voltage: int


class IncidentAudience(BaseModel):
    id: int
    name: str


class IncidentDevice(BaseModel):
    id: int
    name: str
    audience: IncidentAudience


class Incident(BaseModel):
    id: int
    type: enums.IncidentType
    level: enums.IncidentLevel
    status: enums.IncidentStatus
    value: float
    timestamp: datetime
    device: IncidentDevice


class NormalValue(BaseModel):
    id: int
    name: enums.IncidentType
    min: int
    max: int


class Record(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    co2: int
    hum: float
    temp: float
    lux: float
    noise: float
    timestamp: datetime


class DeviceDetail(Device):
    records: List[Record]


class AudienceDetail(Audience):
    devices: List[DeviceDetail]

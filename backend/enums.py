from enum import Enum


class IncidentStatus(Enum):
    ACTIVE = "active"
    FIXING = "fixing"
    FIXED = "fixed"


class IncidentLevel(Enum):
    WARNING = "warning"
    CRITICAL = "critical"


class IncidentType(Enum):
    CO2 = "co2"
    HUM = "hum"
    LUX = "lux"
    TEMP = "temp"
    NOISE = "noise"

from typing import List, Optional

import uvicorn
from fastapi import FastAPI, Depends, Body
from starlette.middleware.cors import CORSMiddleware

import enums
from db.dao.audience_dao import AudienceDAO
from db.dao.device_dao import DeviceDAO
from db.dao.incidents_dao import IncidentDAO
from db.dao.normal_values_dao import NormalValuesDAO
from db.models.audiences import AudienceModel
from db.models.devices import DeviceModel
from db.models.incidents import IncidentModel
from db.models.normal_values import NormalValueModel
from lifespan import lifespan
from schema import Device, Incident, NormalValue, Audience, AudienceDetail

app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/audiences", response_model=List[Audience])
async def audiences(
        dao: AudienceDAO = Depends(),
) -> List[AudienceModel]:
    """Get all audiences."""
    return await dao.get_all()


@app.get("/audiences/{audience_id}", response_model=Optional[AudienceDetail])
async def audience_detail(
        audience_id: int,
        dao: AudienceDAO = Depends(),
) -> Optional[AudienceModel]:
    """Get detail info about audience."""
    audience = await dao.get_by_id(audience_id)
    return audience


@app.get("/devices", response_model=List[Device])
async def devices(
        dao: DeviceDAO = Depends(),
) -> List[DeviceModel]:
    """Get all devices."""
    return await dao.get_all()


@app.get("/incidents", response_model=List[Incident])
async def incidents(
        dao: IncidentDAO = Depends(),
) -> List[IncidentModel]:
    """Get all incidents."""
    return await dao.get_all()


@app.get("/normal_values", response_model=List[NormalValue])
async def normal_values(
        dao: NormalValuesDAO = Depends(),
) -> List[NormalValueModel]:
    """Get all normal values."""
    return await dao.get_all()


@app.patch("/incidents/{incident_id}")
async def change_status(
        incident_id: int,
        status: enums.IncidentStatus = Body(embed=True),
        dao: IncidentDAO = Depends(),
) -> None:
    """Change status of incident."""
    await dao.update_status(incident_id=incident_id, status=status)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

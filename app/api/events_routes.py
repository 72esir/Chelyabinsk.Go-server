from fastapi import APIRouter

from app.core.db_core import SessionDep
from app.schemas.schemas import EventAdd
from app.services import events_service

router = APIRouter(prefix="/events", tags=["Events"])

@router.post("/")
async def add_event(s: SessionDep, payload: EventAdd):
    result = await events_service.add_event(s, payload)
    return {
        "success" : True,
        "data" : result
    }

@router.get("/")
async def get_all_events(s: SessionDep):
    result = await events_service.get_all_events(s)
    return {
        "success" : True,
        "data" : result
    }

@router.get(f"/{id}")
async def get_event_by_id(s: SessionDep, id: int):
    result = await events_service.get_event_by_id(s, id)
    return {
        "success" : True,
        "data" : result
    }
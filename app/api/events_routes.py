from datetime import datetime
from fastapi import APIRouter, File, Form, Request, UploadFile

from app.core.db_core import SessionDep
from app.models.enums import EventsTypes
from app.schemas.schemas import EventAdd
from app.services import events_service
from app.services.uploads_service import save_upload_image

router = APIRouter(prefix="/events", tags=["Events"])

@router.post("/")
async def add_event(
    request: Request,
    s: SessionDep,
    type: EventsTypes = Form(...),
    title: str = Form(...),
    price: str = Form(...),
    description: str = Form(...),
    longitude: float = Form(...),
    latitude: float = Form(...),
    date: datetime = Form(...),
    image: UploadFile | None = File(None),
):
    image_url = None
    if image is not None:
        image_url, _ = save_upload_image(request, image)
    payload = EventAdd(
        type=type,
        title=title,
        price=price,
        description=description,
        longitude=longitude,
        latitude=latitude,
        date=date,
        image_url=image_url,
    )
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

@router.get("/id/{event_id}")
async def get_event_by_id(s: SessionDep, event_id: int):
    result = await events_service.get_event_by_id(s, event_id)
    return {
        "success" : True,
        "data" : result
    }

@router.get("/type/{event_type}")
async def get_events_by_type(s: SessionDep, event_type: EventsTypes):
    result = await events_service.get_events_by_type(s, event_type)
    return {
        "success" : True,
        "data" : result
    }

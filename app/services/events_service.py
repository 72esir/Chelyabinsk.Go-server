from typing import List, Sequence

from fastapi import HTTPException, status
from sqlalchemy import select
from app.core.db_core import SessionDep
from app.models.db_models import EventOrm
from app.models.enums import EventsTypes
from app.schemas.schemas import Event, EventAdd

def get_events_dto(events: Sequence[EventOrm]) -> List[Event]:
    events_dto = []
    for event in events:
        events_dto.append(Event(
            id=event.id,
        type = event.type,
        title=event.title,
        price=event.price,
        description=event.description,
        image_url=event.image_url,
        longitude=event.longitude,
        latitude=event.latitude,
        date=event.date,
            created_at=event.created_at,
            updated_at=event.updated_at,
        ))
    return events_dto

async def add_event(s: SessionDep, payload: EventAdd):
    new_event = EventOrm(
        type=payload.type,
        title=payload.title,
        price=payload.price,
        description=payload.description,
        image_url=payload.image_url,
        date=payload.date,
        latitude=payload.latitude,
        longitude=payload.longitude,
    )

    s.add(new_event)
    await s.commit()
    await s.refresh(new_event)

    return new_event.id

async def get_all_events(s: SessionDep):
    query = select(EventOrm)
    res = await s.execute(query)
    events = res.scalars().all()
    events_dto = get_events_dto(events)
    return events_dto

async def get_event_by_id(s: SessionDep, event_id: int):
    query = select(EventOrm).filter(EventOrm.id == event_id)
    res = await s.execute(query)
    event = res.scalar_one_or_none()
    
    if event:
        event_dto = get_events_dto([event])
        return event_dto

    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="event by id not found"
        )

async def get_events_by_type(s: SessionDep, type: EventsTypes):
    query = select(EventOrm).filter(EventOrm.type == type)
    res = await s.execute(query)
    events = res.scalars().all()

    if not events:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="events by type not found"
        )
    
    events_dto = get_events_dto(events)
    return events_dto

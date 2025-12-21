from typing import List, Sequence

from fastapi import HTTPException, status
from sqlalchemy import select
from app.core.db_core import SessionDep
from app.models.db_models import EventOrm
from app.schemas.schemas import Event, EventAdd

def get_events_dto(events: Sequence[EventOrm]) -> List[Event]:
    events_dto = []
    for event in events:
        events_dto.append(Event(
            id=event.id,
            title=event.title,
            description=event.description,
            longitude=event.longitude,
            latitude=event.latitude,
            date=event.date,
            created_at=event.created_at,
            updated_ad=event.updated_at,
        ))
    return events_dto

async def add_event(s: SessionDep, payload: EventAdd):
    new_event = EventOrm(
        title=payload.title,
        description=payload.description,
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
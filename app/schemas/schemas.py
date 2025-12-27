from datetime import datetime
from pydantic import BaseModel

from app.models.enums import * 

class PlaceAdd(BaseModel):
    type: PlacesTypes
    title: str
    description: str
    longitude: float
    latitude: float

class EventAdd(BaseModel):
    type: EventsTypes
    title: str
    description: str
    longitude: float
    latitude: float
    date: datetime

class Place(PlaceAdd):
    id: int
    created_at: datetime
    updated_ad: datetime

class Event(EventAdd): 
    id: int
    created_at: datetime
    updated_ad: datetime
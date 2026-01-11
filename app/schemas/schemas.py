from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from app.models.enums import * 

class PlaceAdd(BaseModel):
    type: PlacesTypes
    title: str
    address: str
    description: str
    image_url: Optional[str] = None
    longitude: float
    latitude: float

class EventAdd(BaseModel):
    type: EventsTypes
    title: str
    location: str
    price: str
    description: str
    image_url: Optional[str] = None
    longitude: float
    latitude: float
    date: datetime

class Place(PlaceAdd):
    id: int
    created_at: datetime
    updated_at: datetime

class Event(EventAdd): 
    id: int
    created_at: datetime
    updated_at: datetime

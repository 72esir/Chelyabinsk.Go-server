from datetime import datetime
from pydantic import BaseModel

class PlaceAdd(BaseModel):
    title: str
    description: str
    langitude: float
    latitude: float

class EventAdd(PlaceAdd):
    date: datetime

class Place(PlaceAdd):
    id: int
    created_at: datetime
    updated_ad: datetime

class Event(EventAdd): 
    id: int
    created_at: datetime
    updated_ad: datetime
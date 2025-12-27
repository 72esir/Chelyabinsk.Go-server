from enum import Enum

class PlacesTypes(str, Enum):
    EATING = "where to eat"
    DOING = "what to do"
    LIVING = "Where to live"
    GOING = "Where to go"

class EventsTypes(str, Enum):
    NEW_YEAR = "new year"
    THEATERS = "theaters"
    EXCURSIONS = "excursions"
    EXHIBITIONS = "exhibitions"
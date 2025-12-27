from fastapi import APIRouter

from app.core.db_core import SessionDep
from app.models.enums import PlacesTypes
from app.schemas.schemas import PlaceAdd
from app.services import places_service

router = APIRouter(prefix="/places", tags=["Places"])

@router.post("/")
async def add_place(s: SessionDep, payload: PlaceAdd):
    result = await places_service.add_place(s, payload)
    return {
        "success" : True,
        "data" : result
    }

@router.get("/")
async def get_all_places(s: SessionDep):
    result = await places_service.get_all_places(s)
    return {
        "success" : True,
        "data" : result
    }

@router.get(f"/{id}")
async def get_place_by_id(s: SessionDep, place_id: int):
    result = await places_service.get_place_by_id(s, place_id)
    return {
        "success" : True,
        "data" : result
    }

@router.get(f"/{type}")
async def get_places_by_type(s: SessionDep, type: PlacesTypes):
    result = await places_service.get_places_by_type(s, type)
    return {
        "success" : True,
        "data" : result
    }
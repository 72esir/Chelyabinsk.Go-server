from typing import List, Sequence
from fastapi import HTTPException, Query, status
from sqlalchemy import desc, select
from app.core.db_core import SessionDep
from app.models.db_models import PlacesOrm
from app.models.enums import PlacesTypes
from app.schemas.schemas import EventAdd, Place, PlaceAdd

def get_places_dto(places: Sequence[PlacesOrm]) -> List[Place]:
    places_dto = []
    for place in places:
        places_dto.append(Place(
            id=place.id,
            type=place.type,
            title=place.title,
            address=place.address,
            description=place.description,
            image_url=place.image_url,
            longitude=place.longitude,
            latitude=place.latitude,
            created_at=place.created_at,
            updated_at=place.updated_at,
        ))
    return places_dto

async def add_place(s: SessionDep, payload: PlaceAdd):
    new_place = PlacesOrm(
        type=payload.type,
        title=payload.title,
        address=payload.address,
        description=payload.description,
        image_url=payload.image_url,
        latitude=payload.latitude,
        longitude=payload.longitude,
    )

    s.add(new_place)
    await s.commit()
    await s.refresh(new_place)

    return new_place.id

async def get_all_places(s: SessionDep):
    query = select(PlacesOrm)
    res = await s.execute(query)
    places = res.scalars().all()
    places_dto = get_places_dto(places)
    return places_dto

async def get_place_by_id(s: SessionDep, place_id: int):
    query = select(PlacesOrm).filter(PlacesOrm.id == place_id)
    res = await s.execute(query)
    place = res.scalar_one_or_none()
    
    if place:
        place_dto = get_places_dto([place])
        return place_dto

    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="place by id not found"
        )

async def get_places_by_type(s: SessionDep, type: PlacesTypes):
    query = select(PlacesOrm).filter(PlacesOrm.type == type)
    res = await s.execute(query)
    places = res.scalars().all()

    if not places:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="places by type not found"
        )
    
    places_dto = get_places_dto(places)
    return places_dto


    
    

    




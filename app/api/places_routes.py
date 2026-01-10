from fastapi import APIRouter, File, Form, Request, UploadFile

from app.core.db_core import SessionDep
from app.models.enums import PlacesTypes
from app.schemas.schemas import PlaceAdd
from app.services import places_service
from app.services.uploads_service import save_upload_image

router = APIRouter(prefix="/places", tags=["Places"])

@router.post("/")
async def add_place(
    request: Request,
    s: SessionDep,
    type: PlacesTypes = Form(...),
    title: str = Form(...),
    address: str = Form(...),
    description: str = Form(...),
    longitude: float = Form(...),
    latitude: float = Form(...),
    image: UploadFile | None = File(None),
):
    image_url = None
    if image is not None:
        image_url, _ = save_upload_image(request, image)
    payload = PlaceAdd(
        type=type,
        title=title,
        address=address,
        description=description,
        longitude=longitude,
        latitude=latitude,
        image_url=image_url,
    )
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

@router.get("/id/{place_id}")
async def get_place_by_id(s: SessionDep, place_id: int):
    result = await places_service.get_place_by_id(s, place_id)
    return {
        "success" : True,
        "data" : result
    }

@router.get("/type/{place_type}")
async def get_places_by_type(s: SessionDep, place_type: PlacesTypes):
    result = await places_service.get_places_by_type(s, place_type)
    return {
        "success" : True,
        "data" : result
    }

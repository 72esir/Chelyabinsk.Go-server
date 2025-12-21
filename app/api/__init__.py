from fastapi import APIRouter

from app.api.events_routes import router as event_r
from app.api.places_routes import router as place_r

main_router = APIRouter(prefix="/api")

main_router.include_router(event_r)
main_router.include_router(place_r)
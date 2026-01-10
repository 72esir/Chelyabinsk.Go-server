from fastapi import APIRouter, File, Request, UploadFile
from app.services.uploads_service import save_upload_image

router = APIRouter(prefix="/uploads", tags=["Uploads"])

@router.post("/")
async def upload_image(request: Request, file: UploadFile = File(...)):
    url, path = save_upload_image(request, file)
    return {
        "success": True,
        "data": {
            "url": url,
            "path": path
        }
    }

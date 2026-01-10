from pathlib import Path
from uuid import uuid4
import shutil

from fastapi import HTTPException, Request, UploadFile

from app.core.config import BASE_DIR

UPLOAD_DIR = BASE_DIR / "static" / "uploads"
ALLOWED_CONTENT_TYPES = {"image/png", "image/jpeg", "image/webp"}
ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}


def save_upload_image(request: Request, file: UploadFile) -> tuple[str, str]:
    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(status_code=400, detail="unsupported file type")

    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    ext = Path(file.filename or "").suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        ext = ".jpg"

    filename = f"{uuid4().hex}{ext}"
    destination = UPLOAD_DIR / filename

    with destination.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    base_url = str(request.base_url).rstrip("/")
    url = f"{base_url}/static/uploads/{filename}"
    return url, f"static/uploads/{filename}"

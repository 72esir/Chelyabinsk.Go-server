from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from app.api import main_router
from app.core.db_core import engine, Base
from app.core.config import BASE_DIR


app = FastAPI()

app.include_router(main_router)
static_dir = BASE_DIR / "static"
static_dir.mkdir(parents=True, exist_ok=True)
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        print("create tables")
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

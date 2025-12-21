from fastapi import FastAPI
import uvicorn

from app.api import main_router
from app.core.db_core import engine, Base


app = FastAPI()

app.include_router(main_router)

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        print("create tables")
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

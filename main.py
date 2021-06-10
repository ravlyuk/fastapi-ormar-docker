from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from database.db import database
from resume.api import resume_router
from user.routers import user_router

app = FastAPI(title="Resume API", description="Simple api for load resume", version="0.1.0")
app.state.database = database  # підключення бази

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


app.include_router(user_router)
app.include_router(resume_router)

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='0.0.0.0', reload=True)

import aiofiles
from uuid import uuid4
from fastapi import UploadFile, HTTPException
import os

from . import models, schemas


async def save_resume(
        user: models.User,
        file: UploadFile,
        title: str,
        description: str,
):
    user_folder = f"media/{user.email}"
    os.makedirs(user_folder, exist_ok=True)
    file_name = f"{user_folder}/{title.replace(' ', '_')}_{uuid4()}.pdf"
    if file.content_type == "application/pdf":
        await write_resume(file_name, file)
    else:
        raise HTTPException(status_code=418, detail="It's not pdf file.")

    info = schemas.UploadResume(title=title, description=description)
    return await models.Resume.objects.create(file=file_name, user=user.dict(), **info.dict())


async def write_resume(file_name: str, file: UploadFile):
    async with aiofiles.open(file_name, "wb") as buffer:
        data = await file.read()
        await buffer.write(data)

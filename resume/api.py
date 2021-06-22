from typing import List
from starlette.requests import Request
from fastapi import APIRouter, UploadFile, File, Form, Depends
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from . import models, schemas, services
from user import role, auth

resume_router = APIRouter(tags=['resume'])
test_router = APIRouter(tags=['test permission'])

templates = Jinja2Templates(directory="templates")


@resume_router.post("/")
async def create_resume(
        title: str = Form(...),
        description: str = Form(...),
        file: UploadFile = File(...),
        user: models.User = Depends(auth.current_active_user)
):
    return await services.save_resume(user, file, title, description)


@resume_router.get("/user/{user_pk}", response_model=List[schemas.GetListResume])
async def get_list_resume(user_pk: str):
    return await models.Resume.objects.filter(user=user_pk).all()


@resume_router.get("/resumes", response_class=HTMLResponse)
async def get_resume(request: Request):
    resumes = await models.Resume.objects.select_related('user').all()

    return templates.TemplateResponse("resumes.html", {"request": request, "resumes": resumes})


# -----------------

@test_router.get("/user/member_admin", dependencies=[Depends(role.member_admin)])
async def member_admin():
    return 'Member and Admin - success!'


@test_router.get("/user/admin", dependencies=[Depends(role.admin)])
async def admin():
    return 'Admin - success!'


@test_router.get("/user/member", dependencies=[Depends(role.member)])
async def member():
    return 'Member - success!'

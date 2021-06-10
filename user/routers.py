from fastapi import APIRouter

from user.api import after_register

from user.auth import fastapi_users, jwt_authentication

user_router = APIRouter()

user_router.include_router(
    fastapi_users.get_auth_router(jwt_authentication), prefix="/auth/jwt", tags=['auth']
)

user_router.include_router(
    fastapi_users.get_register_router(after_register), prefix='/auth', tags=['auth']
)

user_router.include_router(
    fastapi_users.get_users_router(), prefix='/users', tags=['users'],
)

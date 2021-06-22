from typing import Literal

from fastapi_users import models

# модель користувача
from pydantic import EmailStr


class User(models.BaseUser):
    username: str
    role: Literal['member', 'moderator', 'admin'] = 'member'


# створення користувача
class UserCreate(models.CreateUpdateDictModel):
    username: str
    email: EmailStr
    password: str
    role: Literal['member', 'moderator', 'admin'] = 'member'


# оновлення користувача
class UserUpdate(User, models.BaseUserUpdate):
    pass


# вивід користувача
class UserDB(User, models.BaseUserDB):
    pass

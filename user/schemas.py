from fastapi_users import models

# модель користувача
from pydantic import EmailStr


class User(models.BaseUser):
    username: str


# створення користувача
class UserCreate(models.CreateUpdateDictModel):
    username: str
    email: EmailStr
    password: str


# оновлення користувача
class UserUpdate(User, models.BaseUserUpdate):
    pass


# вивід користувача
class UserDB(User, models.BaseUserDB):
    pass

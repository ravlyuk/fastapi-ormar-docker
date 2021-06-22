import ormar
from fastapi_users.db import OrmarBaseUserModel, OrmarUserDatabase
from database.db import MainMeta
from user.schemas import UserDB


class User(OrmarBaseUserModel):
    class Meta(MainMeta):
        pass

    username: str = ormar.String(max_length=100, unique=True, nullable=False)
    role: str = ormar.String(max_length=50, nullable=False, default='member')


user_db = OrmarUserDatabase(UserDB, User)  # реєстр ormar моделі та pydantic моделі

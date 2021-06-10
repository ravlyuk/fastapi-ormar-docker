from fastapi_users.authentication import JWTAuthentication
from fastapi_users import FastAPIUsers

from user.models import user_db
from user.schemas import User, UserDB, UserCreate, UserUpdate

SECRET = "95hgjbnjkfbjh859b9ubgbjbfbdj054gjnsvcbmaa36umx"

auth_backends = []

jwt_authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=120 * 60)  # життя токену в секундах

auth_backends.append(jwt_authentication)

fastapi_users = FastAPIUsers(
    user_db,  # модель користувача ormar + pydantic
    auth_backends,  # список аутентивіцій
    User,  # ormar модель користувача
    UserCreate,  # ormar модель створення користувача
    UserUpdate,  # ormar модель оновлення користувача
    UserDB,  # ormar модель виведення користувача
)

current_active_user = fastapi_users.current_user(active=True)

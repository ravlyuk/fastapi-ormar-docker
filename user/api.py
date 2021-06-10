from starlette.requests import Request

from user.schemas import UserDB


def after_register(user: UserDB, requests: Request) -> None:
    print(f'User {user.id} has registered.')

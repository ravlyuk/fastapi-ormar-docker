from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str


class UploadResume(BaseModel):
    title: str
    description: str


class GetListResume(BaseModel):
    id: int
    title: str
    description: str
    file: str


class GetResume(GetListResume):
    user: User


class Message(BaseModel):
    message: str

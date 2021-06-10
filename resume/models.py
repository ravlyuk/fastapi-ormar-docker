from typing import Optional, Union, Dict
import ormar
from datetime import datetime

from database.db import MainMeta
from user.models import User


class Resume(ormar.Model):
    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=50)
    description: str = ormar.String(max_length=500)
    file: str = ormar.String(max_length=100, default="some file")
    create_at: datetime = ormar.DateTime(default=datetime.utcnow)
    user: Optional[Union[User, Dict]] = ormar.ForeignKey(User)

    class Meta(MainMeta):
        pass

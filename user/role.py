from typing import List
from user.auth import current_active_user

from fastapi import Depends, HTTPException

from . import models


class RoleChecker:
    def __init__(self, allowed_roles: List):
        self.allowed_roles = allowed_roles

    def __call__(self, user: models.User = Depends(current_active_user)):
        if user.role not in self.allowed_roles:
            print(f"User with role {user.role} not in {self.allowed_roles}")
            raise HTTPException(status_code=403, detail="Operation not permitted")


admin = RoleChecker(["admin"])
member = RoleChecker(["member"])
member_admin = RoleChecker(["member", "admin"])

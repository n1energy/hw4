import typing
from hashlib import sha256
from typing import Optional
import uuid

from app.base.base_accessor import BaseAccessor
from app.admin.models import Admin

if typing.TYPE_CHECKING:
    from app.web.app import Application


class AdminAccessor(BaseAccessor):
    async def connect(self, app: "Application"):
        password_encoded = sha256(b"Nobody inspects the spammish repetition").hexdigest()
        admin = Admin(id=self.app.database.next_admin_id, email=self.app.config.admin.email,
                      password=sha256(self.app.config.admin.password.encode()).hexdigest())
        self.app.database.admins.append(admin)
        # TODO: создать админа по данным в config.yml здесь
        return None

    async def get_by_email(self, email: str) -> Optional[Admin]:
        # next(user.salary for user in userList if user.name == 'john')
        for admin in self.app.database.admins:
            if admin.email == email:
                return admin
        return None

    async def create_admin(self, email: str, password: str) -> Admin:
        # admin = Admin(email=)
        # return admin
        pass

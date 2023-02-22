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
        admin = await self.create_admin(email=self.app.config.admin.email, password=self.app.config.admin.password)
        self.app.database.admins.append(admin)

    async def get_by_email(self, email: str) -> Optional[Admin]:
        for admin in self.app.database.admins:
            if admin.email == str(email):
                return admin
        return None

    async def create_admin(self, email: str, password: str) -> Admin:
        encoded_password = sha256(str(password).encode()).hexdigest()
        admin = Admin(id=self.app.database.next_admin_id, email=email, password=encoded_password)
        self.app.database.admins.append(admin)
        return admin

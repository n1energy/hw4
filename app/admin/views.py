from aiohttp.web_exceptions import HTTPUnauthorized
from aiohttp_apispec import request_schema, response_schema, docs

from app.web.app import View
from app.web.utils import json_response
from app.admin.schemes import AdminSchema


class AdminLoginView(View):
    @docs(tags=["admin"], summary="Login", description="Admin login")
    @request_schema(AdminSchema)
    @response_schema(AdminSchema, 200)
    async def post(self):
        # if not self.request.headers.get("Authorization"):
        #     raise HTTPUnauthorized
        admin = await self.store.admins.get_by_email(self.data['email'])
        if not admin or not admin.is_password_valid(self.data['password']):
            raise HTTPForbidden
        return json_response(AdminSchema().dump(admin))


class AdminCurrentView(View):
    @docs(tags=["admin"], summary="View current admin", description="view your admin info")
    @response_schema(AdminSchema, 200)
    async def get(self):
        if self.request.admin:
            return json_response(data=AdminSchema().dump(self.request.admin))
        raise HTTPUnauthorized

from aiohttp.web_exceptions import HTTPConflict
from aiohttp_apispec import request_schema, response_schema, docs

from app.quiz.schemes import (
    ThemeSchema, QuestionSchema,
)
from app.web.app import View
from app.web.mixins import AuthRequiredMixin
from app.web.schemes import OkResponseSchema
from app.web.utils import json_response


# TODO: добавить проверку авторизации для этого View
class ThemeAddView(View, AuthRequiredMixin):
    @docs(tags=["quiz"], summary="Add new theme", description="Add new theme to database")
    @request_schema(ThemeSchema)
    @response_schema(OkResponseSchema, 200)
    async def post(self):
        title = self.data['title']
        if self.store.quizzes.get_theme_by_title(title):
            raise HTTPConflict
        theme = await self.store.quizzes.create_theme(title=title)
        return json_response(data=ThemeSchema().dump(theme))


class ThemeListView(View):
    @request_schema(ThemeSchema)
    async def get(self):
        themes = await self.store.quizzes.list_themes()
        return json_response(data=ThemeSchema().dump(themes))


class QuestionAddView(View, AuthRequiredMixin):
    @docs(tags=["quiz"], summary="Add new question", description="Add new question to database")
    @request_schema(QuestionSchema)
    @response_schema(OkResponseSchema, 200)
    async def post(self):
        title = self.data['title']
        theme_id = self.data['theme_id']
        question = await self.store.quizzes.create_question(title=title, theme_id=self.data['theme_id'],)
        return json_response(data=QuestionSchema().dump(question))


class QuestionListView(View):
    async def get(self):
        raise NotImplementedError

from dataclasses import dataclass, field

from app.admin.models import Admin
from app.quiz.models import Theme, Question


@dataclass
class Database:
    # TODO: добавить поля admins и questions
    admins: list[Admin] = field(default_factory=list)
    questions: list[Question] = field(default_factory=list)
    themes: list[Theme] = field(default_factory=list)

    @property
    def next_theme_id(self) -> int:
        return len(self.themes) + 1

    def clear(self):
        self.themes = []

    @property
    def next_admin_id(self) -> int:
        return len(self.admins) + 1

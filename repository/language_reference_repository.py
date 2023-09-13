from typing import Sequence

from sqlalchemy import select

from entity import LanguageReference
from repository.base_repository import BaseRepository


class LanguageReferenceRepository(BaseRepository):

    def find_by_code(self, code: str) -> LanguageReference:
        find_by_code_sql = select(LanguageReference).where(LanguageReference.code == code)
        return self.session.scalar(find_by_code_sql)

    def find_all(self, skip: int = 0, limit: int = 100) -> Sequence[LanguageReference]:
        find_all_sql = select(LanguageReference).offset(skip).limit(limit)
        return self.session.scalars(find_all_sql).all()

    def add_one(self, language_reference: LanguageReference) -> LanguageReference:
        self.session.add(language_reference)
        self.session.commit()
        self.session.refresh(language_reference)
        return language_reference

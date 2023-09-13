from typing import Sequence

from sqlalchemy import select

from entity import Translation, Word
from .base_repository import BaseRepository


class TranslationRepository(BaseRepository):
    model_type = Translation

    def find_by_from_word(self, from_word: Word) -> Sequence[Translation]:
        sql = select(Translation).where(Translation.from_word == from_word)
        return self.session.scalars(sql).all()

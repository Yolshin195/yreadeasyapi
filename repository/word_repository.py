from typing import Sequence

from sqlalchemy import select

from entity import Word
from repository.base_repository import BaseRepository


class WordRepository(BaseRepository):

    def find_all(self, skip: int = 0, limit: int = 100) -> Sequence[Word]:
        find_all_sql = select(Word).offset(skip).limit(limit)
        return self.session.scalars(find_all_sql).all()

    def add_one(self, word: Word) -> Word:
        self.session.add(word)
        self.session.commit()
        self.session.refresh(word)
        return word

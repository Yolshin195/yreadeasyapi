from typing import Optional

from sqlalchemy import select

from entity import Word
from repository.base_repository import BaseRepository


class WordRepository(BaseRepository):
    model_type = Word

    def find_by_value(self, value: str) -> Optional[Word]:
        find_by_value_sql = select(Word).where(Word.value == value)
        return self.session.scalar(find_by_value_sql)

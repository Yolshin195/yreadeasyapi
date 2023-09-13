from typing import Sequence

from sqlalchemy import select, insert

from entity import PartOfSpeechReference
from repository.base_repository import BaseRepository


class PartOfSpeechReferenceRepository(BaseRepository):

    def find_by_code(self, code: str) -> PartOfSpeechReference:
        find_by_code_sql = select(PartOfSpeechReference).where(PartOfSpeechReference.code == code)
        return self.session.scalar(find_by_code_sql)

    def find_all(self, skip: int = 0, limit: int = 100) -> Sequence[PartOfSpeechReference]:
        find_all_sql = select(PartOfSpeechReference).offset(skip).limit(limit)
        return self.session.scalars(find_all_sql).all()

    def add_one(self, part_of_speech_reference: PartOfSpeechReference) -> PartOfSpeechReference:
        self.session.add(part_of_speech_reference)
        self.session.commit()
        self.session.refresh(part_of_speech_reference)
        return part_of_speech_reference

from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped

from .base_entity import BaseEntity
from .language_reference import LanguageReference
from .part_of_speech_reference import PartOfSpeechReference


class Word(BaseEntity):
    __tablename__ = BaseEntity.build_table_name("word")

    value: Mapped[str]
    description: Mapped[str | None]
    example_use: Mapped[str | None]
    transcription: Mapped[str | None]

    part_of_speech_id: Mapped[UUID] = mapped_column(ForeignKey("yre_part_Of_speech_reference.id"))
    part_of_speech: Mapped["PartOfSpeechReference"] = relationship(foreign_keys=part_of_speech_id)

    language_id: Mapped[UUID] = mapped_column(ForeignKey("yre_language_reference.id"))
    language: Mapped["LanguageReference"] = relationship(foreign_keys=language_id)

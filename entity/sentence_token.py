from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_entity import BaseEntity

if TYPE_CHECKING:
    from .word import Word
    from .sentence import Sentence


class SentenceToken(BaseEntity):
    __tablename__ = BaseEntity.build_table_name("sentence_token")

    index: Mapped[int]
    type: Mapped[str]
    value: Mapped[str]

    word_id: Mapped[UUID] = mapped_column(ForeignKey("yre_word.id"))
    word: Mapped["Word"] = relationship(foreign_keys=word_id)

    sentence_id: Mapped[UUID] = mapped_column(ForeignKey("yre_sentence.id"))
    sentence: Mapped["Sentence"] = relationship(back_populates="sentence_tokens")

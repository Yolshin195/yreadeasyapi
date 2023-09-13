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

    word_id: Mapped[UUID | None] = mapped_column(ForeignKey("yre_word.id"))
    word: Mapped["Word"] = relationship(foreign_keys=word_id)

    sentence_id: Mapped[UUID] = mapped_column(ForeignKey("yre_sentence.id"))
    sentence: Mapped["Sentence"] = relationship(back_populates="sentence_tokens")

    @staticmethod
    def build_for_sentence(sentence: "Sentence", sentence_text: str) -> list["SentenceToken"]:
        return [SentenceToken.build(sentence, i, value) for i, value in enumerate(sentence_text.split(" "))]

    @staticmethod
    def build(sentence: "Sentence", index: int, value: str) -> "SentenceToken":
        return SentenceToken(
            sentence=sentence,
            index=index,
            type="type",
            value=value
        )

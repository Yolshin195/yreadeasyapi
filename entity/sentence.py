from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_entity import BaseEntity
from .sentence_token import SentenceToken

if TYPE_CHECKING:
    from .article_element import ArticleElement


class Sentence(BaseEntity):
    __tablename__ = BaseEntity.build_table_name("sentence")

    index: Mapped[int]

    article_element_id: Mapped[UUID] = mapped_column(ForeignKey("yre_article_element.id"))
    article_element: Mapped["ArticleElement"] = relationship(back_populates="sentences")

    sentence_tokens: Mapped[list["SentenceToken"]] = relationship(
        back_populates="sentence", cascade="all, delete-orphan"
    )

    @staticmethod
    def build_for_article_element(article_element: "ArticleElement", article_element_text: str) -> list["Sentence"]:
        return [Sentence.build(article_element, i, sentence_text) for i, sentence_text
                in enumerate(article_element_text.split(". "))]

    @staticmethod
    def build(article_element: "ArticleElement", index: int, sentence_text: str) -> "Sentence":
        sentence = Sentence(
            index=index,
            article_element=article_element,
        )
        sentence.sentence_tokens = SentenceToken.build_for_sentence(sentence, sentence_text)
        return sentence

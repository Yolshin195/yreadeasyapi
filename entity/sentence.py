from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_entity import BaseEntity

if TYPE_CHECKING:
    from .article_element import ArticleElement
    from .sentence_token import SentenceToken


class Sentence(BaseEntity):
    __tablename__ = BaseEntity.build_table_name("sentence")

    article_element_id: Mapped[UUID] = mapped_column(ForeignKey("yre_article_element.id"))
    article_element: Mapped["ArticleElement"] = relationship(back_populates="sentences")

    sentence_tokens: Mapped[list["SentenceToken"]] = relationship(
        back_populates="sentence", cascade="all, delete-orphan"
    )

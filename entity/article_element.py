from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_entity import BaseEntity

if TYPE_CHECKING:
    from .article import Article
    from .sentence import Sentence


class ArticleElement(BaseEntity):
    __tablename__ = BaseEntity.build_table_name("article_element")

    article_id: Mapped[UUID] = mapped_column(ForeignKey("yre_article.id"))
    article: Mapped["Article"] = relationship(back_populates="article_elements")

    sentences: Mapped[list["Sentence"]] = relationship(
        back_populates="sentence", cascade="all, delete-orphan"
    )

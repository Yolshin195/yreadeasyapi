from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_entity import BaseEntity
from .sentence import Sentence

if TYPE_CHECKING:
    from .article import Article


class ArticleElement(BaseEntity):
    __tablename__ = BaseEntity.build_table_name("article_element")

    index: Mapped[int]

    article_id: Mapped[UUID] = mapped_column(ForeignKey("yre_article.id"))
    article: Mapped["Article"] = relationship(back_populates="article_elements")

    sentences: Mapped[list["Sentence"]] = relationship(
        back_populates="article_element", cascade="all, delete-orphan"
    )

    @staticmethod
    def build_for_article(article: "Article", original_content: str) -> list["ArticleElement"]:
        return [ArticleElement.build(article, i, article_element_text) for i, article_element_text in
                enumerate(filter(lambda item: True if item else False, original_content.split("\n")))]

    @staticmethod
    def build(article: "Article", index: int, article_element_text: str) -> "ArticleElement":
        article_element = ArticleElement(
            index=index,
            article=article
        )
        article_element.sentences = Sentence.build_for_article_element(article_element, article_element_text)
        return article_element

from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from .base_entity import BaseEntity
from .article_element import ArticleElement


class Article(BaseEntity):
    __tablename__ = BaseEntity.build_table_name("article")

    title: Mapped[str]
    original_content: Mapped[str]
    source_link: Mapped[str]

    article_elements: Mapped[list["ArticleElement"]] = relationship(
        back_populates="article", cascade="all, delete-orphan"
    )

    @staticmethod
    def build(title: str, source_link: str, original_content: str) -> "Article":
        article = Article(
            title=title,
            source_link=source_link,
            original_content=original_content,
        )
        article.article_elements = ArticleElement.build_for_article(article, original_content)
        return article

from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from .base_entity import BaseEntity

if TYPE_CHECKING:
    from .article_element import ArticleElement


class Article(BaseEntity):
    __tablename__ = BaseEntity.build_table_name("article")

    title: Mapped[str]
    original_content: Mapped[str]
    source_link: Mapped[str]

    article_elements: Mapped[list["ArticleElement"]] = relationship(
        back_populates="article", cascade="all, delete-orphan"
    )

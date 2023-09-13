from pydantic import BaseModel

from .article_element_model import ArticleElementModel


class ArticleModel(BaseModel):
    title: str
    source_link: str
    article_elements: list["ArticleElementModel"]
    article_elements_len: int

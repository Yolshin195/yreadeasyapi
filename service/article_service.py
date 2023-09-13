from pydantic import BaseModel

from entity import Article
from mapper.article_model_mapper import article_model_mapper
from model.atricle_model import CreateArticleModel, ArticleModel
from repository import ArticleRepository
from .base_service import BaseService


class ArticleService(BaseService):
    def __init__post__(self):
        self.repository = ArticleRepository(self.session)

    def find_all(self, skip: int = 0, limit: int = 100) -> list[ArticleModel]:
        return [article_model_mapper(entity) for entity in self.repository.find_all(skip, limit)]

    def create(self, create_article_model: CreateArticleModel) -> ArticleModel:
        article = Article.build(
            create_article_model.title,
            create_article_model.source_link,
            create_article_model.original_content
        )

        article = self.repository.add_one(article)

        return article_model_mapper(article)

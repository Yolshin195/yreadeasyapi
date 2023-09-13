from entity import Article
from repository.base_repository import BaseRepository


class ArticleRepository(BaseRepository):
    model_type = Article

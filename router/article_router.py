from fastapi import APIRouter, Depends

from model.atricle_model import ArticleModel, CreateArticleModel
from service import ArticleService

article_router = APIRouter(prefix="/article", tags=["article"])


@article_router.get("/all")
async def get_all(skip: int = 0, limit: int = 100, article_service: ArticleService = Depends()) -> list[ArticleModel]:
    return article_service.find_all(skip, limit)


@article_router.post("/create")
async def create(create_article_model: CreateArticleModel, article_service: ArticleService = Depends()) -> ArticleModel:
    return article_service.create(create_article_model)

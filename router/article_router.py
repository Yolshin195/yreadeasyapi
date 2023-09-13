from fastapi import APIRouter, Depends

from model.atricle_model import ArticleModel

article_router = APIRouter(prefix="/article", tags=["article"])


@article_router.get("/all")
async def get_all(skip: int = 0, limit: int = 100) -> list[ArticleModel]:
    return list()


@article_router.post("/create")
async def create():
    pass

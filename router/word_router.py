from fastapi import APIRouter, Depends

from model.word_model import WordModel, CreateWordModel
from service import WordService

word_router = APIRouter(prefix="/word", tags=["word"])


@word_router.get("/all")
async def get_all(skip: int = 0, limit: int = 100,
                  word_service: WordService = Depends()) -> list[WordModel]:
    return word_service.find_all(skip, limit)


@word_router.post("/create")
async def get_all(create_word_model: CreateWordModel,
                  word_service: WordService = Depends()) -> WordModel:
    return word_service.add_one(create_word_model)

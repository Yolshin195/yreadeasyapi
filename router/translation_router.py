from fastapi import APIRouter, Depends

from model.translation_model import TranslationModel, CreateTranslationModel
from service.translation_service import TranslationService

translation_router = APIRouter(prefix="/translation", tags=["translation"])


@translation_router.get("/all")
async def get_all(skip: int = 0, limit: int = 100,
                  translation_service: TranslationService = Depends()) -> list[TranslationModel]:
    return translation_service.find_all(skip, limit)


@translation_router.put("/create")
async def create(create_translation_model: CreateTranslationModel,
                 translation_service: TranslationService = Depends()):
    return translation_service.add_one(create_translation_model)

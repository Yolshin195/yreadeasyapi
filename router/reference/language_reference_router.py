from fastapi import APIRouter, Depends

from model.reference_model import ReferenceModel, CreateReferenceModel
from service import LanguageReferenceService

language_reference_router = APIRouter(prefix="/language", tags=["reference"])


@language_reference_router.get("/all")
async def get_all(skip: int = 0, limit: int = 100,
                  language_reference_service: LanguageReferenceService = Depends()) -> list[ReferenceModel]:
    return language_reference_service.find_all(skip, limit)


@language_reference_router.post("/create")
async def create(create_reference_model: CreateReferenceModel,
                 language_reference_service: LanguageReferenceService = Depends()):
    return language_reference_service.add_one(create_reference_model)

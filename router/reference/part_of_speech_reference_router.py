from fastapi import APIRouter, Depends

from model.reference_model import ReferenceModel, CreateReferenceModel
from service import PartOfSpeechReferenceService

part_of_speech_reference_router = APIRouter(prefix="/part/of/speech", tags=["reference"])


@part_of_speech_reference_router.get("/all")
async def get_all(skip: int = 0, limit: int = 100,
                  language_reference_service: PartOfSpeechReferenceService = Depends()) -> list[ReferenceModel]:
    return language_reference_service.find_all(skip, limit)


@part_of_speech_reference_router.post("/create")
async def create(create_reference_model: CreateReferenceModel,
                 language_reference_service: PartOfSpeechReferenceService = Depends()):
    return language_reference_service.add_one(create_reference_model)

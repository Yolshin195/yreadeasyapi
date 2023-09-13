from entity import PartOfSpeechReference
from mapper.reference_model_mapper import reference_model_mapper
from model.reference_model import ReferenceModel, CreateReferenceModel
from repository import PartOfSpeechReferenceRepository
from .base_service import BaseService


class PartOfSpeechReferenceService(BaseService):

    def __init__post__(self):
        self.repository = PartOfSpeechReferenceRepository(self.session)

    def find_by_code(self, code: str) -> PartOfSpeechReference:
        return self.repository.find_by_code(code)

    def find_all(self, skip: int = 0, limit: int = 100) -> list[ReferenceModel]:
        return [reference_model_mapper(entity) for entity in self.repository.find_all(skip, limit)]

    def add_one(self, create_reference_model: CreateReferenceModel) -> ReferenceModel:
        part_of_speech_reference = PartOfSpeechReference(**create_reference_model.model_dump())
        part_of_speech_reference = self.repository.add_one(part_of_speech_reference)
        return reference_model_mapper(part_of_speech_reference)

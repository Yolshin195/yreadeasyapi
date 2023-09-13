from entity import LanguageReference
from model.reference_model import ReferenceModel, CreateReferenceModel
from repository import LanguageReferenceRepository
from .base_service import BaseService


class LanguageReferenceService(BaseService):

    def __init__post__(self):
        self.repository = LanguageReferenceRepository(self.session)

    def find_by_code(self, code: str) -> LanguageReference:
        return self.repository.find_by_code(code)

    def find_all(self, skip: int = 0, limit: int = 100) -> list[ReferenceModel]:
        return [ReferenceModel(id=category.id, code=category.code, name=category.name) for category
                in self.repository.find_all(skip, limit)]

    def add_one(self, create_reference_model: CreateReferenceModel) -> ReferenceModel:
        language_reference = LanguageReference(**create_reference_model.model_dump())
        language_reference = self.repository.add_one(language_reference)
        return ReferenceModel(
            id=language_reference.id,
            code=language_reference.code,
            name=language_reference.name
        )

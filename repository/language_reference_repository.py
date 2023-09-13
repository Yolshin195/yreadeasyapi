from entity import LanguageReference
from repository.base_reference_repository import BaseReferenceRepository


class LanguageReferenceRepository(BaseReferenceRepository):
    model_type = LanguageReference


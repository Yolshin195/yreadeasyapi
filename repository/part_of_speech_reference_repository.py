from entity import PartOfSpeechReference
from repository.base_reference_repository import BaseReferenceRepository


class PartOfSpeechReferenceRepository(BaseReferenceRepository):
    model_type = PartOfSpeechReference

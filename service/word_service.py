from entity import Word
from model.reference_model import ReferenceModel
from model.word_model import WordModel, CreateWordModel
from repository import WordRepository, LanguageReferenceRepository, PartOfSpeechReferenceRepository
from .base_service import BaseService


class WordService(BaseService):

    def __init__post__(self):
        self.repository = WordRepository(self.session)
        self.language_reference_repository = LanguageReferenceRepository(self.session)
        self.part_of_speech_reference_repository = PartOfSpeechReferenceRepository(self.session)

    def find_all(self, skip: int = 0, limit: int = 100) -> list[WordModel]:
        return [WordModel(id=word.id, value=word.value,
                          description=word.description,
                          example_use=word.example_use,
                          transcription=word.transcription,
                          part_of_speech=build_reference(word.part_of_speech),
                          language=build_reference(word.language)) for word
                in self.repository.find_all(skip, limit)]

    def add_one(self, create_word_model: CreateWordModel) -> WordModel:
        word = Word(
            value=create_word_model.value,
            description=create_word_model.description,
            example_use=create_word_model.example_use,
            transcription=create_word_model.transcription,
        )
        word.part_of_speech = self.part_of_speech_reference_repository.find_by_code(
            create_word_model.part_of_speech_code)
        word.language = self.language_reference_repository.find_by_code(create_word_model.language_code)

        word = self.repository.add_one(word)

        return WordModel(
            id=word.id,
            value=word.value,
            description=word.description,
            example_use=word.example_use,
            transcription=word.transcription,
            part_of_speech=build_reference(word.part_of_speech),
            language=build_reference(word.language)
        )


def build_reference(reference) -> ReferenceModel:
    return ReferenceModel(
        id=reference.id,
        code=reference.code,
        name=reference.name
    )

from entity import Word
from mapper.word_model_mapper import word_model_mapper
from model.word_model import WordModel, CreateWordModel
from repository import WordRepository, LanguageReferenceRepository, PartOfSpeechReferenceRepository
from .base_service import BaseService
from .translation_service import TranslationService


class WordService(BaseService):

    def __init__post__(self):
        self.repository = WordRepository(self.session)
        self.language_reference_repository = LanguageReferenceRepository(self.session)
        self.part_of_speech_reference_repository = PartOfSpeechReferenceRepository(self.session)
        self.translation_service = TranslationService(self.session)

    def find_all(self, skip: int = 0, limit: int = 100) -> list[WordModel]:
        return [word_model_mapper(word, self.translation_service.find_by_from_word(word)) for word
                in self.repository.find_all(skip, limit)]

    def add_one(self, create_word_model: CreateWordModel) -> WordModel:
        word = Word(
            value=create_word_model.value,
            description=create_word_model.description,
            example_use=create_word_model.example_use,
            transcription=create_word_model.transcription,
            part_of_speech=self.part_of_speech_reference_repository.find_by_code(
                create_word_model.part_of_speech_code),
            language=self.language_reference_repository.find_by_code(create_word_model.language_code)
        )
        word = self.repository.add_one(word)
        return word_model_mapper(word)

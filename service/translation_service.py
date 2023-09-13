from entity import Word, Translation
from mapper.translation_model_mapper import translation_model_mapper
from mapper.translation_word_mapper import translation_word_mapper
from model.translation_model import TranslationModel, CreateTranslationModel
from model.word_model import TranslationWordModel
from repository import WordRepository
from repository.translation_repository import TranslationRepository
from service.base_service import BaseService


class TranslationService(BaseService):

    def __init__post__(self):
        self.translation_repository = TranslationRepository(self.session)
        self.word_repository = WordRepository(self.session)

    def add_one(self, create_translation_model: CreateTranslationModel):
        translation: Translation = Translation(
            from_word=self.word_repository.find_by_id(create_translation_model.from_word_id),
            to_word=self.word_repository.find_by_id(create_translation_model.to_word_id)
        )

        translation = self.translation_repository.add_one(translation)
        return translation_model_mapper(translation)

    def find_by_from_word(self, from_word: Word) -> list[TranslationWordModel]:
        return [translation_word_mapper(translation.to_word)
                for translation in self.translation_repository.find_by_from_word(from_word)]

    def find_all(self, skip: int = 0, limit: int = 100) -> list[TranslationModel]:
        return [translation_model_mapper(entity) for entity in self.translation_repository.find_all(skip, limit)]

from entity import Word
from mapper.reference_model_mapper import reference_model_mapper
from model.translation_word_model import TranslationWordModel
from model.word_model import WordModel


def word_model_mapper(word: Word, translation: list[TranslationWordModel] = None) -> WordModel:
    return WordModel(
        id=word.id,
        value=word.value,
        description=word.description,
        example_use=word.example_use,
        transcription=word.transcription,
        part_of_speech=reference_model_mapper(word.part_of_speech),
        language=reference_model_mapper(word.language),
        translation=translation if translation else list()
    )

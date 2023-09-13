from entity import Word
from mapper.reference_model_mapper import reference_model_mapper
from model.translation_word_model import TranslationWordModel


def translation_word_mapper(word: Word) -> TranslationWordModel:
    return TranslationWordModel(
        id=word.id,
        value=word.value,
        description=word.description,
        example_use=word.example_use,
        transcription=word.transcription,
        language=reference_model_mapper(word.language)
    )
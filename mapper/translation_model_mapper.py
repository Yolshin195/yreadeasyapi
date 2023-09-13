from entity import Translation
from mapper.translation_word_mapper import translation_word_mapper
from model.translation_model import TranslationModel


def translation_model_mapper(translation: Translation) -> TranslationModel:
    return TranslationModel(
        id=translation.id,
        from_word=translation_word_mapper(translation.from_word),
        to_word=translation_word_mapper(translation.to_word)
    )
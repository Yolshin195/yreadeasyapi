from uuid import UUID

from pydantic import BaseModel

from .word_model import TranslationWordModel


class TranslationModel(BaseModel):
    id: UUID
    from_word: TranslationWordModel
    to_word: TranslationWordModel


class CreateTranslationModel(BaseModel):
    from_word_id: UUID
    to_word_id: UUID

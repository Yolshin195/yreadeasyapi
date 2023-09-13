from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from .reference_model import ReferenceModel
from .translation_word_model import TranslationWordModel


class CreateWordModel(BaseModel):
    value: str
    description: Optional[str] = None
    example_use: Optional[str] = None
    transcription: Optional[str] = None
    part_of_speech_code: str
    language_code: str


class WordModel(BaseModel):
    id: UUID
    value: str
    description: Optional[str] = None
    example_use: Optional[str] = None
    transcription: Optional[str] = None
    part_of_speech: "ReferenceModel"
    language: "ReferenceModel"
    translation: list[TranslationWordModel]

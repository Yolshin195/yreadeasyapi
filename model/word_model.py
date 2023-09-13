from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from model.reference_model import ReferenceModel


class CreateWordModel(BaseModel):
    value: str
    description: Optional[str] = None
    example_use: Optional[str] = None
    transcription: Optional[str] = None
    part_of_speech_code: str
    language_code: str


class TranslationWordModel(BaseModel):
    value: str
    description: Optional[str]
    example_use: Optional[str]
    transcription: Optional[str]
    part_of_speech: "ReferenceModel"
    language: "ReferenceModel"


class WordModel(BaseModel):
    id: UUID
    value: str
    description: Optional[str] = None
    example_use: Optional[str] = None
    transcription: Optional[str] = None
    part_of_speech: "ReferenceModel"
    language: "ReferenceModel"

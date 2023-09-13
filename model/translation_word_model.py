from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from.reference_model import ReferenceModel


class TranslationWordModel(BaseModel):
    id: UUID
    value: str
    description: Optional[str]
    example_use: Optional[str]
    transcription: Optional[str]
    language: "ReferenceModel"

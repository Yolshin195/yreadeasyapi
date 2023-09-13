from typing import Optional

from pydantic import BaseModel

from .word_model import WordModel


class SentenceTokenModel(BaseModel):
    index: int
    type: str
    value: str
    word: Optional["WordModel"]

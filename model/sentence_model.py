from pydantic import BaseModel

from .sentence_token_model import SentenceTokenModel


class SentenceModel(BaseModel):
    index: int
    sentence_tokens: list["SentenceTokenModel"]
    sentence_tokens_len: int

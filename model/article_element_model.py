from pydantic import BaseModel

from .sentence_model import SentenceModel


class ArticleElementModel(BaseModel):
    index: int
    sentence_len: int
    sentences: list["SentenceModel"]

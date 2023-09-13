from pydantic import BaseModel

from .sentence_model import SentenceModel


class ArticleElementModel(BaseModel):
    index: int
    sentences: list["SentenceModel"]
    sentences_len: int

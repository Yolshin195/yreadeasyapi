from typing import Optional

from pydantic import BaseModel


class LanguageModel(BaseModel):
    name: str


class PartOfSpeechModel(BaseModel):
    name: str


class TranslationWordModel(BaseModel):
    value: str
    description: str
    example_use: str
    transcription: str
    part_of_speech: "PartOfSpeechModel"
    language: "LanguageModel"


class WordModel(BaseModel):
    value: str
    description: str
    example_use: str
    transcription: str
    part_of_speech: "PartOfSpeechModel"
    language: "LanguageModel"
    translations: list["TranslationWordModel"]


class SentenceTokenModel(BaseModel):
    index: int
    type: str
    value: str
    word: Optional["WordModel"]


class SentenceModel(BaseModel):
    index: int
    sentence_tokens: list["SentenceTokenModel"]
    sentence_tokens_len: int


class ArticleElementModel(BaseModel):
    index: int
    sentences: list["SentenceModel"]
    sentences_len: int


class ArticleModel(BaseModel):
    title: str
    source_link: str
    article_elements: list["ArticleElementModel"]
    article_elements_len: int

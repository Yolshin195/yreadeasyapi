from entity import SentenceToken
from model.sentence_token_model import SentenceTokenModel


def sentence_token_model_mapper(sentence_token: SentenceToken) -> SentenceTokenModel:
    return SentenceTokenModel(
        index=sentence_token.index,
        value=sentence_token.value,
        type=sentence_token.type,
        word=None
    )

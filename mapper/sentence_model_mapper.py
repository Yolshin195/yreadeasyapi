from entity import Sentence
from mapper.sentence_token_model_mapper import sentence_token_model_mapper
from model.sentence_model import SentenceModel


def sentence_model_mapper(sentence: Sentence) -> SentenceModel:
    return SentenceModel(
        index=sentence.index,
        sentence_tokens_len=len(sentence.sentence_tokens),
        sentence_tokens=[sentence_token_model_mapper(sentence_token) for sentence_token in sentence.sentence_tokens]
    )

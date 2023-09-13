from entity import ArticleElement
from mapper.sentence_model_mapper import sentence_model_mapper
from model.article_element_model import ArticleElementModel


def article_element_model_mapper(article_element: ArticleElement) -> ArticleElementModel:
    return ArticleElementModel(
        index=article_element.index,
        sentence_len=len(article_element.sentences),
        sentences=[sentence_model_mapper(sentence) for sentence in article_element.sentences],
    )

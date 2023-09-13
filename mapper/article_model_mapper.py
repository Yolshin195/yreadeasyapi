from entity import Article
from mapper.article_element_model_mapper import article_element_model_mapper
from model.atricle_model import ArticleModel


def article_model_mapper(article: Article) -> ArticleModel:
    return ArticleModel(
        title=article.title,
        source_link=article.source_link,
        article_elements_len=len(article.article_elements),
        article_elements=[
            article_element_model_mapper(article_element) for article_element in article.article_elements
        ],
    )

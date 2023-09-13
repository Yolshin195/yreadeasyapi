from entity import Word
from repository.base_repository import BaseRepository


class WordRepository(BaseRepository):
    model_type = Word

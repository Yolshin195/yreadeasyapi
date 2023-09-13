from sqlalchemy import select

from repository.base_repository import BaseRepository, ModelType


class BaseReferenceRepository(BaseRepository):
    def find_by_code(self, code: str) -> ModelType:
        find_by_code_sql = select(ModelType).where(ModelType.code == code)
        return self.session.scalar(find_by_code_sql)

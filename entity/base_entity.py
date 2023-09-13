from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class BaseEntity(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    created_date: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    @staticmethod
    def build_table_name(table_name: str) -> str:
        return f'yre_{table_name}'

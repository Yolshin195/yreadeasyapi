from sqlalchemy.orm import Mapped, mapped_column

from .base_entity import BaseEntity


class ReferenceEntity(BaseEntity):
    __abstract__ = True

    code: Mapped[str] = mapped_column(unique=True)
    name: Mapped[str]
    description: Mapped[str | None]

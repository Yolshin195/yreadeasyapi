from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from entity import BaseEntity, Word


class Translation(BaseEntity):
    __tablename__ = BaseEntity.build_table_name("translation")

    from_word_id: Mapped[UUID] = mapped_column(ForeignKey("yre_word.id"))
    from_word: Mapped["Word"] = relationship(foreign_keys=from_word_id)

    to_word_id: Mapped[UUID] = mapped_column(ForeignKey("yre_word.id"))
    to_word: Mapped["Word"] = relationship(foreign_keys=to_word_id)

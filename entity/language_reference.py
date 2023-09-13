from .reference_entity import ReferenceEntity


class LanguageReference(ReferenceEntity):
    __tablename__ = ReferenceEntity.build_table_name("language_reference")

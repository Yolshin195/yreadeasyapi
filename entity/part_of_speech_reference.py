from .reference_entity import ReferenceEntity


class PartOfSpeechReference(ReferenceEntity):
    __tablename__ = ReferenceEntity.build_table_name("part_Of_speech_reference")

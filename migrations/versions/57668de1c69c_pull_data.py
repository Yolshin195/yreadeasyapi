"""pull data

Revision ID: 57668de1c69c
Revises: 7ddf550fb781
Create Date: 2023-09-13 18:11:05.334918

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import delete
from sqlalchemy.orm import Session

from entity import PartOfSpeechReference, LanguageReference


# revision identifiers, used by Alembic.
revision: str = '57668de1c69c'
down_revision: Union[str, None] = '7ddf550fb781'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


uuid1 = "90d04c35-7efb-47ee-92f9-b52304643639"
uuid2 = "243359cc-323c-4d2b-bb5f-02f1bd63510c"
uuid3 = "f25c0fc3-a775-44b5-99ca-933b77498dd4"
uuid4 = "12f309ae-36d0-4a75-8d4a-0ffae94d3916"
uuid5 = "9d1c7e78-138c-49b2-84b8-f1c41d98242a"
uuid6 = "10977f7a-b120-4769-90d7-c2fe18a48b0a"
uuid7 = "a126587e-2d1d-4214-9823-a38e392e1878"
uuid8 = "561d0969-7b8a-4be6-8af2-4c84b023eed6"
uuid9 = "78a6063e-bebc-4933-8d30-90086e0e1df5"

language_uuid1 = "ec615719-5e32-4483-a15d-f72ba9629f5a"
language_uuid2 = "48cfa25e-c7f4-418e-bca9-f56e557bcd2f"


def upgrade() -> None:
    session = Session(bind=op.get_bind())
    session.add_all([
        PartOfSpeechReference(id=uuid1, code="NOUN", name="Noun",
                              description="A word that represents a person, place, thing, or idea."),
        PartOfSpeechReference(id=uuid2, code="VERB", name="Verb",
                              description="A word that describes an action or state."),
        PartOfSpeechReference(id=uuid3, code="ADJ", name="Adjective", description="A word that describes a noun."),
        PartOfSpeechReference(id=uuid4, code="ADV", name="Adverb",
                              description="A word that describes a verb, adjective, or other adverb."),
        PartOfSpeechReference(id=uuid5, code="PRON", name="Pronoun",
                              description="A word that replaces a noun or noun phrase."),
        PartOfSpeechReference(id=uuid6, code="PREP", name="Preposition",
                              description="A word that shows the relationship between a noun and other words in a sentence."),
        PartOfSpeechReference(id=uuid7, code="CONJ", name="Conjunction",
                              description="A word that connects words, phrases, or clauses."),
        PartOfSpeechReference(id=uuid8, code="PART", name="Particle",
                              description="A small word that doesn’t belong to any of the main parts of speech, but is used in a sentence for various purposes."),
        PartOfSpeechReference(id=uuid9, code="INTJ", name="Interjection",
                              description="A word or phrase that expresses strong emotion."),

        LanguageReference(id=language_uuid1, code="RU", name="Russian", description="Русский язык"),
        LanguageReference(id=language_uuid2, code="EN", name="English", description="English language")
    ])
    session.commit()


def downgrade() -> None:
    session = Session(bind=op.get_bind())

    delete_account_sql = delete(PartOfSpeechReference).where(PartOfSpeechReference.id.in_([
        uuid1, uuid2, uuid3, uuid4, uuid5, uuid6, uuid7, uuid8, uuid9
    ]))
    session.execute(delete_account_sql)

    delete_account_sql = delete(LanguageReference).where(LanguageReference.id.in_([
        language_uuid1, language_uuid2
    ]))
    session.execute(delete_account_sql)

    session.commit()

from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class ReferenceModel(BaseModel):
    id: UUID
    code: str
    name: str


class CreateReferenceModel(BaseModel):
    code: str
    name: str
    description: Optional[str] = None

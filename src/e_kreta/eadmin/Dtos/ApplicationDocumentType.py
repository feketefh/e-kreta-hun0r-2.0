from typing import Optional
from pydantic import BaseModel, Field


class ApplicationDocumentType(BaseModel):
    code: Optional[str] = Field(alias="kod", default=None, frozen=True)
    description: Optional[str] = Field(alias="leiras", default=None, frozen=True)
    documentTemplateName: Optional[str] = Field(alias="dokumentumSablonNev", default=None, frozen=True)
    documentTemplatePath: Optional[str] = Field(alias="dokumentumSablonUtvonal", default=None, frozen=True)
    id: Optional[str] = Field(alias="azonosito", default=None, frozen=True)
    name: Optional[str] = Field(alias="nev", default=None, frozen=True)
    shortName: Optional[str] = Field(alias="rovidNev", default=None, frozen=True)

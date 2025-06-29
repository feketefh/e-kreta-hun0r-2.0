from typing import Optional
from pydantic import BaseModel, Field


class Administrator(BaseModel):
    id: Optional[int] = Field(alias="azonosito", default=None, frozen=True)
    shortName: Optional[str] = Field(alias="nev", default=None, frozen=True)
    title: Optional[str] = Field(alias="titulus", default=None, frozen=True)
    userId: Optional[int] = Field(alias="kretaFelhasznaloAzonosito", default=None, frozen=True)
    userName: Optional[str] = Field(alias="felhasznaloNev", default=None, frozen=True)

from typing import Optional
from pydantic import BaseModel, Field


class AddresseeType(BaseModel):
    code: Optional[str] = Field(alias="kod", default=None, frozen=True)
    description: Optional[str] = Field(alias="leiras", default=None, frozen=True)
    id: Optional[int] = Field(alias="azonosito", default=None, frozen=True)
    name: Optional[str] = Field(alias="nev", default=None, frozen=True)
    shortName: Optional[str] = Field(alias="rovidNev", default=None, frozen=True)

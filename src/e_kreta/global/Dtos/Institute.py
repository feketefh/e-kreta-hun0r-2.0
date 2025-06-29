from typing import Optional
from pydantic import BaseModel, Field


class Institute(BaseModel):
    city: Optional[str] = Field(alias="telepules", default=None, frozen=True)
    environmentName: Optional[str] = Field(alias="kornyezetNev", default=None, frozen=True)
    id: Optional[str] = Field(alias="id", default=None, frozen=True)
    instituteCode: Optional[str] = Field(alias="azonosito", default=None, frozen=True)
    name: Optional[str] = Field(alias="nev", default=None, frozen=True)
    url: Optional[str] = Field(alias="kretaLink", default=None, frozen=True)

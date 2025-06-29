from typing import Optional
from pydantic import BaseModel, Field


class SchoolClass(BaseModel):
    category: Optional[ValueDescriptor] = Field(alias="OktatasNevelesiKategoria", default=None, frozen=True)
    name: Optional[str] = Field(alias="Nev", default=None, frozen=True)
    uid: Optional[str] = Field(alias="Uid", default=None, frozen=True)

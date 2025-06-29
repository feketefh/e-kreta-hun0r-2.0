from typing import Optional
from pydantic import BaseModel, Field


class Group(BaseModel):
    category: Optional[ValueDescriptor] = Field(alias="OktatasNevelesiKategoria", default=None, frozen=True)
    classMaster: Optional[UidStructure] = Field(alias="OsztalyFonok", default=None, frozen=True)
    classMasterAssistant: Optional[UidStructure] = Field(alias="OsztalyFonokHelyettes", default=None, frozen=True)
    educationType: Optional[ValueDescriptor] = Field(alias="OktatasNevelesiFeladat", default=None, frozen=True)
    isActive: Optional[bool] = Field(alias="IsAktiv", default=None, frozen=True)
    name: Optional[str] = Field(alias="Nev", default=None, frozen=True)
    sortIndex: Optional[int] = Field(alias="OktatasNevelesiFeladatSortIndex", default=None, frozen=True)
    type: Optional[str] = Field(alias="Tipus", default=None, frozen=True)
    uid: Optional[str] = Field(alias="Uid", default=None, frozen=True)

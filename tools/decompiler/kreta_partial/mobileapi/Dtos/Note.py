from typing import Optional
from pydantic import BaseModel, Field


class Note(BaseModel):
    content: Optional[str] = Field(alias="Tartalom", default=None, frozen=True)
    contentFormatted: Optional[str] = Field(alias="TartalomFormazott", default=None, frozen=True)
    creatingTimeAsString: Optional[str] = Field(alias="KeszitesDatuma", default=None, frozen=True)
    dateAsString: Optional[str] = Field(alias="Datum", default=None, frozen=True)
    group: Optional[UidStructure] = Field(alias="OsztalyCsoport", default=None, frozen=True)
    seenByTutelaryAsString: Optional[str] = Field(alias="LattamozasDatuma", default=None, frozen=True)
    teacher: Optional[str] = Field(alias="KeszitoTanarNeve", default=None, frozen=True)
    title: Optional[str] = Field(alias="Cim", default=None, frozen=True)
    type: Optional[ValueDescriptor] = Field(alias="Tipus", default=None, frozen=True)
    uid: Optional[str] = Field(alias="Uid", default=None, frozen=True)

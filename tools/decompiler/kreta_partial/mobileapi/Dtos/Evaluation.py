from typing import Optional
from pydantic import BaseModel, Field


class Evaluation(BaseModel):
    creatingTimeAsString: Optional[str] = Field(alias="KeszitesDatuma", default=None, frozen=True)
    form: Optional[str] = Field(alias="Jelleg", default=None, frozen=True)
    formType: Optional[ValueDescriptor] = Field(alias="ErtekFajta", default=None, frozen=True)
    group: Optional[UidStructure] = Field(alias="OsztalyCsoport", default=None, frozen=True)
    mode: Optional[ValueDescriptor] = Field(alias="Mod", default=None, frozen=True)
    numberValue: Optional[int] = Field(alias="SzamErtek", default=None, frozen=True)
    recordDateAsString: Optional[str] = Field(alias="RogzitesDatuma", default=None, frozen=True)
    seenByTutelaryAsString: Optional[str] = Field(alias="LattamozasDatuma", default=None, frozen=True)
    shortValue: Optional[str] = Field(alias="SzovegesErtekelesRovidNev", default=None, frozen=True)
    sortIndex: Optional[int] = Field(alias="SortIndex", default=None, frozen=True)
    subject: Optional[SubjectDescriptor] = Field(alias="Tantargy", default=None, frozen=True)
    teacher: Optional[str] = Field(alias="ErtekeloTanarNeve", default=None, frozen=True)
    theme: Optional[str] = Field(alias="Tema", default=None, frozen=True)
    type: Optional[ValueDescriptor] = Field(alias="Tipus", default=None, frozen=True)
    uid: Optional[str] = Field(alias="Uid", default=None, frozen=True)
    value: Optional[str] = Field(alias="SzovegesErtek", default=None, frozen=True)
    weight: Optional[str] = Field(alias="SulySzazalekErteke", default=None, frozen=True)

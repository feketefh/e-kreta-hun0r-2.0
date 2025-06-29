from typing import Optional
from pydantic import BaseModel, Field


class Omission(BaseModel):
    creatingTimeAsString: Optional[str] = Field(alias="KeszitesDatuma", default=None, frozen=True)
    dateAsString: Optional[str] = Field(alias="Datum", default=None, frozen=True)
    delayTimeMinutes: Optional[int] = Field(alias="KesesPercben", default=None, frozen=True)
    group: Optional[UidStructure] = Field(alias="OsztalyCsoport", default=None, frozen=True)
    justificationState: Optional[str] = Field(alias="IgazolasAllapota", default=None, frozen=True)
    justificationType: Optional[ValueDescriptor] = Field(alias="IgazolasTipusa", default=None, frozen=True)
    lesson: Optional[Lesson] = Field(alias="Ora", default=None, frozen=True)
    mode: Optional[ValueDescriptor] = Field(alias="Mod", default=None, frozen=True)
    subject: Optional[SubjectDescriptor] = Field(alias="Tantargy", default=None, frozen=True)
    teacher: Optional[str] = Field(alias="RogzitoTanarNeve", default=None, frozen=True)
    type: Optional[ValueDescriptor] = Field(alias="Tipus", default=None, frozen=True)
    uid: Optional[str] = Field(alias="Uid", default=None, frozen=True)

class Lesson(BaseModel):
    endTimeAsString: Optional[str] = Field(alias="VegDatum", default=None, frozen=True)
    scheduleNumber: Optional[int] = Field(alias="Oraszam", default=None, frozen=True)
    startTimeAsString: Optional[str] = Field(alias="KezdoDatum", default=None, frozen=True)

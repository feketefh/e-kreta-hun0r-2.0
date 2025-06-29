from typing import Optional
from pydantic import BaseModel, Field


class Classwork(BaseModel):
    allowToAttachFileTypeId: Optional[int] = Field(alias="csatolasEngedelyezesTipusId", default=None, frozen=True)
    classGroupId: Optional[int] = Field(alias="csoportId", default=None, frozen=True)
    classId: Optional[int] = Field(alias="osztalyId", default=None, frozen=True)
    className: Optional[str] = Field(alias="osztalyNev", default=None, frozen=True)
    creationTimeAsString: Optional[str] = Field(alias="letrehozasIdeje", default=None, frozen=True)
    employeeId: Optional[int] = Field(alias="alkalmazottId", default=None, frozen=True)
    groupId: Optional[str] = Field(alias="groupId", default=None, frozen=True)
    id: Optional[int] = Field(alias="id", default=None, frozen=True)
    lengthInMinutes: Optional[int] = Field(alias="idotartamPerc", default=None, frozen=True)
    lessonDateAsString: Optional[str] = Field(alias="oraDatum", default=None, frozen=True)
    lessonNumber: Optional[int] = Field(alias="oraszam", default=None, frozen=True)
    lessonTimeAsString: Optional[str] = Field(alias="oraIdopont", default=None, frozen=True)
    score: Optional[float] = Field(alias="pontszam", default=None, frozen=True)
    subjectCategoryUid: Optional[str] = Field(alias="tantargyKategoriaId", default=None, frozen=True)
    subjectId: Optional[int] = Field(alias="tantargyId", default=None, frozen=True)
    subjectName: Optional[str] = Field(alias="tantargyNev", default=None, frozen=True)
    taskTypeId: Optional[int] = Field(alias="beadandoTipusId", default=None, frozen=True)
    teacherName: Optional[str] = Field(alias="alkalmazottNev", default=None, frozen=True)
    text: Optional[str] = Field(alias="szoveg", default=None, frozen=True)
    title: Optional[str] = Field(alias="cim", default=None, frozen=True)
    uniqueId: Optional[str] = Field(alias="egyediId", default=None, frozen=True)

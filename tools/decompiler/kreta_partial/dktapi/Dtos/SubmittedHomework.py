from typing import Optional
from pydantic import BaseModel, Field


class SubmittedHomework(BaseModel):
    creationTimeAsString: Optional[str] = Field(alias="letrehozva", default=None, frozen=True)
    homeworkId: Optional[int] = Field(alias="feladatId", default=None, frozen=True)
    id: Optional[int] = Field(alias="id", default=None, frozen=True)
    lastModifiedAsString: Optional[str] = Field(alias="utoljaraModositva", default=None, frozen=True)
    solutionText: Optional[str] = Field(alias="szoveg", default=None, frozen=True)
    statusId: Optional[int] = Field(alias="statuszId", default=None, frozen=True)
    statusName: Optional[str] = Field(alias="statuszNev", default=None, frozen=True)
    studentGuid: Optional[str] = Field(alias="tanuloGuid", default=None, frozen=True)
    studentId: Optional[int] = Field(alias="tanuloId", default=None, frozen=True)
    studentName: Optional[str] = Field(alias="tanuloNev", default=None, frozen=True)
    uniqueId: Optional[str] = Field(alias="egyediId", default=None, frozen=True)

from typing import Optional
from pydantic import BaseModel, Field


class Homework(BaseModel):
    _subjectName: Optional[str] = Field(alias="TantargyNeve", default=None, frozen=True)
    attachmentList: Optional[list[Attachment]] = Field(alias="Csatolmanyok", default=None, frozen=True)
    createDateAsString: Optional[str] = Field(alias="RogzitesIdopontja", default=None, frozen=True)
    deadlineDateAsString: Optional[str] = Field(alias="HataridoDatuma", default=None, frozen=True)
    group: Optional[UidStructure] = Field(alias="OsztalyCsoport", default=None, frozen=True)
    isAllowToAttachFile: Optional[bool] = Field(alias="IsCsatolasEngedelyezes", default=None, frozen=True)
    isDone: Optional[bool] = Field(alias="IsMegoldva", default=None, frozen=True)
    isStudentHomeworkEnabled: Optional[bool] = Field(alias="IsTanuloHaziFeladatEnabled", default=None, frozen=True)
    isTeacherRecorded: Optional[bool] = Field(alias="IsTanarRogzitette", default=None, frozen=True)
    recordDateAsString: Optional[str] = Field(alias="FeladasDatuma", default=None, frozen=True)
    recorderTeacherName: Optional[str] = Field(alias="RogzitoTanarNeve", default=None, frozen=True)
    subject: Optional[SubjectDescriptor] = Field(alias="Tantargy", default=None, frozen=True)
    submittable: Optional[bool] = Field(alias="IsBeadhato", default=None, frozen=True)
    text: Optional[str] = Field(alias="Szoveg", default=None, frozen=True)
    uid: Optional[str] = Field(alias="Uid", default=None, frozen=True)

class Attachment(BaseModel):
    name: Optional[str] = Field(alias="Nev", default=None, frozen=True)
    type: Optional[str] = Field(alias="Tipus", default=None, frozen=True)
    uid: Optional[str] = Field(alias="Uid", default=None, frozen=True)

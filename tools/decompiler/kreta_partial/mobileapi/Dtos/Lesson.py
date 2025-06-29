from typing import Optional
from pydantic import BaseModel, Field


class Lesson(BaseModel):
    announcedTestUid: Optional[str] = Field(alias="BejelentettSzamonkeresUid", default=None, frozen=True)
    attachments: Optional[list[Attachment]] = Field(alias="Csatolmanyok", default=None, frozen=True)
    classGroup: Optional[UidNameStructure] = Field(alias="OsztalyCsoport", default=None, frozen=True)
    classScheduleNumber: Optional[int] = Field(alias="Oraszam", default=None, frozen=True)
    classroom: Optional[str] = Field(alias="TeremNeve", default=None, frozen=True)
    classworkGroupId: Optional[str] = Field(alias="FeladatGroupUid", default=None, frozen=True)
    digitalInstrumentType: Optional[str] = Field(alias="DigitalisEszkozTipus", default=None, frozen=True)
    digitalPlatformType: Optional[str] = Field(alias="DigitalisPlatformTipus", default=None, frozen=True)
    endTimeAsString: Optional[str] = Field(alias="VegIdopont", default=None, frozen=True)
    homeWorkUid: Optional[str] = Field(alias="HaziFeladatUid", default=None, frozen=True)
    homeworkEditedByStudentEnabled: Optional[bool] = Field(alias="IsTanuloHaziFeladatEnabled", default=None, frozen=True)
    isDigitalLesson: Optional[bool] = Field(alias="IsDigitalisOra", default=None, frozen=True)
    languageTaskGroupId: Optional[str] = Field(alias="NyelviFeladatGroupUid", default=None, frozen=True)
    lessonNumber: Optional[int] = Field(alias="OraEvesSorszama", default=None, frozen=True)
    name: Optional[str] = Field(alias="Nev", default=None, frozen=True)
    presence: Optional[ValueDescriptor] = Field(alias="TanuloJelenlet", default=None, frozen=True)
    startTimeAsString: Optional[str] = Field(alias="KezdetIdopont", default=None, frozen=True)
    state: Optional[ValueDescriptor] = Field(alias="Allapot", default=None, frozen=True)
    subject: Optional[SubjectDescriptor] = Field(alias="Tantargy", default=None, frozen=True)
    supplyTeacher: Optional[str] = Field(alias="HelyettesTanarNeve", default=None, frozen=True)
    supportedDigitalInstrumentTypes: Optional[list[str]] = Field(alias="DigitalisTamogatoEszkozTipusList", default=None, frozen=True)
    teacher: Optional[str] = Field(alias="TanarNeve", default=None, frozen=True)
    topic: Optional[str] = Field(alias="Tema", default=None, frozen=True)
    type: Optional[ValueDescriptor] = Field(alias="Tipus", default=None, frozen=True)
    uid: Optional[str] = Field(alias="Uid", default=None, frozen=True)

class Attachment(BaseModel):
    name: Optional[str] = Field(alias="Nev", default=None, frozen=True)
    uid: Optional[str] = Field(alias="Uid", default=None, frozen=True)

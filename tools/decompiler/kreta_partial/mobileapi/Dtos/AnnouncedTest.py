from typing import Optional
from pydantic import BaseModel, Field


class AnnouncedTest(BaseModel):
    _subjectName: Optional[str] = Field(alias="TantargyNeve", default=None, frozen=True)
    announcedAtAsString: Optional[str] = Field(alias="BejelentesDatuma", default=None, frozen=True)
    classScheduleNumber: Optional[int] = Field(alias="OrarendiOraOraszama", default=None, frozen=True)
    dateAsString: Optional[str] = Field(alias="Datum", default=None, frozen=True)
    group: Optional[UidStructure] = Field(alias="OsztalyCsoport", default=None, frozen=True)
    mode: Optional[ValueDescriptor] = Field(alias="Modja", default=None, frozen=True)
    subject: Optional[SubjectDescriptor] = Field(alias="Tantargy", default=None, frozen=True)
    teacher: Optional[str] = Field(alias="RogzitoTanarNeve", default=None, frozen=True)
    theme: Optional[str] = Field(alias="Temaja", default=None, frozen=True)
    uid: Optional[str] = Field(alias="Uid", default=None, frozen=True)

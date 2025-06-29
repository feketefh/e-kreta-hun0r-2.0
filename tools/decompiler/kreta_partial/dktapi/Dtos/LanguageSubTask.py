from typing import Optional
from pydantic import BaseModel, Field


class LanguageSubTask(BaseModel):
    durationInMinutes: Optional[int] = Field(alias="idotartamPerc", default=None, frozen=True)
    id: Optional[int] = Field(alias="id", default=None, frozen=True)
    percent: Optional[int] = Field(alias="xeropanSzazalek", default=None, frozen=True)
    submissionDateAsString: Optional[str] = Field(alias="xeropanMegoldasBekuldesiIdeje", default=None, frozen=True)
    timeSpent: Optional[int] = Field(alias="xeropanMegoldassalToltottIdoPerc", default=None, frozen=True)
    title: Optional[str] = Field(alias="cim", default=None, frozen=True)
    xeropanLessonId: Optional[int] = Field(alias="xeropanLessonId", default=None, frozen=True)
    xeropanLessonTypeId: Optional[int] = Field(alias="xeropanLessonTypeId", default=None, frozen=True)

from typing import Optional
from pydantic import BaseModel, Field


class ClassworkTeachingMaterialPost(BaseModel):
    classId: Optional[int] = Field(alias="osztalyId", default=None, frozen=True)
    classworkId: Optional[int] = Field(alias="feladatId", default=None, frozen=True)
    date: Optional[str] = Field(alias="datum", default=None, frozen=True)
    employeeId: Optional[int] = Field(alias="alkalmazottId", default=None, frozen=True)
    groupId: Optional[int] = Field(alias="csoportId", default=None, frozen=True)
    lessonNumber: Optional[int] = Field(alias="oraszam", default=None, frozen=True)
    subjectId: Optional[int] = Field(alias="tantargyId", default=None, frozen=True)
    time: Optional[str] = Field(alias="idopont", default=None, frozen=True)

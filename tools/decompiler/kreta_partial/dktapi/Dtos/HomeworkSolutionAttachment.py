from typing import Optional
from pydantic import BaseModel, Field


class HomeworkSolutionAttachment(BaseModel):
    extension: Optional[str] = Field(alias="kiterjesztes", default=None, frozen=True)
    fileName: Optional[str] = Field(alias="fajlNev", default=None, frozen=True)
    id: Optional[int] = Field(alias="id", default=None, frozen=True)
    name: Optional[str] = Field(alias="nev", default=None, frozen=True)
    submittedHomeworkId: Optional[int] = Field(alias="feladatBeadasId", default=None, frozen=True)
    uniqueId: Optional[str] = Field(alias="egyediId", default=None, frozen=True)
    uploaderEmployeeId: Optional[int] = Field(alias="feltoltoAlkalmazottId", default=None, frozen=True)
    uploaderStudentId: Optional[int] = Field(alias="feltoltoTanuloId", default=None, frozen=True)

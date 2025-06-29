from typing import Optional
from pydantic import BaseModel, Field


class ClassworkSolutionAttachment(BaseModel):
    extension: Optional[str] = Field(alias="kiterjesztes", default=None, frozen=True)
    fileName: Optional[str] = Field(alias="fajlNev", default=None, frozen=True)
    id: Optional[int] = Field(alias="id", default=None, frozen=True)
    name: Optional[str] = Field(alias="nev", default=None, frozen=True)
    submittedClassworkId: Optional[int] = Field(alias="feladatBeadasId", default=None, frozen=True)
    uniqueId: Optional[str] = Field(alias="egyediId", default=None, frozen=True)

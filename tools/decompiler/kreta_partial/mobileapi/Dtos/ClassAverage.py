from typing import Optional
from pydantic import BaseModel, Field


class ClassAverage(BaseModel):
    average: Optional[float] = Field(alias="TanuloAtlag", default=None, frozen=True)
    classAverageNumber: Optional[float] = Field(alias="OsztalyCsoportAtlag", default=None, frozen=True)
    differenceFromClassAverage: Optional[float] = Field(alias="OsztalyCsoportAtlagtolValoElteres", default=None, frozen=True)
    subject: Optional[SubjectDescriptor] = Field(alias="Tantargy", default=None, frozen=True)
    uid: Optional[str] = Field(alias="Uid", default=None, frozen=True)

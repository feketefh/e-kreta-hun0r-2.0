from typing import Optional
from pydantic import BaseModel, Field


class SubjectAverage(BaseModel):
    averageNumber: Optional[float] = Field(alias="Atlag", default=None, frozen=True)
    averagesInTime: Optional[list[AverageWithTime]] = Field(alias="AtlagAlakulasaIdoFuggvenyeben", default=None, frozen=True)
    sortIndex: Optional[int] = Field(alias="SortIndex", default=None, frozen=True)
    subject: Optional[SubjectDescriptor] = Field(alias="Tantargy", default=None, frozen=True)
    sumOfWeightedEvaluations: Optional[float] = Field(alias="SulyozottOsztalyzatOsszege", default=None, frozen=True)
    sumOfWeights: Optional[float] = Field(alias="SulyozottOsztalyzatSzama", default=None, frozen=True)
    uid: Optional[str] = Field(alias="Uid", default=None, frozen=True)

class AverageWithTime(BaseModel):
    average: Optional[float] = Field(alias="Atlag", default=None, frozen=True)
    dateAsString: Optional[str] = Field(alias="Datum", default=None, frozen=True)

from typing import Optional
from pydantic import BaseModel, Field


class TimeTableWeek(BaseModel):
    endDateAsString: Optional[str] = Field(alias="VegNapDatuma", default=None, frozen=True)
    numberOfWeek: Optional[int] = Field(alias="HetSorszama", default=None, frozen=True)
    startDateAsString: Optional[str] = Field(alias="KezdoNapDatuma", default=None, frozen=True)
    type: Optional[ValueDescriptor] = Field(alias="Tipus", default=None, frozen=True)
    uid: Optional[str] = Field(alias="Uid", default=None, frozen=True)

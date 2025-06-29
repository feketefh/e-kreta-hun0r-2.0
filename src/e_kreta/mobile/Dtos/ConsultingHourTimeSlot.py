from typing import Optional
from pydantic import BaseModel, Field


class ConsultingHourTimeSlot(BaseModel):
    endTimeAsString: Optional[str] = Field(alias="VegIdopont", default=None, frozen=True)
    isReservedByMe: Optional[bool] = Field(alias="IsJelentkeztem", default=None, frozen=True)
    startTimeAsString: Optional[str] = Field(alias="KezdoIdopont", default=None, frozen=True)
    uid: Optional[str] = Field(alias="Uid", default=None, frozen=True)

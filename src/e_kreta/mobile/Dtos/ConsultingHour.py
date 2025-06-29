from typing import Optional
from pydantic import BaseModel, Field


class ConsultingHour(BaseModel):
    classroomDescriptor: Optional[UidNameStructure] = Field(alias="Terem", default=None, frozen=True)
    consultingHourTimeSlots: Optional[list[ConsultingHourTimeSlot]] = Field(alias="Idopontok", default=None, frozen=True)
    deadlineAsString: Optional[str] = Field(alias="JelentkezesHatarido", default=None, frozen=True)
    endTimeAsString: Optional[str] = Field(alias="VegIdopont", default=None, frozen=True)
    isReservationEnabled: Optional[bool] = Field(alias="IsJelentkezesFeatureEnabled", default=None, frozen=True)
    startTimeAsString: Optional[str] = Field(alias="KezdoIdopont", default=None, frozen=True)
    uid: Optional[str] = Field(alias="Uid", default=None, frozen=True)

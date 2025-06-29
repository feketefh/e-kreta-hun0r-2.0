from typing import Optional
from pydantic import BaseModel, Field


class ConsultingHourList(BaseModel):
    consultingHours: Optional[list[ConsultingHour]] = Field(alias="Fogadoorak", default=None, frozen=True)
    teacherDescriptor: Optional[UidNameStructure] = Field(alias="Tanar", default=None, frozen=True)

from typing import Optional
from pydantic import BaseModel, Field


class SchoolYearCalendarEntry(BaseModel):
    dateAsString: Optional[str] = Field(alias="Datum", default=None, frozen=True)
    dayType: Optional[ValueDescriptor] = Field(alias="Naptipus", default=None, frozen=True)
    group: Optional[UidStructure] = Field(alias="OsztalyCsoport", default=None, frozen=True)
    irregularDay: Optional[ValueDescriptor] = Field(alias="ElteroOrarendSzerintiTanitasiNap", default=None, frozen=True)
    uid: Optional[str] = Field(alias="Uid", default=None, frozen=True)
    weekTypeSchedule: Optional[ValueDescriptor] = Field(alias="OrarendiNapHetirendje", default=None, frozen=True)

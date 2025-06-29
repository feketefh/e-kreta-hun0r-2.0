from typing import Optional
from pydantic import BaseModel, Field


class NepEvent(BaseModel):
    address: Optional[str] = Field(alias="Helyszin", default=None, frozen=True)
    creationDateAsString: Optional[str] = Field(alias="Datum", default=None, frozen=True)
    eventEndTimeAsString: Optional[str] = Field(alias="Vege", default=None, frozen=True)
    eventStartTimeAsString: Optional[str] = Field(alias="Kezdete", default=None, frozen=True)
    eventTitle: Optional[str] = Field(alias="ProgramNev", default=None, frozen=True)
    hasGuardianPermission: Optional[bool] = Field(alias="GondviseloElfogadas", default=None, frozen=True)
    hasStudentAppeared: Optional[bool] = Field(alias="Megjelent", default=None, frozen=True)
    organizationName: Optional[str] = Field(alias="SzervezetNev", default=None, frozen=True)
    uid: Optional[int] = Field(alias="Id", default=None, frozen=True)

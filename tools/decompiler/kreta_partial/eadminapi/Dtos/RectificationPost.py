from typing import Optional
from pydantic import BaseModel, Field


class RectificationPost(BaseModel):
    caseId: Optional[str] = Field(alias="azonosito", default=None, frozen=True)
    caseType: Optional[Type] = Field(alias="tipus", default=None, frozen=True)
    caseTypeCode: Optional[str] = Field(alias="tipusKod", default=None, frozen=True)
    optionalAttachments: Optional[list[OtherThingsToDoAttachments]] = Field(alias="csatolmanyok", default=None, frozen=True)
    state: Optional[State] = Field(alias="statusz", default=None, frozen=True)

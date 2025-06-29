from typing import Optional
from pydantic import BaseModel, Field


class NepEventGuardianPermissionPost(BaseModel):
    eventId: Optional[int] = Field(alias="Id", default=None, frozen=True)
    isPermitted: Optional[bool] = Field(alias="Dontes", default=None, frozen=True)

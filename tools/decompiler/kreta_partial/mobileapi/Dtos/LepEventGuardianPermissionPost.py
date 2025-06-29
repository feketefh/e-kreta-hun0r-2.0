from typing import Optional
from pydantic import BaseModel, Field


class LepEventGuardianPermissionPost(BaseModel):
    eventId: Optional[int] = Field(alias="EloadasId", default=None, frozen=True)
    isPermitted: Optional[bool] = Field(alias="Dontes", default=None, frozen=True)

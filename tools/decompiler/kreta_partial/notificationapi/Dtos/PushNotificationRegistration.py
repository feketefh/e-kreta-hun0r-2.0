from typing import Optional
from pydantic import BaseModel, Field


class PushNotificationRegistration(BaseModel):
    registrationID: Optional[str] = Field(alias="registrationId", default=None, frozen=True)

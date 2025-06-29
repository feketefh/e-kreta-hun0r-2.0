from typing import Optional
from pydantic import BaseModel, Field


class Status(BaseModel):
    buildNumber: Optional[str] = Field(alias="buildNumber", default=None, frozen=True)
    enabledFeatures: Optional[list[str]] = Field(alias="enabledFeatures", default=None, frozen=True)
    idpUrl: Optional[str] = Field(alias="idpUrl", default=None, frozen=True)
    trackingId: Optional[str] = Field(alias="trackingId", default=None, frozen=True)

class FileHandler(BaseModel):
    apiUrl: Optional[str] = Field(alias="apiUrl", default=None, frozen=True)
    features: Optional[list[str]] = Field(alias="features", default=None, frozen=True)

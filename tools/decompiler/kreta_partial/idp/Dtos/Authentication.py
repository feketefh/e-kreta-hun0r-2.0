from typing import Optional
from pydantic import BaseModel, Field


class Authentication(BaseModel):
    accessToken: Optional[str] = Field(alias="access_token", default=None, frozen=True)
    expiresIn: Optional[int] = Field(alias="expires_in", default=None, frozen=True)
    idToken: Optional[str] = Field(alias="id_token", default=None, frozen=True)
    refreshToken: Optional[str] = Field(alias="refresh_token", default=None, frozen=True)
    tokenType: Optional[str] = Field(alias="token_type", default=None, frozen=True)

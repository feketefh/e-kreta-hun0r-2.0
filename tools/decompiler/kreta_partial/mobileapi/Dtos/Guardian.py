from typing import Optional
from pydantic import BaseModel, Field


class Guardian(BaseModel):
    email: Optional[str] = Field(alias="EmailCim", default=None, frozen=True)
    hasParentalRights: Optional[bool] = Field(alias="IsNincsFelugyeletiJoga", default=None, frozen=True)
    isLegalRepresentative: Optional[bool] = Field(alias="IsTorvenyesKepviselo", default=None, frozen=True)
    name: Optional[str] = Field(alias="Nev", default=None, frozen=True)
    phoneNumber: Optional[str] = Field(alias="Telefonszam", default=None, frozen=True)
    uid: Optional[str] = Field(alias="Uid", default=None, frozen=True)

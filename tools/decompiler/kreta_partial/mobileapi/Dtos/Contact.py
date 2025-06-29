from typing import Optional
from pydantic import BaseModel, Field


class Contact(BaseModel):
    email: Optional[str] = Field(alias="Email", default=None, frozen=True)
    id: Optional[str] = Field(alias="Id", default=None, frozen=True)
    isEmailVerified: Optional[bool] = Field(alias="IsEmailMegerositve", default=None, frozen=True)
    phoneNumber: Optional[str] = Field(alias="Telefonszam", default=None, frozen=True)

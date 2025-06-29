from typing import Optional
from pydantic import BaseModel, Field


class Signer(BaseModel):
    educationId: Optional[str] = Field(alias="oktatasiAzonosito", default=None, frozen=True)
    id: Optional[int] = Field(alias="kretaAzonosito", default=None, frozen=True)
    isSigner: Optional[bool] = Field(alias="isAlairo", default=None, frozen=True)
    name: Optional[str] = Field(alias="nev", default=None, frozen=True)
    title: Optional[str] = Field(alias="titulus", default=None, frozen=True)

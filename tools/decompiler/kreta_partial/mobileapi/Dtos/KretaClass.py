from typing import Optional
from pydantic import BaseModel, Field


class KretaClass(BaseModel):
    id: Optional[int] = Field(alias="kretaAzonosito", default=None, frozen=True)
    name: Optional[str] = Field(alias="nev", default=None, frozen=True)

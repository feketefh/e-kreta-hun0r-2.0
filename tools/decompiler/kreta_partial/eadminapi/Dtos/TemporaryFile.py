from typing import Optional
from pydantic import BaseModel, Field


class TemporaryFile(BaseModel):
    fileLength: Optional[int] = Field(alias="fajlMeretByteLength", default=None, frozen=True)
    path: Optional[str] = Field(alias="utvonal", default=None, frozen=True)

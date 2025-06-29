from typing import Optional
from pydantic import BaseModel, Field


class FiledApplication(BaseModel):
    file: Optional[File] = Field(alias="fajl", default=None, frozen=True)
    fileName: Optional[str] = Field(alias="fajlNev", default=None, frozen=True)
    id: Optional[int] = Field(alias="azonosito", default=None, frozen=True)
    registrationNumber: Optional[str] = Field(alias="iktatoszam", default=None, frozen=True)

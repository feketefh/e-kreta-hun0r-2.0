from typing import Optional
from pydantic import BaseModel, Field


class Attachment(BaseModel):
    fileName: Optional[str] = Field(alias="fajlNev", default=None, frozen=True)
    id: Optional[str] = Field(alias="azonosito", default=None, frozen=True)
    temporaryId: Optional[TemporaryId] = Field(alias="fajl", default=None, frozen=True)

class TemporaryId(BaseModel):
    fileHandler: Optional[str] = Field(alias="fileHandler", default=None, frozen=True)
    id: Optional[str] = Field(alias="azonosito", default=None, frozen=True)
    path: Optional[str] = Field(alias="utvonal", default=None, frozen=True)
    temporaryServerUid: Optional[str] = Field(alias="ideiglenesFajlAzonosito", default=None, frozen=True)

from typing import Optional
from pydantic import BaseModel, Field


class File(BaseModel):
    id: Optional[int] = Field(alias="azonosito", default=None, frozen=True)
    temporaryFileId: Optional[str] = Field(alias="ideiglenesFajlAzonosito", default=None, frozen=True)

from typing import Optional
from pydantic import BaseModel, Field


class AccessControlSystemItem(BaseModel):
    commentText: Optional[str] = Field(alias="megjegyzes", default=None, frozen=True)
    directionText: Optional[str] = Field(alias="irany", default=None, frozen=True)
    id: Optional[int] = Field(alias="azonosito", default=None, frozen=True)
    recordDateAsString: Optional[str] = Field(alias="idopont", default=None, frozen=True)

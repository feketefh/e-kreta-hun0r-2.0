from typing import Optional
from pydantic import BaseModel, Field


class FiledDecision(BaseModel):
    id: Optional[int] = Field(alias="azonosito", default=None, frozen=True)

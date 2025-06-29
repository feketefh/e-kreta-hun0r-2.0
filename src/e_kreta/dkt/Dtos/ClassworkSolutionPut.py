from typing import Optional
from pydantic import BaseModel, Field


class ClassworkSolutionPut(BaseModel):
    text: Optional[str] = Field(alias="szoveg", default=None, frozen=True)

from typing import Optional
from pydantic import BaseModel, Field


class HomeworkSolutionPut(BaseModel):
    text: Optional[str] = Field(alias="szoveg", default=None, frozen=True)

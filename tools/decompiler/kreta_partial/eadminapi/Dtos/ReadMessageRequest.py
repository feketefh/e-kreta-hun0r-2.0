from typing import Optional
from pydantic import BaseModel, Field


class ReadMessageRequest(BaseModel):
    readByUser: Optional[bool] = Field(alias="isOlvasott", default=None, frozen=True)

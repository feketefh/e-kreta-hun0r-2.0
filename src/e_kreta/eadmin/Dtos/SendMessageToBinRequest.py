from typing import Optional
from pydantic import BaseModel, Field


class SendMessageToBinRequest(BaseModel):
    deleted: Optional[bool] = Field(alias="isKuka", default=None, frozen=True)

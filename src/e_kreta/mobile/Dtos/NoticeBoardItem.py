from typing import Optional
from pydantic import BaseModel, Field


class NoticeBoardItem(BaseModel):
    content: Optional[str] = Field(alias="Tartalom", default=None, frozen=True)
    expireEndTimeAsString: Optional[str] = Field(alias="ErvenyessegVege", default=None, frozen=True)
    expireStartTimeAsString: Optional[str] = Field(alias="ErvenyessegKezdete", default=None, frozen=True)
    madeBy: Optional[str] = Field(alias="RogzitoNeve", default=None, frozen=True)
    title: Optional[str] = Field(alias="Cim", default=None, frozen=True)
    uid: Optional[str] = Field(alias="Uid", default=None, frozen=True)

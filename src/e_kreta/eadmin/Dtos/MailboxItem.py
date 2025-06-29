from typing import Optional
from pydantic import BaseModel, Field


class MailboxItem(BaseModel):
    isDeleted: Optional[bool] = Field(alias="isToroltElem", default=None, frozen=True)
    message: Optional[Message] = Field(alias="uzenet", default=None, frozen=True)
    readByUser: Optional[bool] = Field(alias="isElolvasva", default=None, frozen=True)
    type: Optional[Type] = Field(alias="tipus", default=None, frozen=True)
    uid: Optional[str] = Field(alias="azonosito", default=None, frozen=True)

class Type(BaseModel):
    typeCode: Optional[str] = Field(alias="kod", default=None, frozen=True)
    typeDescription: Optional[str] = Field(alias="leiras", default=None, frozen=True)
    typeId: Optional[int] = Field(alias="azonosito", default=None, frozen=True)
    typeName: Optional[str] = Field(alias="nev", default=None, frozen=True)
    typeShortName: Optional[str] = Field(alias="rovidNev", default=None, frozen=True)

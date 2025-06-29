from typing import Optional
from pydantic import BaseModel, Field


class Message(BaseModel):
    addressList: Optional[list[Addressee]] = Field(alias="cimzettLista", default=None, frozen=True)
    addressesHidden: Optional[bool] = Field(alias="isCimzettekElrejtve", default=None, frozen=True)
    attachmentList: Optional[list[Attachment]] = Field(alias="csatolmanyok", default=None, frozen=True)
    messageId: Optional[int] = Field(alias="azonosito", default=None, frozen=True)
    messageSenderName: Optional[str] = Field(alias="feladoNev", default=None, frozen=True)
    messageSenderTitle: Optional[str] = Field(alias="feladoTitulus", default=None, frozen=True)
    messageSentDateAsString: Optional[str] = Field(alias="kuldesDatum", default=None, frozen=True)
    messageSubject: Optional[str] = Field(alias="targy", default=None, frozen=True)
    messageText: Optional[str] = Field(alias="szoveg", default=None, frozen=True)
    previousMessageId: Optional[int] = Field(alias="elozoUzenetAzonosito", default=None, frozen=True)

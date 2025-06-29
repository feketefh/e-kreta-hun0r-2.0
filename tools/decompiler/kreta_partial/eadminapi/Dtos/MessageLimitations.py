from typing import Optional
from pydantic import BaseModel, Field


class MessageLimitations(BaseModel):
    isMessageOnlyOneAddresseeLimitation: Optional[bool] = Field(alias="isCsakEgyCimzettLehet", default=None, frozen=True)
    isSendableMessagesLimitation: Optional[bool] = Field(alias="isKuldhetoUzenetekSzamaKorlatozvaVan", default=None, frozen=True)
    sendableMessagesTodayCount: Optional[int] = Field(alias="kuldhetoUzenetekSzamaMegMa", default=None, frozen=True)

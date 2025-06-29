from typing import Optional
from pydantic import BaseModel, Field


class BankAccountNumberPost(BaseModel):
    bankAccountNumber: Optional[str] = Field(alias="BankszamlaSzam", default=None, frozen=True)
    bankAccountOwnerName: Optional[str] = Field(alias="BankszamlaTulajdonosNeve", default=None, frozen=True)
    bankAccountOwnerType: Optional[int] = Field(alias="BankszamlaTulajdonosTipusId", default=None, frozen=True)
    bankName: Optional[str] = Field(alias="SzamlavezetoBank", default=None, frozen=True)

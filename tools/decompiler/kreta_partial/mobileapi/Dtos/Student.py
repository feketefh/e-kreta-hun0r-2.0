from typing import Optional
from pydantic import BaseModel, Field


class Student(BaseModel):
    addressDataList: Optional[list[str]] = Field(alias="Cimek", default=None, frozen=True)
    bankAccount: Optional[BankAccount] = Field(alias="Bankszamla", default=None, frozen=True)
    dayOfBirth: Optional[int] = Field(alias="SzuletesiNap", default=None, frozen=True)
    emailAddress: Optional[str] = Field(alias="EmailCim", default=None, frozen=True)
    guardianList: Optional[list[Guardian]] = Field(alias="Gondviselok", default=None, frozen=True)
    instituteCode: Optional[str] = Field(alias="IntezmenyAzonosito", default=None, frozen=True)
    instituteName: Optional[str] = Field(alias="IntezmenyNev", default=None, frozen=True)
    institution: Optional[Institution] = Field(alias="Intezmeny", default=None, frozen=True)
    monthOfBirth: Optional[int] = Field(alias="SzuletesiHonap", default=None, frozen=True)
    mothersName: Optional[str] = Field(alias="AnyjaNeve", default=None, frozen=True)
    name: Optional[str] = Field(alias="Nev", default=None, frozen=True)
    nameOfBirth: Optional[str] = Field(alias="SzuletesiNev", default=None, frozen=True)
    phoneNumber: Optional[str] = Field(alias="Telefonszam", default=None, frozen=True)
    placeOfBirth: Optional[str] = Field(alias="SzuletesiHely", default=None, frozen=True)
    schoolYearUID: Optional[int] = Field(alias="TanevUid", default=None, frozen=True)
    uid: Optional[str] = Field(alias="Uid", default=None, frozen=True)
    yearOfBirth: Optional[int] = Field(alias="SzuletesiEv", default=None, frozen=True)

class BankAccount(BaseModel):
    accountNumber: Optional[str] = Field(alias="BankszamlaSzam", default=None, frozen=True)
    isReadOnly: Optional[bool] = Field(alias="IsReadOnly", default=None, frozen=True)
    ownerName: Optional[str] = Field(alias="BankszamlaTulajdonosNeve", default=None, frozen=True)
    ownerType: Optional[int] = Field(alias="BankszamlaTulajdonosTipusId", default=None, frozen=True)

from typing import Optional
from pydantic import BaseModel, Field


class GuardianEAdmin(BaseModel):
    classId: Optional[int] = Field(alias="tanuloOsztalyKretaAzonosito", default=None, frozen=True)
    emailAddress: Optional[str] = Field(alias="emailCim", default=None, frozen=True)
    guardianName: Optional[str] = Field(alias="gondviseloNev", default=None, frozen=True)
    isLegalRepresentative: Optional[bool] = Field(alias="isTorvenyesKepviselo", default=None, frozen=True)
    isSzmk: Optional[bool] = Field(alias="isSZMK", default=None, frozen=True)
    isSzmkDeputy: Optional[bool] = Field(alias="isSZMKHelyettes", default=None, frozen=True)
    kretaId: Optional[int] = Field(alias="kretaAzonosito", default=None, frozen=True)
    relationType: Optional[str] = Field(alias="rokonsagiFok", default=None, frozen=True)
    studentClass: Optional[str] = Field(alias="tanuloOsztaly", default=None, frozen=True)
    studentId: Optional[str] = Field(alias="tanuloOktatasiAzonosito", default=None, frozen=True)
    studentName: Optional[str] = Field(alias="tanuloNev", default=None, frozen=True)
    szmkClass: Optional[str] = Field(alias="SZMKOsztaly", default=None, frozen=True)
    szmkClassDeputy: Optional[str] = Field(alias="sZMKOsztalyHelyettes", default=None, frozen=True)
    szmkClassDeputyKretaId: Optional[int] = Field(alias="sZMKOsztalyHelyettesKretaAzonosito", default=None, frozen=True)
    szmkClassKretaEmployee: Optional[int] = Field(alias="sZMKOsztalyKretaAlkalmazott", default=None, frozen=True)
    szmkClassKretaId: Optional[int] = Field(alias="sZMKOsztalyKretaAzonosito", default=None, frozen=True)

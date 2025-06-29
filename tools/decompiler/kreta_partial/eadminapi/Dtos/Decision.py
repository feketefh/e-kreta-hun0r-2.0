from typing import Optional
from pydantic import BaseModel, Field


class Decision(BaseModel):
    adjudication: Optional[str] = Field(alias="dontesSzovege", default=None, frozen=True)
    applicationMandatoryDocuments: Optional[list[ApplicationMandatoryDocument]] = Field(alias="hatarozatKotelezoDokumentumLista", default=None, frozen=True)
    attachments: Optional[list[Attachment]] = Field(alias="csatolmanyok", default=None, frozen=True)
    decisionDateAsString: Optional[str] = Field(alias="hatarozatDatum", default=None, frozen=True)
    filedDecision: Optional[FiledDecision] = Field(alias="iktatottHatarozat", default=None, frozen=True)
    id: Optional[str] = Field(alias="azonosito", default=None, frozen=True)
    judgement: Optional[Judgement] = Field(alias="dontes", default=None, frozen=True)
    justification: Optional[str] = Field(alias="indoklas", default=None, frozen=True)
    needToBeSendDigitally: Optional[bool] = Field(alias="isDigitalisanKikuldendo", default=None, frozen=True)
    postState: Optional[PostState] = Field(alias="postazasiStatusz", default=None, frozen=True)
    requestedAbsenceEndAsString: Optional[str] = Field(alias="igazoltTavolletVegeDatum", default=None, frozen=True)
    requestedAbsenceStartAsString: Optional[str] = Field(alias="igazoltTavolletKezdeteDatum", default=None, frozen=True)
    signerId: Optional[int] = Field(alias="alairoKretaAzonosito", default=None, frozen=True)

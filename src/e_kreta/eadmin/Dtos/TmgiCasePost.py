from typing import Optional
from pydantic import BaseModel, Field


class TmgiCasePost(BaseModel):
    caseType: Optional[Type] = Field(alias="igazolasTipus", default=None, frozen=True)
    educationClassName: Optional[str] = Field(alias="tanuloOsztaly", default=None, frozen=True)
    educationId: Optional[str] = Field(alias="tanuloOktatasiAzonosito", default=None, frozen=True)
    endDate: Optional[str] = Field(alias="igazoltTavolletVegeDatum", default=None, frozen=True)
    mandatoryAttachments: Optional[list[ApplicationMandatoryDocument]] = Field(alias="kerelemKotelezoDokumentumLista", default=None, frozen=True)
    optionalAttachments: Optional[list[OtherThingsToDoAttachments]] = Field(alias="csatolmanyok", default=None, frozen=True)
    reason: Optional[str] = Field(alias="indoklas", default=None, frozen=True)
    startDate: Optional[str] = Field(alias="igazoltTavolletKezdeteDatum", default=None, frozen=True)
    studentFirstName: Optional[str] = Field(alias="tanuloCsaladiNev", default=None, frozen=True)
    studentLastName: Optional[str] = Field(alias="tanuloKeresztNev", default=None, frozen=True)
    type: Optional[Type] = Field(alias="tipus", default=None, frozen=True)
    typeCode: Optional[str] = Field(alias="tipusKod", default=None, frozen=True)

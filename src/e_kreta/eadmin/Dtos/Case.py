from typing import Optional
from pydantic import BaseModel, Field


class Case(BaseModel):
    administrator: Optional[Administrator] = Field(alias="ugyintezo", default=None, frozen=True)
    applicants: Optional[Applicants] = Field(alias="kerelmezo", default=None, frozen=True)
    applicationMandatoryDocument: Optional[list[ApplicationMandatoryDocument]] = Field(alias="kerelemKotelezoDokumentumLista", default=None, frozen=True)
    attachments: Optional[list[Attachment]] = Field(alias="csatolmanyok", default=None, frozen=True)
    decisions: Optional[list[Decision]] = Field(alias="hatarozatLista", default=None, frozen=True)
    documentNumber: Optional[str] = Field(alias="ugyiratszam", default=None, frozen=True)
    filedApplication: Optional[FiledApplication] = Field(alias="iktatottKerelem", default=None, frozen=True)
    historyFileNumber: Optional[str] = Field(alias="elozmenyUgyiratszam", default=None, frozen=True)
    id: Optional[str] = Field(alias="azonosito", default=None, frozen=True)
    internalDeadlineDateAsString: Optional[str] = Field(alias="belsoHataridoDatum", default=None, frozen=True)
    internalNote: Optional[str] = Field(alias="belsoMegjegyzes", default=None, frozen=True)
    justificationType: Optional[Type] = Field(alias="igazolasTipus", default=None, frozen=True)
    lastModificationDateAsString: Optional[str] = Field(alias="utolsoModositasDatum", default=None, frozen=True)
    otherThingsToDoAttachments: Optional[list[OtherThingsToDoAttachments]] = Field(alias="teendoEgyebCsatolmanyok", default=None, frozen=True)
    postState: Optional[PostState] = Field(alias="postazasiStatusz", default=None, frozen=True)
    reason: Optional[str] = Field(alias="indoklas", default=None, frozen=True)
    registrationNumber: Optional[str] = Field(alias="iktatoszam", default=None, frozen=True)
    requestedAbsenceEndAsString: Optional[str] = Field(alias="igazoltTavolletVegeDatum", default=None, frozen=True)
    requestedAbsenceStartAsString: Optional[str] = Field(alias="igazoltTavolletKezdeteDatum", default=None, frozen=True)
    sentDateAsString: Optional[str] = Field(alias="bekuldesDatum", default=None, frozen=True)
    state: Optional[State] = Field(alias="statusz", default=None, frozen=True)
    studentClass: Optional[str] = Field(alias="tanuloOsztaly", default=None, frozen=True)
    studentEducationId: Optional[str] = Field(alias="tanuloOktatasiAzonosito", default=None, frozen=True)
    studentFamilyName: Optional[str] = Field(alias="tanuloCsaladiNev", default=None, frozen=True)
    studentFirstName: Optional[str] = Field(alias="tanuloKeresztNev", default=None, frozen=True)
    submittedDigitally: Optional[bool] = Field(alias="isDigitalisanBekuldve", default=None, frozen=True)
    toDoItem: Optional[list[ToDoItem]] = Field(alias="teendoLista", default=None, frozen=True)
    type: Optional[Type] = Field(alias="tipus", default=None, frozen=True)
    typeCode: Optional[str] = Field(alias="tipusKod", default=None, frozen=True)

class WhenMappings(BaseModel):

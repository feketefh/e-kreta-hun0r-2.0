from typing import Optional
from pydantic import BaseModel, Field


class ToDoItem(BaseModel):
    appellation: Optional[str] = Field(alias="megnevezes", default=None, frozen=True)
    documentTemplateId: Optional[int] = Field(alias="dokumentumSablonAzonosito", default=None, frozen=True)
    executiveId: Optional[int] = Field(alias="vegrehajtoKretaAzonosito", default=None, frozen=True)
    help: Optional[str] = Field(alias="segitseg", default=None, frozen=True)
    helpUrl: Optional[str] = Field(alias="segitsegUrl", default=None, frozen=True)
    id: Optional[int] = Field(alias="azonosito", default=None, frozen=True)
    isAutomatic: Optional[bool] = Field(alias="isAutomatikus", default=None, frozen=True)
    isOnline: Optional[bool] = Field(alias="isElektronizalt", default=None, frozen=True)
    isReady: Optional[bool] = Field(alias="isKesz", default=None, frozen=True)
    isSystemReady: Optional[bool] = Field(alias="isRendszerKesz", default=None, frozen=True)
    label: Optional[str] = Field(alias="cimke", default=None, frozen=True)
    sequence: Optional[str] = Field(alias="sorrend", default=None, frozen=True)
    systemReadyText: Optional[str] = Field(alias="rendszerKeszSzoveg", default=None, frozen=True)
    toDoMandatoryDocumentsList: Optional[ToDoMandatoryDocumentsList] = Field(alias="teendoKotelezoDokumentum", default=None, frozen=True)

from typing import Optional
from pydantic import BaseModel, Field


class EmployeeDetails(BaseModel):
    classSubstitute: Optional[str] = Field(alias="osztalyHelyettes", default=None, frozen=True)
    classSubstituteKretaId: Optional[int] = Field(alias="osztalyHelyettesKretaAzonosito", default=None, frozen=True)
    educatedId: Optional[str] = Field(alias="oktatasiAzonosito", default=None, frozen=True)
    educationClass: Optional[str] = Field(alias="osztaly", default=None, frozen=True)
    isAdmin: Optional[bool] = Field(alias="isAdmin", default=None, frozen=True)
    isClassMaster: Optional[bool] = Field(alias="isOsztalyfonok", default=None, frozen=True)
    isDeleted: Optional[bool] = Field(alias="isTorolt", default=None, frozen=True)
    isDeputyClassMaster: Optional[bool] = Field(alias="isOsztalyfonokHelyettes", default=None, frozen=True)
    isDeputyDirector: Optional[bool] = Field(alias="isIgazgatoHelyettes", default=None, frozen=True)
    isDirector: Optional[bool] = Field(alias="isIgazgato", default=None, frozen=True)
    isSignatory: Optional[bool] = Field(alias="isAlairo", default=None, frozen=True)
    isTeacher: Optional[bool] = Field(alias="isTanar", default=None, frozen=True)
    kretaClassId: Optional[int] = Field(alias="osztalyKretaAzonosito", default=None, frozen=True)
    kretaId: Optional[int] = Field(alias="kretaAzonosito", default=None, frozen=True)
    name: Optional[str] = Field(alias="nev", default=None, frozen=True)
    title: Optional[str] = Field(alias="titulus", default=None, frozen=True)

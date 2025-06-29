from typing import Optional
from pydantic import BaseModel, Field


class Institution(BaseModel):
    customizationSettings: Optional[CustomizationSettings] = Field(alias="TestreszabasBeallitasok", default=None, frozen=True)
    fullName: Optional[str] = Field(alias="TeljesNev", default=None, frozen=True)
    shortName: Optional[str] = Field(alias="RovidNev", default=None, frozen=True)
    systemModuleList: Optional[list[SystemModule]] = Field(alias="Rendszermodulok", default=None, frozen=True)
    uid: Optional[str] = Field(alias="Uid", default=None, frozen=True)

class CustomizationSettings(BaseModel):
    delayOfNotifications: Optional[int] = Field(alias="ErtekelesekMegjelenitesenekKesleltetesenekMerteke", default=None, frozen=True)
    isClassAverageVisible: Optional[bool] = Field(alias="IsOsztalyAtlagMegjeleniteseEllenorzoben", default=None, frozen=True)
    isContactDataEditable: Optional[bool] = Field(alias="IsElerhetosegSzerkesztheto", default=None, frozen=True)
    isLessonsThemeVisible: Optional[bool] = Field(alias="IsTanorakTemajaMegtekinthetoEllenorzoben", default=None, frozen=True)
    nextServerDeployAsString: Optional[str] = Field(alias="KovetkezoTelepitesDatuma", default=None, frozen=True)

class SystemModule(BaseModel):
    isActive: Optional[bool] = Field(alias="IsAktiv", default=None, frozen=True)
    type: Optional[str] = Field(alias="Tipus", default=None, frozen=True)
    url: Optional[str] = Field(alias="Url", default=None, frozen=True)

from typing import Optional
from pydantic import BaseModel, Field


class CurrentInstitutionDetails(BaseModel):
    cashReportIdPrefix: Optional[str] = Field(alias="penztarjelentesAzonositoElotag", default=None, frozen=True)
    educationDistrictName: Optional[str] = Field(alias="tankeruletNeve", default=None, frozen=True)
    id: Optional[int] = Field(alias="azonosito", default=None, frozen=True)
    institutionAddress: Optional[str] = Field(alias="intezmenyCim", default=None, frozen=True)
    institutionId: Optional[str] = Field(alias="kretaIntezmenyAzonosito", default=None, frozen=True)
    isBasicLevel: Optional[bool] = Field(alias="isAltalanos", default=None, frozen=True)
    isMessageHandlingAccessible: Optional[bool] = Field(alias="IsUzenetKezelesElerheto", default=None, frozen=True)
    isMidLevel: Optional[bool] = Field(alias="isKozepfoku", default=None, frozen=True)
    isSzeusz: Optional[bool] = Field(alias="isSzeusz", default=None, frozen=True)
    name: Optional[str] = Field(alias="nev", default=None, frozen=True)
    notificationEmailAddress: Optional[str] = Field(alias="ertesitesiEmailCim", default=None, frozen=True)
    omId: Optional[str] = Field(alias="omAzonosito", default=None, frozen=True)

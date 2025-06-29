from typing import Optional
from pydantic import BaseModel, Field


class DriversLicenseRegistrationStatus(BaseModel):
    approvalDate: Optional[str] = Field(alias="gondviseloJovahagytaDatum", default=None, frozen=True)
    approvedBy: Optional[str] = Field(alias="gondviseloNev", default=None, frozen=True)
    id: Optional[int] = Field(alias="id", default=None, frozen=True)
    isApprovedByGuardian: Optional[bool] = Field(alias="gondviseloJovahagyta", default=None, frozen=True)
    mothersGivenName: Optional[str] = Field(alias="anyjaNeveUtoNev", default=None, frozen=True)
    mothersNamePrefix: Optional[str] = Field(alias="anyjaNeveElotag", default=None, frozen=True)
    mothersSurname: Optional[str] = Field(alias="anyjaNeveVezetekNev", default=None, frozen=True)
    studentBirthGivenName: Optional[str] = Field(alias="szuletesiUtoNev", default=None, frozen=True)
    studentBirthNamePrefix: Optional[str] = Field(alias="szuletesiNevElotag", default=None, frozen=True)
    studentBirthSurname: Optional[str] = Field(alias="szuletesiVezetekNev", default=None, frozen=True)
    studentDateOfBirth: Optional[str] = Field(alias="szuletesiDatum", default=None, frozen=True)
    studentGivenName: Optional[str] = Field(alias="utoNev", default=None, frozen=True)
    studentNamePrefix: Optional[str] = Field(alias="nevElotag", default=None, frozen=True)
    studentPlaceOfBirth: Optional[str] = Field(alias="szuletesiHely", default=None, frozen=True)
    studentSurname: Optional[str] = Field(alias="vezetekNev", default=None, frozen=True)

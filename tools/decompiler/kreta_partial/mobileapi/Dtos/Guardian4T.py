from typing import Optional
from pydantic import BaseModel, Field


class Guardian4T(BaseModel):
    dateOfBirthAsString: Optional[str] = Field(alias="SzuletesiDatum", default=None, frozen=True)
    firstname: Optional[str] = Field(alias="Utonev", default=None, frozen=True)
    firstnameOfBirth: Optional[str] = Field(alias="SzuletesiUtonev", default=None, frozen=True)
    mothersFirstname: Optional[str] = Field(alias="AnyjaUtonev", default=None, frozen=True)
    mothersSurname: Optional[str] = Field(alias="AnyjaVezeteknev", default=None, frozen=True)
    namePrefix: Optional[str] = Field(alias="Elotag", default=None, frozen=True)
    placeOfBirth: Optional[str] = Field(alias="SzuletesiHely", default=None, frozen=True)
    surname: Optional[str] = Field(alias="Vezeteknev", default=None, frozen=True)
    surnameOfBirth: Optional[str] = Field(alias="SzuletesiVezeteknev", default=None, frozen=True)

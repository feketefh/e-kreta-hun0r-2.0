from typing import Optional
from pydantic import BaseModel, Field


class ClassMaster(BaseModel):
    listOfClass: Optional[list[SchoolClass]] = Field(alias="Osztalyai", default=None, frozen=True)
    teacher: Optional[Teacher] = Field(alias="Tanar", default=None, frozen=True)
    uid: Optional[str] = Field(alias="Uid", default=None, frozen=True)

class Email(BaseModel):
    email: Optional[str] = Field(alias="Email", default=None, frozen=True)
    uid: Optional[str] = Field(alias="Uid", default=None, frozen=True)

class Employee(BaseModel):
    emailList: Optional[list[Email]] = Field(alias="Emailek", default=None, frozen=True)
    name: Optional[str] = Field(alias="Nev", default=None, frozen=True)
    phoneList: Optional[list[Phone]] = Field(alias="Telefonok", default=None, frozen=True)
    uid: Optional[str] = Field(alias="Uid", default=None, frozen=True)

class Phone(BaseModel):
    phone: Optional[str] = Field(alias="Telefonszam", default=None, frozen=True)
    uid: Optional[str] = Field(alias="Uid", default=None, frozen=True)

class Teacher(BaseModel):
    employee: Optional[Employee] = Field(alias="Alkalmazott", default=None, frozen=True)
    uid: Optional[str] = Field(alias="Uid", default=None, frozen=True)

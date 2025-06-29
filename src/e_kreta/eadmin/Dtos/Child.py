from typing import Optional
from pydantic import BaseModel, Field


class Child(BaseModel):
    educationId: Optional[int] = Field(alias="oktatasiAzonosito", default=None, frozen=True)
    firstName: Optional[str] = Field(alias="vezetekNev", default=None, frozen=True)
    lastName: Optional[str] = Field(alias="keresztNev", default=None, frozen=True)
    studentClass: Optional[str] = Field(alias="osztaly", default=None, frozen=True)

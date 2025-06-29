from typing import Optional
from pydantic import BaseModel, Field


class TeszekRegistration(BaseModel):
    id: Optional[str] = Field(alias="Id", default=None, frozen=True)
    registrationDateAsString: Optional[str] = Field(alias="RegisztracioIdopontja", default=None, frozen=True)

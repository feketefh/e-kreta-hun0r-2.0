from typing import Optional
from pydantic import BaseModel, Field


class ClassworkTeachingMaterial(BaseModel):
    classworkId: Optional[int] = Field(alias="feladatId", default=None, frozen=True)
    id: Optional[int] = Field(alias="id", default=None, frozen=True)
    link: Optional[str] = Field(alias="link", default=None, frozen=True)
    materialTypeId: Optional[int] = Field(alias="forrasTipusId", default=None, frozen=True)
    title: Optional[str] = Field(alias="cim", default=None, frozen=True)

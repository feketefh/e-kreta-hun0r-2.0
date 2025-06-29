from typing import Optional
from pydantic import BaseModel, Field


class LanguageTask(BaseModel):
    creationTimeAsString: Optional[str] = Field(alias="rogzitesIdopontja", default=None, frozen=True)
    deadlineAsString: Optional[str] = Field(alias="beadasiHatarido", default=None, frozen=True)
    groupId: Optional[str] = Field(alias="groupId", default=None, frozen=True)
    id: Optional[int] = Field(alias="id", default=None, frozen=True)
    subTaskList: Optional[list[LanguageSubTask]] = Field(alias="alfeladatok", default=None, frozen=True)
    text: Optional[str] = Field(alias="szoveg", default=None, frozen=True)
    title: Optional[str] = Field(alias="cim", default=None, frozen=True)

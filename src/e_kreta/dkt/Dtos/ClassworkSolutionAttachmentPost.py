from typing import Optional
from pydantic import BaseModel, Field


class ClassworkSolutionAttachmentPost(BaseModel):
    fileId: Optional[str] = Field(alias="fajlId", default=None, frozen=True)
    fileName: Optional[str] = Field(alias="teljesFajlNev", default=None, frozen=True)
    sizeInBytes: Optional[int] = Field(alias="meretInBytes", default=None, frozen=True)
